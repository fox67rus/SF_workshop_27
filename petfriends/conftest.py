import time
from datetime import datetime

import pytest

from selenium import webdriver as selenium_wd
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

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


@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    rep = outcome.get_result()
    setattr(item, 'rep_' + rep.when, rep)


@pytest.fixture(scope='function', autouse=True)
def test_failed_check(request):
    yield
    if request.node.rep_setup.failed:
        print('test is failed', request.node.nodeid)
    elif request.node.rep_setup.passed:
        if request.node.rep_call.failed:
            driver = request.node.funcargs["selenium_driver"]
            take_screenshot(driver, request.node.nodeid)
            print('executing is fail', request.node.nodeid)


def take_screenshot(driver, nodeid):
    time.sleep(1)
    file_name = f'{nodeid}_{datetime.today().strftime("%Y-%m-%d_%H%M%S")}.png'.replace('/', '_').replace('::', '__')
    driver.save_screenshot(file_name)
