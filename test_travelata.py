from time import sleep

from selenium import webdriver as selenium_wd
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

s = Service(r"C:\webdrivers\chromedriver.exe")
chrome_options = Options()

driver = selenium_wd.Chrome(service=s, options=chrome_options)
driver.get('https://travelata.ru/')

marketing_banner_locator = (By.XPATH, "//div[@class='btn btnOrange btnFlat js-popup-close']")
market_banner = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located(marketing_banner_locator)
)
market_banner.click()

destination_locator = (By.NAME, "destination")
destination = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located(destination_locator)
)
destination.clear()
destination.send_keys('Самара')
sleep(2)

start_search_locator = (By.ID, "startSearch")
start_search = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located(start_search_locator)
)
start_search.click()

sleep(10)
driver.quit()
