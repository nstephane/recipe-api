from django.test import TestCase
from django.contrib.auth import get_user_model


class ModelTests(TestCase):

    def test_create_user_with_email_successful(self):
        """ It creates a user successfully with an email """
        email = 'west@email.com'
        password = 'test123!@#'
        user = get_user_model().objects.create_user(
            email=email,
            password=password
        )

        self.assertEqual(user.email, email)
        self.assertTrue(user.check_password(password))

    def test_new_user_email_normalization(self):
        """ It ensures users email are normalized """
        email = "just@MAIL.COM"
        user = get_user_model().objects.create_user(email, '1234')

        self.assertEqual(user.email, email.lower())

    def test_user_email_validation(self):
        """ Validates new user email by raising an error """
        with self.assertRaises(ValueError):
            get_user_model().objects.create_user(None, '1234test')

    def test_super_user_creation(self):
        """ A super user can be created """
        user = get_user_model().objects.create_superuser(
          'admin@email.com',
          '!@#$%6'
        )

        self.assertTrue(user.is_superuser)
        self.assertTrue(user.is_staff)
