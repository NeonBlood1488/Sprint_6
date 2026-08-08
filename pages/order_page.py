import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from pages.base_page import BasePage
from locators import OrderPageLocators

class OrderPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    @allure.step("Заполнение первой формы заказа")
    def fill_first_form(self, name, surname, address, metro, phone):
        self.find(OrderPageLocators.NAME_FIELD).send_keys(name)
        self.find(OrderPageLocators.SURNAME_FIELD).send_keys(surname)
        self.find(OrderPageLocators.ADDRESS_FIELD).send_keys(address)

        metro_input = self.find(OrderPageLocators.METRO_FIELD)
        metro_input.send_keys(metro)
        station_locator = (By.XPATH, f"//div[text()='{metro}']")
        self.click(station_locator)

        self.find(OrderPageLocators.PHONE_FIELD).send_keys(phone)
        self.click(OrderPageLocators.NEXT_BUTTON)  # Переход ко второй части формы

    @allure.step("Заполнение второй формы заказа и подтверждение")
    def fill_second_form(self, date, rental_period, color, comment):
        # Ввод даты
        date_input = self.find(OrderPageLocators.DATE_FIELD)
        date_input.send_keys(date)
        date_input.send_keys(Keys.ENTER)

        # Выбор срока аренды
        self.click(OrderPageLocators.RENTAL_PERIOD_DROPDOWN)
        option_locator = (By.XPATH, f"//div[@class='Dropdown-option' and text()='{rental_period}']")
        self.click(option_locator)

        # Выбор цвета
        color_id = "black" if color == "чёрный жемчуг" else "grey"
        color_locator = (By.XPATH, f"//label[@for='{color_id}']")
        self.scroll_and_click(color_locator)

        # Комм
        self.find(OrderPageLocators.COMMENT_FIELD).send_keys(comment)

        self.scroll_and_click(OrderPageLocators.ORDER_BUTTON)   # Клик по кнопке "Заказать" с прокруточкой

        self.wait_for_visibility(OrderPageLocators.CONFIRM_MODAL)
        self.click(OrderPageLocators.CONFIRM_YES)    # Подтверждение заказа
        self.wait_for_visibility(OrderPageLocators.SUCCESS_MESSAGE)

    @allure.step("Получение сообщения об успешном заказе")
    def get_success_message(self):
        return self.get_text(OrderPageLocators.SUCCESS_MESSAGE)
