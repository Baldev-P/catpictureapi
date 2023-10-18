import os

from django.shortcuts import render
from rest_framework import generics, renderers
from .models import CatPicture
from .serializers import CatPictureSerializer
from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly, AllowAny
from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema

# Create your views here.

@swagger_auto_schema(
    method="POST",
    request_body=openapi.Schema(
        type=openapi.TYPE_OBJECT,
        required=["title", "image"],
        properties={
            "title": openapi.Schema(type=openapi.TYPE_STRING, description="Title of the cat picture"),
            "image": openapi.Schema(type=openapi.TYPE_FILE, description="Image file of the cat picture"),
            "description": openapi.Schema(type=openapi.TYPE_STRING, description="Description of the cat picture"),
        },
    ),
    responses={201: openapi.Response("CatPictureSerializer")},
    operation_description="Create a new cat picture.",
)
@api_view(['GET','POST'])
@permission_classes([AllowAny])#IsAuthenticatedOrReadOnly])
def cat_pictures(request):
    """
    Get a list of all cat pictures or create a new cat picture.
    """
    if request.method == 'GET':
        try:
            # Get the 'limit' and 'offset' parameters from the request, defaulting to 10 and 0 if not provided
            limit = int(request.GET.get('limit', 10))
            offset = int(request.GET.get('offset', 0))
            # Retrieve cat pictures using limit and offset
            cat_pictures = CatPicture.objects.all()[offset:offset + limit]
            serializer = CatPictureSerializer(cat_pictures, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    elif request.method == 'POST':
        serializer = CatPictureSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@swagger_auto_schema(
    method="PUT",
    request_body=openapi.Schema(
        type=openapi.TYPE_OBJECT,
        required=["title", "image"],
        properties={
            "title": openapi.Schema(type=openapi.TYPE_STRING, description="Updated title of the cat picture"),
            "image": openapi.Schema(type=openapi.TYPE_FILE, description="Updated image file of the cat picture"),
            "description": openapi.Schema(type=openapi.TYPE_STRING, description="Updated description of the cat picture"),
        },
    ),
    responses={200: openapi.Response("CatPictureSerializer")},
    operation_description="Update a cat picture by its ID.",
)

@api_view(['GET', 'PUT', 'DELETE'])
@permission_classes([AllowAny])#IsAuthenticatedOrReadOnly])
def cat_picture_detail(request, cat_picture_id):
    """
    Retrieve, update, or delete a cat picture by its ID.
    """
    try:
        cat_picture = CatPicture.objects.get(pk=cat_picture_id)
        image_path = os.path.join('media/', cat_picture.image.name)
    except CatPicture.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    except Exception as e:
        return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    if request.method == 'GET':
        try:
            serializer = CatPictureSerializer(cat_picture)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    elif request.method == 'PUT':
        serializer = CatPictureSerializer(cat_picture, data=request.data)
        if serializer.is_valid():
            serializer.save()
            if os.path.isfile(image_path):
                os.remove(image_path)
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        try:
            cat_picture.delete()
            if os.path.isfile(image_path):
                os.remove(image_path)
            return Response(status=status.HTTP_204_NO_CONTENT)
        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

