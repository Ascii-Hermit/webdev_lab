# user_info/views.py

from django.shortcuts import render, redirect

def first_page(request):
    if request.method == 'POST':
        # Retrieve data from the form and save it in the session
        name = request.POST.get('name')
        roll = request.POST.get('roll')
        subject = request.POST.get('subject')
        
        # Store data in session
        request.session['name'] = name
        request.session['roll'] = roll
        request.session['subject'] = subject
        
        # Redirect to second page
        return redirect('second_page')

    return render(request, 'user_info/firstPage.html')

def second_page(request):
    # Get data from the session
    name = request.session.get('name', 'Not Provided')
    roll = request.session.get('roll', 'Not Provided')
    subject = request.session.get('subject', 'Not Provided')

    return render(request, 'user_info/secondPage.html', {
        'name': name,
        'roll': roll,
        'subject': subject,
    })
