from django.test import TestCase
from django.urls import reverse
from .models import Post

# Create your tests here.
class HomepageTests(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.post = Post.objects.create(text="Test data")

    def test_model_content(self):
        self.assertEqual(self.post.text, "Test data")

    def test_url_exists_at_correct_location(self):
        response = self.client.get("/")
        self.assertEqual(response.status_code, 200)

    def test_homepage(self):
        response = self.client.get(reverse("home"))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "home.html")
        self.assertContains(response, "Test data")