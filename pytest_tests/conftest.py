import pytest
from selenium import webdriver


@pytest.fixture(scope='class')
def driver(request):
    driver = webdriver.Chrome('./driver/chromedriver.exe')
    request.cls.driver = driver
    driver.maximize_window()
    yield
    driver.quit()
