from django.test import TestCase
from rest_framework.reverse import reverse_lazy
from rest_framework.test import APITestCase
from rest_framework import status
from .models import Article


class BlogTest(APITestCase):

    @classmethod
    def setUpTestData(cls):
        a = Article.objects.create(title='title', content='крутая, крутая', category=None, author=None )
        print(a.slug)

    def test_article_detail(self):
        print(Article.objects.all()[0].slug)
        url = reverse_lazy('blog:post-detail', kwargs={'slug': 'title'})
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK, response.data)

    def test_article_list(self):
        url = reverse_lazy('blog:post-list',)
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK, response.data)
        print(response.data)
