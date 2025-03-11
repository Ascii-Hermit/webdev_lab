from django import forms

class CarForm(forms.Form):
    car_manufacturers = [
        ('toyota', 'Toyota'),
        ('ford', 'Ford'),
        ('bmw', 'BMW'),
        ('honda', 'Honda'),
        ('audi', 'Audi')
    ]
    
    manufacturer = forms.ChoiceField(choices=car_manufacturers, label='Select Manufacturer')
    model_name = forms.CharField(max_length=100, label='Enter Model Name')
