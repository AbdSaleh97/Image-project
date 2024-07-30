from django.urls import path
from .views import home_view, image_detail_view

urlpatterns = [
    path("", home_view, name="image-list"), 
    path("image/<int:pk>/", image_detail_view, name="image-detail"), 
]
