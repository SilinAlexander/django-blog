from django.test import TestCase
from rest_framework.reverse import reverse_lazy
from rest_framework.test import APITestCase
from rest_framework import status


class BlogTest(APITestCase):

    def test_article_detail(self):
        url = reverse_lazy('blog:post-detail', kwargs={'slug': 'крутая'})
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK, response.data)

    def test_article_list(self):
        url = reverse_lazy('blog:post-list', kwargs={'slug': 'крутая'})
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK, response.data)


