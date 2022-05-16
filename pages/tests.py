from django.test import TestCase, SimpleTestCase
from django.urls import reverse
from django.contrib.auth import get_user_model, models


# Create your tests here.
class HomePageTests(SimpleTestCase):

    def test_home_test_status_code(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)

    def test_view_url_by_name(self):
        response = self.client.get(reverse('pages:home'))
        self.assertEqual(response.status_code, 200)

    def test_view_uses_correct_template(self):
        response = self.client.get(reverse('pages:home'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'home.html')


class SignupPageTest(TestCase):

    username = 'newuser'
    email = 'newuser@email.com'

    def test_signup_ststus_page(self):
        response = self.client.get('/accounts/signup/')
        self.assertEqual(response.status_code, 200)

    def test_view_url_by_name(self):
        response = self.client.get(reverse('accounts:signup'))
        self.assertEqual(response.status_code, 200)

    def test_view_users_correct_template(self):
        response = self.client.get(reverse('accounts:signup'))
        self.assertTemplateUsed(response, 'registration/signup.html')
        self.assertEqual(response.status_code, 200)

    def test_signup_form(self):
        new_user = get_user_model().objects.create_user(
            self.username, self.email)
        users = get_user_model().objects.all()
        self.assertEqual(users.count(), 1)
        self.assertEqual(users[0].username, new_user.username)
        self.assertEqual(users[0].email, new_user.email)
