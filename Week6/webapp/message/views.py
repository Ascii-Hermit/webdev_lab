from django.shortcuts import render

def home(request):
    name = ''
    message = ''
    bold = False
    italic = False
    underline = False
    color = 'black'

    if request.method == 'POST':
        # Get data from the form
        name = request.POST.get('name', '')
        message = request.POST.get('message', '')
        bold = 'bold' in request.POST
        italic = 'italic' in request.POST
        underline = 'underline' in request.POST
        color = request.POST.get('color', 'black')

    context = {
        'name': name,
        'message': message,
        'bold': bold,
        'italic': italic,
        'underline': underline,
        'color': color
    }
    
    return render(request, 'message/home.html', context)
