from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys

class OrderPage:
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
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def fill_first_form(self, name, surname, address, metro, phone):
        self.wait.until(EC.element_to_be_clickable(self.NAME_FIELD)).send_keys(name)
        self.driver.find_element(*self.SURNAME_FIELD).send_keys(surname)
        self.driver.find_element(*self.ADDRESS_FIELD).send_keys(address)
        metro_input = self.driver.find_element(*self.METRO_FIELD)
        metro_input.send_keys(metro)
        self.wait.until(EC.element_to_be_clickable((By.XPATH, f"//div[text()='{metro}']"))).click()
        self.driver.find_element(*self.PHONE_FIELD).send_keys(phone)
        self.driver.find_element(*self.NEXT_BUTTON).click()

    def fill_second_form(self, date, rental_period, color, comment):
        date_input = self.driver.find_element(*self.DATE_FIELD)
        date_input.send_keys(date)
        date_input.send_keys(Keys.ENTER)

        self.driver.find_element(*self.RENTAL_PERIOD_DROPDOWN).click()
        self.wait.until(EC.element_to_be_clickable(
            (self.RENTAL_OPTION[0], self.RENTAL_OPTION[1].format(rental_period))
        )).click()

        color_id = "black" if color == "чёрный жемчуг" else "grey"
        color_checkbox = self.driver.find_element(
            self.COLOR_CHECKBOX[0], self.COLOR_CHECKBOX[1].format(color_id)
        )
        self.driver.execute_script("arguments[0].click();", color_checkbox)

        self.driver.find_element(*self.COMMENT_FIELD).send_keys(comment)

        # Находим кнопку, прокручиваем и кликаем через JS
        order_button = self.driver.find_element(*self.ORDER_BUTTON)
        self.driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", order_button)
        self.driver.execute_script("arguments[0].click();", order_button)

        self.wait.until(EC.visibility_of_element_located(self.CONFIRM_MODAL))    # Ждем всплывающее окно с подтверждением заказа
        self.wait.until(EC.element_to_be_clickable(self.CONFIRM_YES)).click()    # Клик на кнопку "Да"
        self.wait.until(EC.visibility_of_element_located(self.SUCCESS_MESSAGE))  # Ждем сообщение об успехе

    def get_success_message(self):
        return self.wait.until(EC.visibility_of_element_located(self.SUCCESS_MESSAGE)).text
