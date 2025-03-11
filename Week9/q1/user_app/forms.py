from django import forms

class UserRegistrationForm(forms.Form):
    username = forms.CharField(max_length=100, required=True, label="Username")
    password = forms.CharField(widget=forms.PasswordInput(), label="Password", required=False)
    email = forms.EmailField(label="Email", required=False)
    contact_number = forms.CharField(max_length=15, label="Contact Number", required=False)
