from django.test import TestCase
from django.urls import reverse

# Create your tests here.
class TestSnackList(TestCase):
    def test_snack_List_code(self):
        url = reverse('snack_List')
        response = self.client.get(url)
        # print(response)
        self.assertEqual(response.status_code, 200)


    def test_snack_List_page_templates(self):
        url = reverse('snack_List')
        response = self.client.get(url)
        self.assertTemplateUsed(response, 'snack_list.html')

