import pytest
from selenium import webdriver

@pytest.fixture(scope="function")
def driver():
    browser = webdriver.Firefox()
    browser.maximize_window()
    browser.get("https://qa-scooter.praktikum-services.ru/")
    yield browser
    browser.quit()
