# grocery_app/views.py

from django.shortcuts import render

def grocery_list(request):
    # Grocery items with their prices
    grocery_items = [
        {'name': 'Apple', 'price': 2},
        {'name': 'Banana', 'price': 1},
        {'name': 'Carrot', 'price': 1.5},
        {'name': 'Dairy Milk', 'price': 3},
        {'name': 'Eggs', 'price': 2.5},
        {'name': 'Flour', 'price': 0.8},
        {'name': 'Grapes', 'price': 3},
        {'name': 'Honey', 'price': 5},
    ]

    # Initialize selected_items
    selected_items = []

    if request.method == 'POST':
        # Get the selected items from the form
        selected_items_names = request.POST.getlist('items')  # Get all selected item names

        # Match selected items with their prices
        for item in grocery_items:
            if item['name'] in selected_items_names:
                selected_items.append(item)

    # Ensure the correct template name is passed here
    return render(request, 'grocery_app/grocery_list.html', {
        'grocery_items': grocery_items,  # Pass grocery items here
        'selected_items': selected_items  # Pass selected items here
    })
