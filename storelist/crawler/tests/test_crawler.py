# coding: utf-8
from django.test import TestCase

from crawler.crawler import WebDriver
from stores.models import Village

from selenium.webdriver import Firefox
from mock import patch
from model_mommy import mommy


class WebDriverTest(TestCase):

    def setUp(self):
        self.manager = WebDriver()
        self.village = mommy.make(Village,
                                  name='Barra-Shopping',
                                  url='http://www.barrashopping.com.br/lojas')

    def test_instance(self):
        self.assertTrue(isinstance(self.manager.webdriver, Firefox))

    def test_get_village(self):
        resposta = self.manager.get_village('Barra-Shopping')
        esperado = self.village
        self.assertEqual(resposta, esperado)

    def test_enter_site(self):
        resposta = self.manager.enter_site(self.village.url)
        esperado = 'http://www.barrashopping.com.br/lojas'
        self.assertEqual(resposta, esperado)

    @patch('crawler.crawler.Webdriver')
    def test_get_total_stores(self, _driver):
        self.manager.get_total_stores()
        _driver.find_element_by_class_name.assert_called_once_with()

    @patch('crawler.crawler.WebDriver')
    def move_down_page(self, _webdriver):
        self.manager.move_down_page()
        _webdriver.find_element_by_class_name.assert_called_once_with()
#        self.manager.find_element_by_class_name('maisConteudo')

    def tearDown(self):
        self.manager.tearDown()
