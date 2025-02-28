# magazine/views.py

from django.shortcuts import render
from .forms import MagazineCoverForm
from django.core.files.storage import FileSystemStorage

def generate_cover(request):
    form = MagazineCoverForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        # Get form data
        image = form.cleaned_data['image']
        background_color = form.cleaned_data['background_color']
        text = form.cleaned_data['text']
        font_size = form.cleaned_data['font_size']
        font_color = form.cleaned_data['font_color']

        # Save the image to the filesystem
        fs = FileSystemStorage()
        filename = fs.save(image.name, image)
        image_url = fs.url(filename)  # This gives the correct URL to the media file

        return render(request, 'magazine/cover.html', {
            'form': form,
            'image_url': image_url,  # Send the URL to the template
            'background_color': background_color,
            'text': text,
            'font_size': font_size,
            'font_color': font_color,
        })
    return render(request, 'magazine/cover.html', {'form': form})
