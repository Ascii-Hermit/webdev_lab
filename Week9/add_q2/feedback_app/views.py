from django.shortcuts import render
from .forms import FeedbackForm

def feedback_view(request):
    message = ""
    if request.method == 'POST':
        form = FeedbackForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            feedback_choice = form.cleaned_data['feedback_choice']
            
            message = f"Thank you for your feedback, {name}! You chose '{feedback_choice}' as your feedback option."
    else:
        form = FeedbackForm()

    return render(request, 'feedback_app/feedback_form.html', {'form': form, 'message': message})
