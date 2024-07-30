from django.shortcuts import render, get_object_or_404
from .models import Image
import requests

# Define your API key and category
API_KEY = "45190622-133e1a9d44e0b599901454a1a"
CATEGORY = "food"

def fetch_images():
    response = requests.get(f"https://pixabay.com/api/?key={API_KEY}&q={CATEGORY}&image_type=photo&pretty=true")
    return response.json()

def home_view(request):
    api_data = fetch_images()

    for image in api_data["hits"]:
        if not Image.objects.filter(image_url=image["largeImageURL"]).exists():
            Image.objects.create(
                title=image["tags"],
                image_url=image["largeImageURL"],
                photographer=image["user"],
                description=image["tags"],
            )

    images = Image.objects.all()
    return render(request, "index.html", {"images": images})

def image_detail_view(request, pk):
    image = get_object_or_404(Image, pk=pk)
    return render(request, "detail.html", {"image": image})
