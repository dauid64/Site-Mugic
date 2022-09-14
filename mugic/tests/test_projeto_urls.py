from django.test import TestCase
from django.urls import reverse

class ProjetoURLsTest(TestCase):
    
    def test_projeto_home_url_is_correct(self):
        home_url = reverse('projetos:home')
        self.assertEqual(home_url, '/')

    def test_projeto_url_is_correct(self):
        home_url = reverse('projetos:projeto', kwargs={'id': 1})
        self.assertEqual(home_url, '/project/1')