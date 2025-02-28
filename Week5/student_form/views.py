# student_app/views.py

from django.shortcuts import render
from .forms import StudentForm

def student_form(request):
    percentage = None
    student_details = None

    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            dob = form.cleaned_data['dob']
            address = form.cleaned_data['address']
            contact = form.cleaned_data['contact']
            email = form.cleaned_data['email']
            english = form.cleaned_data['english_marks']
            physics = form.cleaned_data['physics_marks']
            chemistry = form.cleaned_data['chemistry_marks']

            # Calculate percentage
            total_marks = english + physics + chemistry
            percentage = (total_marks / 300) * 100  # Total is out of 300

            # Prepare student details for display
            student_details = {
                'name': name,
                'dob': dob,
                'address': address,
                'contact': contact,
                'email': email,
                'english_marks': english,
                'physics_marks': physics,
                'chemistry_marks': chemistry,
                'total_marks': total_marks,
                'percentage': percentage,
            }
    else:
        form = StudentForm()

    return render(request, 'student_form/student_form.html', {'form': form, 'student_details': student_details, 'percentage': percentage})
