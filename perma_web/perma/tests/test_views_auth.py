from django.conf import settings
from django.urls import reverse

from .utils import PermaTestCase


class AuthViewsTestCase(PermaTestCase):

    def test_login(self):
        """
        Test the login form
        We should get redirected to the create page
        """

        # Login through our form and make sure we get redirected to our create page
        response = self.client.post(reverse('user_management_limited_login'),
            {'username':'test_user@example.com', 'password':'pass'})
        create_url = 'login' not in response['Location']
        self.assertEqual(create_url, True)
        self.assertEqual(response.status_code, 302)
        self.assertIn('_auth_user_id', self.client.session)
        self.assertTrue(response.cookies.get(settings.CACHE_BYPASS_COOKIE_NAME).value)


    def test_deactived_user_login(self):
        response = self.submit_form('user_management_limited_login',
                          data = {'username': 'deactivated_registrar_user@example.com',
                                  'password': 'pass'},
                          success_url=reverse('user_management_account_is_deactivated'))
        self.assertFalse(response.cookies.get(settings.CACHE_BYPASS_COOKIE_NAME).value)


    def test_unactived_user_login(self):
        response = self.submit_form('user_management_limited_login',
                          data = {'username': 'unactivated_faculty_user@example.com',
                                  'password': 'pass'},
                          success_url=reverse('user_management_not_active'))
        self.assertFalse(response.cookies.get(settings.CACHE_BYPASS_COOKIE_NAME).value)

    def test_logout(self):
        """
        Test our logout link
        """

        # Login with our client and logout with our view
        self.log_in_user(user='test_user@example.com', password='pass')
        self.assertIn('_auth_user_id', self.client.session)
        self.get('logout')
        response = self.submit_form('logout')
        self.assertNotIn('_auth_user_id', self.client.session)
        self.assertFalse(response.cookies.get(settings.CACHE_BYPASS_COOKIE_NAME).value)

    def test_password_change(self):
        """
        Let's make sure we can login and change our password
        """

        self.log_in_user(user='test_user@example.com', password='pass')
        self.assertIn('_auth_user_id', self.client.session)

        self.client.post(reverse('password_change'),
            {'old_password':'pass', 'new_password1':'Changed-password1',
            'new_password2':'Changed-password1'})

        self.client.logout()

        # Try to login with our old password
        self.log_in_user(user='test_user@example.com', password='pass')
        self.assertNotIn('_auth_user_id', self.client.session)

        self.client.logout()

        # Try to login with our new password
        self.log_in_user(user='test_user@example.com', password='Changed-password1')
        self.assertIn('_auth_user_id', self.client.session)
