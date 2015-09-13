# coding: utf-8
from stores.models import Village, StoresTxt
from selenium.webdriver import Firefox


class WebDriver(object):
    def __init__(self, name):
        self.webdriver = Firefox()
        self.name = name

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
        total_pages = self.get_total_stores()
        total = int(total_pages)
        for i in xrange(total):
            self.webdriver.find_element_by_class_name('maisConteudo').click()

    def create_stores(self):
        village = self.get_village(self.name)
        stores = self.webdriver.find_element_by_class_name('col2-1')
        StoresTxt.objects.create(village=village, content=stores)

    def run(self):
        if self.name:
            village = self.get_village(self.name)
            self.enter_site(village.url)
            self.move_down_page()
            self.create_stores()

    def tearDown(self):
        self.webdriver.quit()
