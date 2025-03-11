from django.shortcuts import render, redirect
from .forms import CGPAForm

def page1(request):
    if request.method == "POST":
        form = CGPAForm(request.POST)
        if form.is_valid():
            request.session['name'] = form.cleaned_data['name']
            request.session['total_marks'] = form.cleaned_data['total_marks']
            return redirect('page2')  
    else:
        form = CGPAForm()
    return render(request, 'cgpa_app/page1.html', {'form': form})

def page2(request):
    name = request.session.get('name')
    total_marks = request.session.get('total_marks')
    if name and total_marks is not None:
        cgpa = total_marks / 50  
        return render(request, 'cgpa_app/page2.html', {'name': name, 'cgpa': cgpa})
    else:
        return redirect('page1')  
