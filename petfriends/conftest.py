import pytest

from selenium import webdriver as selenium_wd
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

BASE_URL = 'https://petfriends.skillfactory.ru/'
USER = '123@a.ru'
PASSWORD = '123@a.ru'


@pytest.fixture(scope='session')
def selenium_driver(request):
    s = Service(r"C:\webdrivers\chromedriver.exe")
    chrome_options = Options()
    driver = selenium_wd.Chrome(service=s, options=chrome_options)
    driver.maximize_window()
    driver.implicitly_wait(5)

    driver.get(BASE_URL + '/login')
    driver.find_element(By.ID, 'email').send_keys(USER)
    driver.find_element(By.ID, 'pass').send_keys(PASSWORD)
    driver.find_element(By.CSS_SELECTOR, 'button[type="submit"]').click()

    yield driver

    driver.quit()
