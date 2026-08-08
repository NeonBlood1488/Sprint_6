import allure
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    @allure.step("Ожидание видимости элемента")
    def wait_for_visibility(self, locator, timeout=10):
        return WebDriverWait(self.driver, timeout).until(EC.visibility_of_element_located(locator))

    @allure.step("Ожидание кликабельности элемента")
    def wait_for_clickable(self, locator, timeout=10):
        return WebDriverWait(self.driver, timeout).until(EC.element_to_be_clickable(locator))

    @allure.step("Клик по элементу")
    def click(self, locator, timeout=10):
        self.wait_for_clickable(locator, timeout).click()

    @allure.step("Прокрутка к элементу и клик")
    def scroll_and_click(self, locator, timeout=10):
        element = self.wait_for_visibility(locator, timeout)
        self.driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", element)
        self.driver.execute_script("arguments[0].click();", element)

    @allure.step("Получение текста элемента")
    def get_text(self, locator, timeout=10):
        return self.wait_for_visibility(locator, timeout).text

    @allure.step("Поиск элемента")
    def find(self, locator):
        return self.driver.find_element(*locator)

    @allure.step("Получение текущего URL")
    def get_current_url(self):
        return self.driver.current_url

    @allure.step("Получение списка окон")
    def get_window_handles(self):
        return self.driver.window_handles

    @allure.step("Переключение на окно по handle")
    def switch_to_window(self, handle):
        self.driver.switch_to.window(handle)

    @allure.step("Ожидание количества окон")
    def wait_for_window_count(self, count, timeout=10):
        WebDriverWait(self.driver, timeout).until(lambda d: len(d.window_handles) == count)

    @allure.step("Переключение на последнее открытое окно")
    def switch_to_new_window(self):
        handles = self.get_window_handles()
        if len(handles) > 1:
            self.switch_to_window(handles[-1])
        else:
            raise Exception("Нет нового окна")

    @allure.step("Ожидание, что URL не равен about:blank")
    def wait_for_url_not_blank(self, timeout=10):
        WebDriverWait(self.driver, timeout).until(lambda d: d.current_url != "about:blank")
