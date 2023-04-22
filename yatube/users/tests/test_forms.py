from django.test import Client, TestCase
from django.urls import reverse

from posts.forms import CreationForm
from posts.models import User


class UserCreateFormTests(TestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.user = User.objects.create_user(username='auth')
        cls.form = CreationForm()

    def setUp(self):
        self.guest_client = Client()

    def test_user_create(self):
        users_count = User.objects.count()
        form_data = {
            'first_name': 'Имя',
            'last_name': 'Фамилия',
            'username': 'auth',
            'email': 'Электронная почта',
            'password': 'Пароль',
            'password2': 'Пароль2'
        }
        response = self.guest_client.post(
            reverse('users:signup'),
            data=form_data,
            follow=True
        )
        new_user = User.objects.latest('id')
        self.assertEqual(new_user.username, form_data['username'])
        self.assertRedirects(response, reverse('posts:index'))
        self.assertEqual(User.objects.count(), users_count+1)