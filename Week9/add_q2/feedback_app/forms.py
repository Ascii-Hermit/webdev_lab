from django import forms

class FeedbackForm(forms.Form):
    name = forms.CharField(label="Name", max_length=100)
    email = forms.EmailField(label="Email")
    feedback_choice = forms.ChoiceField(
        choices=[('ASP-XML', 'ASP-XML'),
                 ('DotNET', 'DotNET'),
                 ('JavaPro', 'JavaPro'),
                 ('Unix', 'Unix'),
                 ('C', 'C'),
                 ('C++', 'C++')],
        widget=forms.Select
    )
