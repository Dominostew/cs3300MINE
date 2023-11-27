from django.test import TestCase
from django.contrib.auth.models import User
from project_app.models import User

# Create your tests here.
class CounselorModelTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='testpass')

    def test_counselor_str(self):
        self.assertEqual(str(self.counselor), 'Test Counselor')