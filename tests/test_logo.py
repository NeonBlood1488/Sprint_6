import allure
from pages.main_page import MainPage
from selenium.webdriver.support import expected_conditions as EC

@allure.feature('Лого')
class TestLogo:
    @allure.story('Переход на главную страницу сайта через лого Самоката')
    def test_scooter_logo_redirects_to_main(self, driver):
        main_page = MainPage(driver)
        main_page.accept_cookies()
        main_page.click_order_button_top()    # Сначала переходим на страницу заказа, чтобы потом вернуться
        from pages.order_page import OrderPage
        order_page = OrderPage(driver)
        order_page.wait.until(EC.visibility_of_element_located(order_page.NAME_FIELD))  # Ждём загрузку страницы заказа
        main_page.click_scooter_logo()    # Кликаем на лого сайта, чтобы попасть на главную
        assert driver.current_url == "https://qa-scooter.praktikum-services.ru/", "Не перешли на главную"    # Проверка того, что мы на главной

    @allure.story('Переход на Дзен через лого Яндекса')
    def test_yandex_logo_redirects_to_dzen(self, driver):
        main_page = MainPage(driver)
        main_page.accept_cookies()
        original_window = driver.current_window_handle
        main_page.click_yandex_logo()
        driver.switch_to.window(driver.window_handles[1])
        assert "dzen.ru" in driver.current_url or "yandex" in driver.current_url, "Редирект на Дзен не выполнен"    # Проверка того, что URL содержит dzen.ru (или Яндекс)
        driver.close()
        driver.switch_to.window(original_window)
