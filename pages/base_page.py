### Добавил общий базовый класс, от которого наследуются методы других страниц
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def wait_for_visibility(self, locator, timeout=10):
        return WebDriverWait(self.driver, timeout).until(EC.visibility_of_element_located(locator))

    def wait_for_clickable(self, locator, timeout=10):
        return WebDriverWait(self.driver, timeout).until(EC.element_to_be_clickable(locator))

    def click(self, locator, timeout=10):
        self.wait_for_clickable(locator, timeout).click()

    def scroll_and_click(self, locator, timeout=10):
        element = self.wait_for_visibility(locator, timeout)
        self.driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", element)
        self.driver.execute_script("arguments[0].click();", element)

    def get_text(self, locator, timeout=10):
        return self.wait_for_visibility(locator, timeout).text

    def find(self, locator):
        return self.driver.find_element(*locator)

    def get_current_url(self):
        return self.driver.current_url
