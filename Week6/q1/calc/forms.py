from django import forms

class ArithmeticForm(forms.Form):
    num1 = forms.IntegerField(label='First Number')
    num2 = forms.IntegerField(label='Second Number')
    operation = forms.ChoiceField(choices=[('+', 'Add'), ('-', 'Subtract'), ('*', 'Multiply'), ('/', 'Divide')], label='Operation')
