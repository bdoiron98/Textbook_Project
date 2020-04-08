from django.test import TestCase

# Create your tests here.
# tweets/tests.py
from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse
from .models import Post

class PostTests(TestCase):
    def setUp(self):
        self.user = get_user_model().objects.create_user(
            username='testuser',
            email='test@email.com',
            password='specialpwd'
        )

        self.post = Post.objects.create(
            body='Cool',
            user=self.user,
        )

    def test_post_string(self):
        post = Post(body='A sample')
        self.assertEqual(str(post), post.body)

    def test_post_content(self):
        self.assertEqual(f'{self.post.user}', 'testuser')
        self.assertEqual(f'{self.post.body}', 'Cool')

    def test_post_list_view(self):
        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Cool')
        self.assertTemplateUsed(response, 'home.html')

    def test_post_create_view(self):
        response = self.client.post(reverse('post_new'), {
            'body': 'New post',
            'user': self.user,
        })
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'New post')
