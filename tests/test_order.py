import allure
import pytest
from pages.main_page import MainPage
from pages.order_page import OrderPage
from data import ORDER_DATA

@allure.feature('Заказ самоката')
class TestOrder:
    @allure.story('Позитивный сценарий оформления заказа')
    @pytest.mark.parametrize("order", ORDER_DATA, ids=["top_button", "bottom_button"])
    def test_successful_order(self, driver, order):
        main_page = MainPage(driver)
        main_page.accept_cookies()

        if order["button_location"] == "top":    # Выбор кнопки заказа в зависимости от данных
            main_page.click_order_button_top()
        else:
            main_page.click_order_button_bottom()

        order_page = OrderPage(driver)           # Заполнение формы заказа
        order_page.fill_first_form(
            name=order["name"],
            surname=order["surname"],
            address=order["address"],
            metro=order["metro"],
            phone=order["phone"]
        )
        order_page.fill_second_form(
            date=order["date"],
            rental_period=order["rental_period"],
            color=order["color"],
            comment=order["comment"]
        )
        success_text = order_page.get_success_message()    # Проверка появления сообщения об успешном оформлении заказа
        assert "Заказ оформлен" in success_text, "Сообщение об успешном заказе не появилось"
