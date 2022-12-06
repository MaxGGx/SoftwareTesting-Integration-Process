from django.test import LiveServerTestCase
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By

class BaseTestCase(LiveServerTestCase):

    @classmethod
    def setUpClass(cls):
        cls.driver = WebDriver()
        super(BaseTestCase, cls).setUpClass()

    @classmethod
    def tearDownClass(cls):
        super(BaseTestCase, cls).tearDownClass()
        cls.driver.quit()


    def AgregarReceta_Test1(self):
        self.driver.get(self.live_server_url)
        poll = self.driver.find_element(By.ID,'explanation')
        assert poll == "Ver recetas"
        
        