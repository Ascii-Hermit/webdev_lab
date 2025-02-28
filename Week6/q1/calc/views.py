# calc/views.py

from django.shortcuts import render
from .forms import ArithmeticForm

def calculate(request):
    result = None
    if request.method == 'POST':
        form = ArithmeticForm(request.POST)
        if form.is_valid():
            num1 = form.cleaned_data['num1']
            num2 = form.cleaned_data['num2']
            operation = form.cleaned_data['operation']

            if operation == '+':
                result = num1 + num2
            elif operation == '-':
                result = num1 - num2
            elif operation == '*':
                result = num1 * num2
            elif operation == '/':
                if num2 != 0:
                    result = num1 / num2
                else:
                    result = 'Error: Division by zero'

    else:
        form = ArithmeticForm()

    return render(request, 'calc/calculator.html', {'form': form, 'result': result})
