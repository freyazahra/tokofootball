// Open Modal
function openModal(modalId) {
    const modal = document.getElementById(modalId);
    modal.classList.remove('hidden');
    document.body.style.overflow = 'hidden';
}

// Close Modal
function closeModal(modalId) {
    const modal = document.getElementById(modalId);
    modal.classList.add('hidden');
    document.body.style.overflow = 'auto';
}

// Show Add Product Modal
function showAddProductModal() {
    fetch('/create-product-ajax/')
        .then(response => response.text())
        .then(html => {
            document.getElementById('modalTitle').textContent = 'Add New Product';
            document.getElementById('modalBody').innerHTML = html;
            openModal('crudModal');
        })
        .catch(error => {
            console.error('Error loading add product form:', error);
            showToast('Failed to load the form. Please try again.', 'error');
        });
}

// Show Edit Product Modal
function showEditProductModal(productId) {
    fetch(`/edit-product-ajax/${productId}/`)
        .then(response => response.text())
        .then(html => {
            document.getElementById('modalTitle').textContent = 'Edit Product';
            document.getElementById('modalBody').innerHTML = html;
            openModal('crudModal');
        })
        .catch(error => {
            console.error('Error loading edit product form:', error);
            showToast('Failed to load the form. Please try again.', 'error');
        });
}

// Show Product Detail Modal
function showProductDetailModal(productId) {
    fetch(`/product-detail-ajax/${productId}/`)
        .then(response => response.text())
        .then(html => {
            document.getElementById('productDetailBody').innerHTML = html;
            openModal('productDetailModal');
        })
        .catch(error => {
            console.error('Error loading product details:', error);
            showToast('Failed to load product details. Please try again.', 'error');
        });
}

// Submit Product Form (for both Add and Edit)
function submitProductForm(event, formId) {
    event.preventDefault();
    
    const form = document.getElementById(formId);
    const formData = new FormData(form);
    const url = form.action;
    
    fetch(url, {
        method: 'POST',
        body: formData,
        headers: {
            'X-Requested-With': 'XMLHttpRequest',
        }
    })
    .then(response => response.json())
    .then(data => {
        if (data.success) {
            // Close modal
            closeModal('crudModal');
            
            // Show success message
            showToast(data.message || 'Operation successful!', 'success');
            
            // Reload products or refresh the page
            setTimeout(() => {
                location.reload();
            }, 1000);
        } else {
            // Show errors in the form
            if (data.errors) {
                displayFormErrors(data.errors);
            } else {
                showToast(data.message || 'An error occurred', 'error');
            }
        }
    })
    .catch(error => {
        console.error('Error submitting form:', error);
        showToast('Failed to submit form. Please try again.', 'error');
    });
}

// Display form errors
function displayFormErrors(errors) {
    // Clear previous errors
    document.querySelectorAll('.error-message').forEach(el => el.remove());
    document.querySelectorAll('.border-red-500').forEach(el => {
        el.classList.remove('border-red-500');
        el.classList.add('border-gray-300');
    });
    
    // Display new errors
    for (const [field, messages] of Object.entries(errors)) {
        const input = document.querySelector(`[name="${field}"]`);
        if (input) {
            input.classList.remove('border-gray-300');
            input.classList.add('border-red-500');
            
            const errorDiv = document.createElement('div');
            errorDiv.className = 'error-message text-red-500 text-sm mt-1';
            errorDiv.textContent = messages.join(', ');
            input.parentNode.appendChild(errorDiv);
        }
    }
}

// Show toast notification
function showToast(message, type = 'info') {
    const toastContainer = document.getElementById('toastContainer');
    if (!toastContainer) {
        console.log(message);
        return;
    }
    
    const toastId = 'toast-' + Date.now();
    
    let bgColor, icon;
    switch(type) {
        case 'success':
            bgColor = 'bg-green-500';
            icon = 'fa-check-circle';
            break;
        case 'error':
            bgColor = 'bg-red-500';
            icon = 'fa-exclamation-circle';
            break;
        default:
            bgColor = 'bg-blue-500';
            icon = 'fa-info-circle';
    }
    
    const toastHTML = `
        <div id="${toastId}" class="transform transition-all duration-300 ${bgColor} text-white px-6 py-4 rounded-lg shadow-lg flex items-center space-x-3 min-w-[300px]">
            <i class="fas ${icon} text-xl"></i>
            <span class="flex-1">${message}</span>
            <button onclick="removeToast('${toastId}')" class="text-white hover:text-gray-200">
                <i class="fas fa-times"></i>
            </button>
        </div>
    `;
    
    toastContainer.insertAdjacentHTML('beforeend', toastHTML);
    
    // Auto remove after 5 seconds
    setTimeout(() => {
        removeToast(toastId);
    }, 5000);
}

// Remove toast
function removeToast(toastId) {
    const toast = document.getElementById(toastId);
    if (toast) {
        toast.classList.add('opacity-0');
        setTimeout(() => {
            toast.remove();
        }, 300);
    }
}

// Delete Product with Confirmation
function deleteProduct(productId) {
    if (confirm('Are you sure you want to delete this product?')) {
        fetch(`/delete-product-ajax/${productId}/`, {
            method: 'POST',
            headers: {
                'X-CSRFToken': getCookie('csrftoken'),
                'X-Requested-With': 'XMLHttpRequest',
            }
        })
        .then(response => response.json())
        .then(data => {
            if (data.success) {
                showToast(data.message || 'Product deleted successfully!', 'success');
                setTimeout(() => {
                    location.reload();
                }, 1000);
            } else {
                showToast(data.message || 'Failed to delete product', 'error');
            }
        })
        .catch(error => {
            console.error('Error deleting product:', error);
            showToast('Failed to delete product. Please try again.', 'error');
        });
    }
}

// Get CSRF token from cookies
function getCookie(name) {
    let cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        const cookies = document.cookie.split(';');
        for (let i = 0; i < cookies.length; i++) {
            const cookie = cookies[i].trim();
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}

// Close modal when clicking outside
window.onclick = function(event) {
    const crudModal = document.getElementById('crudModal');
    const detailModal = document.getElementById('productDetailModal');
    
    if (event.target === crudModal) {
        closeModal('crudModal');
    }
    if (event.target === detailModal) {
        closeModal('productDetailModal');
    }
}