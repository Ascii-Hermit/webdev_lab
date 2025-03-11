from django import forms

class BillForm(forms.Form):
    mobile_brand_choices = [
        ('HP', 'HP'),
        ('Nokia', 'Nokia'),
        ('Samsung', 'Samsung'),
        ('Motorola', 'Motorola'),
        ('Apple', 'Apple'),
    ]
    brand = forms.ChoiceField(choices=mobile_brand_choices, widget=forms.RadioSelect)
    items = forms.MultipleChoiceField(choices=[('Mobile', 'Mobile'), ('Laptop', 'Laptop')], widget=forms.CheckboxSelectMultiple)
    quantity = forms.IntegerField(min_value=1)
