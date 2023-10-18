from django.urls import path
from .views import cat_pictures, cat_picture_detail

urlpatterns = [
    path('', cat_pictures, name='cat_pictures'),
    path('<int:cat_picture_id>', cat_picture_detail, name='cat_picture_detail'),
]
