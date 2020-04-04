from selenium import webdriver
from tests.data.config import settings
from urllib.parse import urljoin

class WebApp:
    instance = None

    @classmethod
    def get_instance(cls):
        if cls.instance is None:
            cls.instance = WebApp()
        return cls.instance

    def __init__(self):
        if str(settings['browser']) is "firefox":
            self.driver = webdriver.Firefox(executable_path='tests/drivers/geckodriver')
        elif str(settings['browser']) is "chrome":
            self.driver = webdriver.Chrome(executable_path='tests/drivers/chromedriver')
        else:
            self.driver = webdriver.Chrome(executable_path='tests/drivers/chromedriver')
            self.driver.maximize_window()

    def get_driver(self):
        return self.driver

    def load_website(self):
        self.driver.get(settings['url'])

webapp = WebApp.get_instance()
