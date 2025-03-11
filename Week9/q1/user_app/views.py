from django.shortcuts import render
from .forms import UserRegistrationForm

def register_view(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            email = form.cleaned_data.get('email', '')
            contact_number = form.cleaned_data.get('contact_number', '')

            # Sending the data to success page using GET parameters
            return render(request, 'user_app/success.html', {
                'username': username,
                'email': email,
                'contact_number': contact_number
            })
    else:
        form = UserRegistrationForm()

    return render(request, 'user_app/register.html', {'form': form})

def success_view(request):
    return render(request, 'user_app/success.html')
