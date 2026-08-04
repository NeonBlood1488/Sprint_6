import allure
from pages.main_page import MainPage
from pages.order_page import OrderPage
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

@allure.feature('Лого')
class TestLogo:
    @allure.story('Переход на главную страницу сайта через лого Самоката')
    def test_scooter_logo_redirects_to_main(self, driver):
        main_page = MainPage(driver)
        main_page.accept_cookies()
        main_page.click_order_button_top()
        order_page = OrderPage(driver)
        order_page.wait.until(EC.visibility_of_element_located(order_page.NAME_FIELD))
        main_page.click_scooter_logo()
        assert driver.current_url == "https://qa-scooter.praktikum-services.ru/", "Не перешли на главную"

    @allure.story('Переход на Дзен через лого Яндекса')
    def test_yandex_logo_redirects_to_dzen(self, driver):
        main_page = MainPage(driver)
        main_page.accept_cookies()
        main_page.click_yandex_logo()
        wait = WebDriverWait(driver, 10)
        wait.until(lambda d: len(d.window_handles) > 1)
        driver.switch_to.window(driver.window_handles[1])
        wait.until(lambda d: d.current_url != "about:blank")
        assert "dzen.ru" in driver.current_url or "yandex" in driver.current_url, "Редирект на Дзен не выполнен"
