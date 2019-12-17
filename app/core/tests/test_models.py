from django.test import TestCase
from django.contrib.auth import get_user_model

class ModelTests(TestCase):

    def test_create_user_with_email_successful(self):
        """Test creating a new user with an email is successful"""
        email = "izhan@gmail.com"
        password = "12345"
        user = get_user_model().objects.create_user(
        email = email,
        password = password
        )
        self.assertEqual(user.email, email)
        self.assertTrue(user.check_password(password))

    def test_new_user_email_nomalized(self):
        """Test that email for a new user is nomalized"""
        email = "izhan@GMAIL.COM"
        user= get_user_model().objects.create_user(email, '12345')
        self.assertEqual(user.email, email.lower())

    def test_new_user_invalid_email(self):
        """Test creating user with no email raise error"""
        with self.assertRaises(ValueError):
            get_user_model().objects.create_user(None, "12345")

    def test_create_new_super_user(self):
        """Test creating new super user"""
        user = get_user_model().objects.create_superuser(
        'izhan@gmail.com',
        '12345'
        )
        self.assertTrue(user.is_superuser)
        self.assertTrue(user.is_staff)
