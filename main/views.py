from django.shortcuts import render

def home(request):
    context = {
        "app_name": "Kalcer Shop",
        "student_name": "Freya Zahra",   
        "student_class": "PBP F"        
    }
    return render(request, "main.html", context) 

#render = cara Django “mengirim” variabel itu ke file HTML (main.html).
#jadi intinya di views ini kita kayak simpan varibel buat bisa di aksem di main.html
