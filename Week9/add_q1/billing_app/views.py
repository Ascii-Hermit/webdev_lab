from django.shortcuts import render, redirect
from .forms import BillForm

def page1(request):
    if request.method == 'POST':
        form = BillForm(request.POST)
        if form.is_valid():
            request.session['brand'] = form.cleaned_data['brand']
            request.session['items'] = form.cleaned_data['items']
            request.session['quantity'] = form.cleaned_data['quantity']
            return redirect('page2')  
    else:
        form = BillForm()

    return render(request, 'billing_app/page1.html', {'form': form})

def page2(request):
    brand = request.session.get('brand')
    items = request.session.get('items')
    quantity = request.session.get('quantity')

    price_list = {
        'HP': 500,
        'Nokia': 400,
        'Samsung': 600,
        'Motorola': 550,
        'Apple': 800
    }
    item_prices = {
        'Mobile': 1000,
        'Laptop': 3000
    }

    total_amount = 0
    for item in items:
        total_amount += item_prices.get(item, 0) * quantity

    return render(request, 'billing_app/page2.html', {
        'brand': brand,
        'items': items,
        'quantity': quantity,
        'total_amount': total_amount,
    })
