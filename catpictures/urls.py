from django.urls import path
#from .views import CatPictureListCreateView, CatPictureDetailView
from .views import get_cat_pictures, create_cat_picture, cat_picture_detail

urlpatterns = [
    path('', get_cat_pictures, name='get_cat_pictures'),
    path('create/', create_cat_picture, name='create_cat_picture'),
    path('<int:cat_picture_id>/', cat_picture_detail, name='cat_picture_detail'),
]
