import allure
from pages.main_page import MainPage
from pages.order_page import OrderPage
from locators import OrderPageLocators
from config import BASE_URL, DZEN_PATTERNS

@allure.feature('Лого')
class TestLogo:
    @allure.title("Переход на главную через лого Самоката")
    @allure.story('Переход на главную через лого Самоката')
    def test_scooter_logo_redirects_to_main(self, driver):
        main_page = MainPage(driver)
        main_page.accept_cookies()
        main_page.click_order_button_top()  # Переход на страницу заказа
        order_page = OrderPage(driver)
        order_page.wait_for_visibility(OrderPageLocators.NAME_FIELD)   # Ждем загрузку страницы заказа
        main_page.click_scooter_logo()  # Клик по лого Самоката
        assert main_page.get_current_url() == BASE_URL, "Не перешли на главную"   # Проверка того, что вернулись на главную

    @allure.title("Переход на Дзен через лого Яндекса")
    @allure.story('Переход на Дзен через лого Яндекса')
    def test_yandex_logo_redirects_to_dzen(self, driver):
        main_page = MainPage(driver)
        main_page.accept_cookies()
        main_page.click_yandex_logo()  # Клик по лого Яндекса

        main_page.wait_for_window_count(2)   # Ожидаем появления второго окна
        main_page.switch_to_new_window()     # И переключаемся на него
        main_page.wait_for_url_not_blank()   # Ожидаем, что URL перестанет быть "about:blank"

        assert any(pattern in main_page.get_current_url() for pattern in DZEN_PATTERNS), "Редирект на Дзен не выполнен"  # Проверяем, что текущий URL содержит один из ожидаемых паттернов
