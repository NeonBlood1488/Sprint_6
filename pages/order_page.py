from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from pages.base_page import BasePage

class OrderPage(BasePage):
    # Локаторы
    NAME_FIELD = (By.XPATH, "//input[@placeholder='* Имя']")
    SURNAME_FIELD = (By.XPATH, "//input[@placeholder='* Фамилия']")
    ADDRESS_FIELD = (By.XPATH, "//input[@placeholder='* Адрес: куда привезти заказ']")
    METRO_FIELD = (By.XPATH, "//input[@placeholder='* Станция метро']")
    PHONE_FIELD = (By.XPATH, "//input[@placeholder='* Телефон: на него позвонит курьер']")
    NEXT_BUTTON = (By.XPATH, "//button[text()='Далее']")

    DATE_FIELD = (By.XPATH, "//input[@placeholder='* Когда привезти самокат']")
    RENTAL_PERIOD_DROPDOWN = (By.CLASS_NAME, "Dropdown-placeholder")
    RENTAL_OPTION = (By.XPATH, "//div[@class='Dropdown-option' and text()='{}']")
    COLOR_CHECKBOX = (By.XPATH, "//label[@for='{}']")
    COMMENT_FIELD = (By.XPATH, "//input[@placeholder='Комментарий для курьера']")

    ORDER_BUTTON = (By.XPATH, "//button[@class='Button_Button__ra12g Button_Middle__1CSJM' and text()='Заказать']")
    CONFIRM_MODAL = (By.XPATH, "//*[contains(., 'Хотите оформить заказ?')]")
    CONFIRM_YES = (By.XPATH, "//button[normalize-space()='Да']")
    SUCCESS_MESSAGE = (By.XPATH, "//*[contains(., 'Заказ оформлен')]")

    def __init__(self, driver):
        super().__init__(driver)

    def fill_first_form(self, name, surname, address, metro, phone):
        self.click(self.NAME_FIELD)
        self.find(self.NAME_FIELD).send_keys(name)
        self.find(self.SURNAME_FIELD).send_keys(surname)
        self.find(self.ADDRESS_FIELD).send_keys(address)

        metro_input = self.find(self.METRO_FIELD)
        metro_input.send_keys(metro)
        station_locator = (By.XPATH, f"//div[text()='{metro}']")
        self.click(station_locator)  # Клик по выпадающему списку варианты станции

        self.find(self.PHONE_FIELD).send_keys(phone)
        self.click(self.NEXT_BUTTON)

    def fill_second_form(self, date, rental_period, color, comment):
        date_input = self.find(self.DATE_FIELD)
        date_input.send_keys(date)
        date_input.send_keys(Keys.ENTER)

        self.click(self.RENTAL_PERIOD_DROPDOWN)          # Выбор срока аренды
        option_locator = (By.XPATH, f"//div[@class='Dropdown-option' and text()='{rental_period}']")
        self.click(option_locator)

        # Выбор цвета через JS (на всякий)
        color_id = "black" if color == "чёрный жемчуг" else "grey"
        color_locator = (By.XPATH, f"//label[@for='{color_id}']")
        self.scroll_and_click(color_locator)

        self.find(self.COMMENT_FIELD).send_keys(comment)          # Комм

        self.scroll_and_click(self.ORDER_BUTTON)                  # Нажимаем на кнопку "Заказать" с прокруткой

        # Подтверждение заказа
        self.wait_for_visibility(self.CONFIRM_MODAL)
        self.click(self.CONFIRM_YES)
        self.wait_for_visibility(self.SUCCESS_MESSAGE)

    def get_success_message(self):
        return self.get_text(self.SUCCESS_MESSAGE)
#67