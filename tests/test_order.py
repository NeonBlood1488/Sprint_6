import allure
from pages.main_page import MainPage
from pages.order_page import OrderPage
from data import ORDER_DATA

@allure.feature('Заказ самоката')
class TestOrder:
    def _fill_order_form(self, driver, order_data):    # Этот метод заполняет форму и возвращает текст успеха
        order_page = OrderPage(driver)
        order_page.fill_first_form(
            name=order_data["name"],
            surname=order_data["surname"],
            address=order_data["address"],
            metro=order_data["metro"],
            phone=order_data["phone"])
        order_page.fill_second_form(
            date=order_data["date"],
            rental_period=order_data["rental_period"],
            color=order_data["color"],
            comment=order_data["comment"])
        return order_page.get_success_message()

    @allure.title("Оформление заказа через верхнюю кнопку")
    @allure.story('Позитивный сценарий оформления заказа через верхнюю кнопку')
    def test_successful_order_top_button(self, driver):
        main_page = MainPage(driver)
        main_page.accept_cookies()
        main_page.click_order_button_top()  # Заказ через верхнюю кнопку
        success_text = self._fill_order_form(driver, ORDER_DATA[0])
        assert "Заказ оформлен" in success_text, "Сообщение об успешном заказе не появилось"

    @allure.title("Оформление заказа через нижнюю кнопку")
    @allure.story('Позитивный сценарий оформления заказа через нижнюю кнопку')
    def test_successful_order_bottom_button(self, driver):
        main_page = MainPage(driver)
        main_page.accept_cookies()
        main_page.click_order_button_bottom()  # Заказ через нижнюю кнопку
        success_text = self._fill_order_form(driver, ORDER_DATA[1])
        assert "Заказ оформлен" in success_text, "Сообщение об успешном заказе не появилось"
