from django.test import TestCase
from posts.templatetags.first_before import first_before

# Create your tests here.
class PostsTest(TestCase):
    def test_filter_first_before(self):
        self.assertEqual(first_before("1 month, 2 hours", ','), '1 month')
