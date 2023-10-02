from django.contrib.auth.models import User
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from market.models import Lesson, Product, UserProductRelation
from market.serializer import LessonSerializer


class LessonApiTestCase(APITestCase):
    """
    Test case for /api/lessons/ api
    """
    def setUp(self):
        self.user = User.objects.create(username='test_user')
        self.user2 = User.objects.create(username='test_user2')
        self.fake_user = User.objects.create(username='fake_user')

        self.product = Product.objects.create(
            owner=self.user,
            name='Django from scratch',
        )
        self.product2 = Product.objects.create(
            owner=self.user,
            name='Python from scratch',
        )
        self.product_access = UserProductRelation.objects.create(
            user=self.user2,
            product=self.product,
            access=True,
        )
        self.product_access2 = UserProductRelation.objects.create(
            user=self.user2,
            product=self.product2,
            access=True,
        )
        self.lesson = Lesson.objects.create(
            title='Greeting!',
            video_link='http://example.com',
            duration_in_seconds=5000,
        )
        self.lesson2 = Lesson.objects.create(
            title='Python local installation',
            video_link='http://example.com',
            duration_in_seconds=3000,
        )
        self.lesson.product.set([self.product,])
        self.lesson2.product.set([self.product2,])
        
        
    def test_get_lessons(self):
        url = reverse('Lesson-list')
        self.client.force_login(self.user2)
        response = self.client.get(url)
        serializer_data = LessonSerializer([self.lesson, self.lesson2], many=True).data
        self.assertEqual(status.HTTP_200_OK, response.status_code)
        self.assertEqual(serializer_data, response.data)
        
        
    def test_get_lessons_by_fake_user(self):
        url = reverse('Lesson-list')
        self.client.force_login(self.fake_user)
        response = self.client.get(url)
        self.assertEqual(status.HTTP_200_OK, response.status_code)
        self.assertEqual([], response.data)
