from django import forms

class MagazineCoverForm(forms.Form):
    image = forms.ImageField(label='Upload Image')
    background_color = forms.CharField(max_length=7, label='Background Color', initial="#ffffff", widget=forms.TextInput(attrs={'placeholder': 'e.g. #ffffff'}))
    text = forms.CharField(widget=forms.Textarea(attrs={'placeholder': 'Enter your text here'}), label='Cover Text')
    font_size = forms.IntegerField(min_value=10, max_value=100, label='Font Size', initial=30)
    font_color = forms.CharField(max_length=7, label='Font Color', initial="#000000", widget=forms.TextInput(attrs={'placeholder': 'e.g. #000000'}))
