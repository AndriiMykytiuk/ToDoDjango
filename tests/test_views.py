from django.test import TestCase, Client
from django.contrib.auth.models import User
from django.urls import reverse
import json


class HomeViewTestCase(TestCase):

    def setUp(self):
        self.username = 'myuser'
        self.password = 'valid_password'
        self.client = Client()
        self.url = reverse('home')

        User.objects.create_superuser(self.username, 'email@test.com', self.password)

    def test_home_view_redirects_unauthenticated_user_to_login(self):
        response = self.client.get(self.url)
        self.assertRedirects(response, reverse('login'))

    def test_home_view_redirects_authenticated_users_to_list(self):
        self.client.login(username = self.username, password = self.password)
        response = self.client.get(self.url)
        self.assertRedirects(response, reverse('tasks'))


class RegisterViewTest(TestCase):

    def setUp(self):
        self.client = Client()
        self.username = 'myuser'
        self.url = reverse('register')
        self.data = {
            'password1': 'valid_password',
            'password2': 'valid_password',
            'email': 'email@test.com',
            'username': self.username
        }
        self.bad_data = self.data.copy()
        self.bad_data.update({'password2': 'badpassword'})
        self.register_button = '<button class="btn btn-success btn-center btn-fullwidth" type="submit">Register</button>'

    def test_register_with_correct_data(self):
        self.client.post(self.url, self.data)
        self.assertEqual(User.objects.count(), 1)
        self.assertEqual(User.objects.first().username, self.username)

    def test_register_redirects_after_registration(self):
        response = self.client.post(self.url, self.data, follow=True)
        self.assertRedirects(response, reverse('tasks'))

    def test_register_returns_form_for_get(self):
        response = self.client.get(self.url)
        self.assertTemplateUsed('register.html')
        self.assertInHTML(
            self.register_button,
            response.content.decode('utf8')
        )

    def test_register_returns_form_for_invalid(self):
        response = self.client.post(self.url, self.bad_data)
        self.assertInHTML(
            self.register_button,
            response.content.decode('utf8')
        )

    def test_register_returns_form_error_for_invalid(self):
        response = self.client.post(self.url, self.bad_data)
        self.assertInHTML(
            '<li>The two password fields didn&#39;t match.</li>',
            response.content.decode('utf8')
        )





