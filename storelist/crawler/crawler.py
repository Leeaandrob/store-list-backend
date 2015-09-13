# coding: utf-8
from stores.models import Village
from selenium.webdriver import Firefox


class WebDriver(object):
    def __init__(self):
        self.webdriver = Firefox()

    def get_village(self, name):
        village = Village.objects.get(name=name)
        return village

    def enter_site(self, url):
        self.webdriver.get(url)
        return self.webdriver.current_url

    def get_total_stores(self):
        result = self.webdriver.find_element_by_class_name('total')
        return result.text

    def move_down_page(self):
        self.webdriver.find_element_by_class_name('maisConteudo')

    def tearDown(self):
        self.webdriver.quit()
