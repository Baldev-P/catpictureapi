import os

from django.test import TestCase
from rest_framework import status
from django.urls import reverse
from django.core.files.uploadedfile import SimpleUploadedFile
from .models import CatPicture
from .serializers import CatPictureSerializer

class CatPictureAPITests(TestCase):
    def setUp(self):
        # Create a test image file for uploading
        image_file_path = 'catpictures/tests/test1.jpeg'
        # Open and read the test image file
        with open(image_file_path, 'rb') as image_file:
            image_data = image_file.read()
        self.image_file = SimpleUploadedFile("test1.jpeg", image_data, content_type="image/jpeg")
        image_file.close()

    '''def tearDown(self):
        # Clean up test files (e.g., the test image file)
        self.image_file.close()
        os.remove(os.path.join('media/cat_pics/', self.image_file.name))'''

    def test_create_cat_picture(self):
        # Define the payload for creating a new cat picture with the image file
        payload = {
            "title": "Test Cat Picture",
            "image": self.image_file,
            "description": "A test cat picture"
        }

        # Send a POST request to create a new cat picture
        response = self.client.post(reverse('create_cat_picture'), payload, format='multipart')

        # Check if the request was successful (HTTP 201 Created)
        if response.status_code != status.HTTP_201_CREATED:
            print("Error response content:", response.content)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

        # Check if the cat picture was created in the database
        self.assertEqual(CatPicture.objects.count(), 1)
        cat_picture = CatPicture.objects.first()
        self.assertEqual(cat_picture.title, payload["title"])
        self.assertEqual(cat_picture.description, payload["description"])
        os.remove(os.path.join('media/', cat_picture.image.name))

    def test_get_cat_pictures(self):
        # Create some test cat pictures
        cat_picture1 = CatPicture.objects.create(image=self.image_file, title="Cat 1", description="Description 1")
        cat_picture2 = CatPicture.objects.create(image=self.image_file, title="Cat 2", description="Description 2")

        # Send a GET request to retrieve a list of cat pictures
        response = self.client.get(reverse('get_cat_pictures'))

        # Check if the request was successful (HTTP 200 OK)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        # Check if the response contains the created cat pictures
        self.assertEqual(len(response.data), 2)
        os.remove(os.path.join('media/', cat_picture1.image.name))
        os.remove(os.path.join('media/', cat_picture2.image.name))

    def test_get_cat_picture_detail(self):
        # Create a test cat picture
        cat_picture = CatPicture.objects.create(image=self.image_file, title="Test Cat", description="Test Description")

        # Send a GET request to retrieve the detail of the created cat picture
        response = self.client.get(reverse('cat_picture_detail', args=[cat_picture.pk]))

        # Check if the request was successful (HTTP 200 OK)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        os.remove(os.path.join('media/', cat_picture.image.name))

    def test_delete_cat_picture(self):
        # Create a test cat picture
        cat_picture = CatPicture.objects.create(image=self.image_file, title="Test Cat", description="Test Description")

        # Send a DELETE request to delete the cat picture
        response = self.client.delete(reverse('cat_picture_detail', args=[cat_picture.pk]))

        # Check if the request was successful (HTTP 204 No Content)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

        # Check if the cat picture was deleted from the database
        self.assertEqual(CatPicture.objects.count(), 0)
