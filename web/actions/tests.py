from django.contrib.auth import get_user_model
from django.test import TestCase
from rest_framework.reverse import reverse_lazy
from rest_framework.test import APITestCase
from blog.models import Article, Category
from blog.choices import ArticleStatus
from rest_framework import status
from .choices import LikeStatus, LikeObjects, LikeIconStatus


User = get_user_model()


class LikeTest(APITestCase):

    def setUp(self):
        category = Category.objects.create(name='test')
        self.article = Article.objects.create(
            category=category, title='testarticle', content='testtest', status=ArticleStatus.ACTIVE)
        user1 = User.objects.create_user(email='abctest@mail.com', password='abcdef123456')
        user1.emailaddress_set.create(email=user1.email, verified=True, primary=True)
        user2 = User.objects.create_user(email='abctest2@mail.com', password='abcdefg123456')
        user2.emailaddress_set.create(email=user2.email, verified=True, primary=True)
        self.login_url = reverse_lazy('auth_app:api_login')
        data = {'email': 'abctest@mail.com', 'password': 'abcdef123456'}
        response = self.client.post(path=self.login_url, data=data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_like_create(self):
        url = reverse_lazy('actions:like_dislike')
        data = {'vote': LikeStatus.LIKE, 'model': LikeObjects.ARTICLE, 'object_id': self.article.id}
        response = self.client.post(path=url, data=data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['like_count'], 1)
        self.assertEqual(response.data['dislike_count'], 0)
        self.assertEqual(response.data['status'], LikeIconStatus.LIKED)
        self.assertEqual(self.article.likes, 1)
        self.client.logout()
        data = {'email': 'abctest2@mail.com', 'password': 'abcdefg123456'}
        response = self.client.post(path=self.login_url, data=data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        data = {'vote': LikeStatus.LIKE, 'model': LikeObjects.ARTICLE, 'object_id': self.article.id}
        response = self.client.post(path=url, data=data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(self.article.likes, 2)
        data = {'vote': LikeStatus.DISLIKE, 'model': LikeObjects.ARTICLE, 'object_id': self.article.id}
        response = self.client.post(path=url, data=data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(self.article.likes, 1)
        self.assertEqual(self.article.dislikes, 1)
        self.assertEqual(response.data['like_count'], 1)
        self.assertEqual(response.data['dislike_count'], 1)
        self.assertEqual(response.data['status'], LikeIconStatus.DISLIKED)
        data = {'vote': LikeStatus.DISLIKE, 'model': LikeObjects.ARTICLE, 'object_id': self.article.id}
        response = self.client.post(path=url, data=data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(self.article.likes, 1)
        self.assertEqual(self.article.dislikes, 0)
        self.assertEqual(response.data['like_count'], 1)
        self.assertEqual(response.data['dislike_count'], 0)
        self.assertEqual(response.data['status'], LikeIconStatus.CANCELED)

    def test_unauthorized(self):
        self.client.logout()
        url = reverse_lazy('actions:like_dislike')
        data = {'vote': LikeStatus.DISLIKE, 'model': LikeObjects.ARTICLE, 'object_id': self.article.id}
        response = self.client.post(path=url, data=data)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)


class FollowTest(APITestCase):

    def setUp(self):
        user1 = User.objects.create_user(email='abctest@mail.com', password='abcdef123456')
        user1.emailaddress_set.create(email=user1.email, verified=True, primary=True)
        user2 = User.objects.create_user(email='abctest2@mail.com', password='abcdefg123456')
        user2.emailaddress_set.create(email=user2.email, verified=True, primary=True)

        pass

    def test_like_create(self):


