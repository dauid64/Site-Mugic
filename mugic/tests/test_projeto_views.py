from pydoc import resolve
from django.test import TestCase
from django.urls import reverse, resolve
from mugic import views

class ProjetoViewsTest(TestCase):
    def test_portfolio_home_views_function_is_correct(self):
        view = resolve(reverse('projetos:home'))
        self.assertTrue(view.func, views.portfolio )

    def test_projeto_home_views_function_is_correct(self):
        view = resolve(reverse('projetos:projeto', kwargs={'id': 1}))
        self.assertTrue(view.func, views.projeto )
