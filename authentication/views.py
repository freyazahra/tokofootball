import json
from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout
from django.contrib.auth.models import User
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt


def _get_request_data(request):
    if request.content_type == 'application/json':
        try:
            return json.loads(request.body.decode('utf-8'))
        except Exception:
            return {}
    return request.POST


@csrf_exempt
def login(request):
    """Login endpoint for Flutter integration.

    Accepts form-encoded or JSON POST with `username` and `password`.
    Sets session cookie on successful login (use withCredentials on client).
    """
    if request.method != 'POST':
        return JsonResponse({'status': False, 'message': 'Use POST.'}, status=405)

    data = _get_request_data(request)
    username = data.get('username')
    password = data.get('password')

    if not username or not password:
        return JsonResponse({'status': False, 'message': 'username and password required'}, status=400)

    user = authenticate(username=username, password=password)
    if user is not None:
        if user.is_active:
            auth_login(request, user)
            return JsonResponse({
                'username': user.username,
                'status': True,
                'message': 'Login successful!'
            }, status=200)
        else:
            return JsonResponse({'status': False, 'message': 'Account disabled.'}, status=401)

    return JsonResponse({'status': False, 'message': 'Invalid credentials.'}, status=401)


@csrf_exempt
def register(request):
    """Register endpoint for Flutter integration.
    Accepts POST with `username`, `password1`, `password2` (and optional `email`).
    """
    if request.method != 'POST':
        return JsonResponse({'status': False, 'message': 'Use POST.'}, status=405)

    data = _get_request_data(request)
    username = data.get('username')
    password1 = data.get('password1')
    password2 = data.get('password2')
    email = data.get('email', '')

    # Validate presence
    if not username or not password1 or not password2:
        return JsonResponse({'status': False, 'message': 'username and both passwords required'}, status=400)

    # Check password match
    if password1 != password2:
        return JsonResponse({'status': False, 'message': 'Passwords do not match.'}, status=400)

    if User.objects.filter(username=username).exists():
        return JsonResponse({'status': False, 'message': 'Username already exists.'}, status=400)

    user = User.objects.create_user(username=username, password=password1, email=email)
    user.save()
    return JsonResponse({'username': user.username, 'status': 'success', 'message': 'User created successfully!'}, status=200)


@csrf_exempt
def logout(request):
    username = getattr(request.user, 'username', None)
    try:
        auth_logout(request)
        return JsonResponse({
            'username': username,
            'status': True,
            'message': 'Logged out successfully!'
        }, status=200)
    except Exception:
        return JsonResponse({'status': False, 'message': 'Logout failed.'}, status=401)
