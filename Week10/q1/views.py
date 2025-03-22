from django.shortcuts import render, redirect, get_object_or_404
from .forms import CategoryForm, PageForm
from .models import Category, Page

def index(request):
    return render(request, 'q1/index.html')

def category_list(request):
    categories = Category.objects.all()
    return render(request, 'q1/category_list.html', {'categories': categories})

def page_list(request):
    pages = Page.objects.all()
    return render(request, 'q1/page_list.html', {'pages': pages})

def category_create(request):
    if request.method == 'POST':
        form = CategoryForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('category_list')
    else:
        form = CategoryForm()
    return render(request, 'q1/category_form.html', {'form': form})

def page_create(request):
    if request.method == 'POST':
        form = PageForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('page_list')
    else:
        form = PageForm()
    return render(request, 'q1/page_form.html', {'form': form})

def category_detail(request, pk):
    category = get_object_or_404(Category, pk=pk)
    pages = Page.objects.filter(category=category)
    return render(request, 'q1/category_detail.html', {'category': category, 'pages': pages})