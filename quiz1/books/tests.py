from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from .models import Book


class BookApiTests(APITestCase):
    def test_create_and_list_books(self):
        response = self.client.post(
            reverse("book-list"),
            {
                "title": "Clean Code",
                "author": "Robert C. Martin",
                "rating": 4.5,
                "is_featured": True,
            },
            format="json",
        )

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Book.objects.count(), 1)

        response = self.client.get(reverse("book-list"))

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]["title"], "Clean Code")

    def test_retrieve_and_delete_book(self):
        book = Book.objects.create(
            title="Django for APIs",
            author="William S. Vincent",
            rating=4.7,
        )

        response = self.client.get(reverse("book-detail", args=[book.pk]))

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["author"], "William S. Vincent")

        response = self.client.delete(reverse("book-detail", args=[book.pk]))

        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertFalse(Book.objects.filter(pk=book.pk).exists())
