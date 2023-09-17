from django.test import TestCase
from django.urls import reverse

class GenerateRandomFloatsTestCase(TestCase):
    def test_empty_input(self):
        response = self.client.get(reverse('generate_random_float'), {'input_string': ''})
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, '<h2>500 Random Float Values:</h2>')

    def test_valid_input(self):
        response = self.client.get(reverse('generate_random_float'), {'input_string': 'abc123.45xyz'})
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, '<p>Processed Numeric String: 123.45</p>')
        self.assertContains(response, '<h2>500 Random Float Values:</h2>')

    def test_no_floats(self):
        response = self.client.get(reverse('generate_random_float'), {'input_string': 'no floats here'})
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, '<p>Processed Numeric String: </p>')
        self.assertContains(response, '<h2>500 Random Float Values:</h2>')
