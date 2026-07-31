from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys
import time

class OrderPage:
    NAME_FIELD = (By.XPATH, "//input[@placeholder='* Имя']")                           # Первая форма (кому, куда и т.п.)
    SURNAME_FIELD = (By.XPATH, "//input[@placeholder='* Фамилия']")
    ADDRESS_FIELD = (By.XPATH, "//input[@placeholder='* Адрес: куда привезти заказ']")
    METRO_FIELD = (By.XPATH, "//input[@placeholder='* Станция метро']")
    PHONE_FIELD = (By.XPATH, "//input[@placeholder='* Телефон: на него позвонит курьер']")
    NEXT_BUTTON = (By.XPATH, "//button[text()='Далее']")


    DATE_FIELD = (By.XPATH, "//input[@placeholder='* Когда привезти самокат']")       # Вторая форма (про аренду)
    RENTAL_PERIOD_DROPDOWN = (By.CLASS_NAME, "Dropdown-placeholder")   # Выпадающее окно с датой получения самоката
    RENTAL_OPTION = (By.XPATH, "//div[@class='Dropdown-option' and text()='{}']")   # позже будет использоваться format()
    COLOR_CHECKBOX = (By.XPATH, "//label[@for='{}']")   # подставить id цвета
    COMMENT_FIELD = (By.XPATH, "//input[@placeholder='Комментарий для курьера']")   # Комм для курьера
    ORDER_BUTTON = (By.XPATH, "//button[@class='Button_Button__ra12g Button_Middle__1CSJM' and text()='Заказать']")    # Кнопка Заказать
    CONFIRM_YES = (By.XPATH, "//button[@class='Button_Button__ra12g Button_Middle__1CSJM' and text()='Да']")  # Кнопка подтверждения заказа
    CONFIRM_MODAL = (By.XPATH, "//*[contains(., 'Хотите оформить заказ?')]")

    SUCCESS_MESSAGE = (By.XPATH, "//div[contains(@class, 'Order_ModalHeader') and text()='Заказ оформлен!']")  # Сообщение об успешном оформлении заказа

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def fill_first_form(self, name, surname, address, metro, phone):
        self.wait.until(EC.element_to_be_clickable(self.NAME_FIELD)).send_keys(name)
        self.driver.find_element(*self.SURNAME_FIELD).send_keys(surname)
        self.driver.find_element(*self.ADDRESS_FIELD).send_keys(address)
        metro_input = self.driver.find_element(*self.METRO_FIELD)    # Выбор станции метро из выпадающего списка
        metro_input.send_keys(metro)
        self.wait.until(EC.element_to_be_clickable((By.XPATH, f"//div[text()='{metro}']"))).click()
        self.driver.find_element(*self.PHONE_FIELD).send_keys(phone)
        self.driver.find_element(*self.NEXT_BUTTON).click()

    def fill_second_form(self, date, rental_period, color, comment):
        date_input = self.driver.find_element(*self.DATE_FIELD)    # Дата
        date_input.send_keys(date)
        date_input.send_keys(Keys.ENTER)    # Закрытие календаря

        self.driver.find_element(*self.RENTAL_PERIOD_DROPDOWN).click()    # Период аренды
        self.wait.until(EC.element_to_be_clickable((self.RENTAL_OPTION[0], self.RENTAL_OPTION[1].format(rental_period)))).click()
        
        color_id = "black" if color == "чёрный жемчуг" else "grey"    # Цвет (чёрный или серый)
        color_checkbox = self.driver.find_element(self.COLOR_CHECKBOX[0], self.COLOR_CHECKBOX[1].format(color_id))
        self.driver.execute_script("arguments[0].click();", color_checkbox)  # Клик через JS на всякий случай
        self.driver.find_element(*self.COMMENT_FIELD).send_keys(comment)    # Комм

        self.driver.find_element(*self.ORDER_BUTTON).click()    # Кликаем по кнопке "Заказать"
        WebDriverWait(self.driver, 15).until(EC.visibility_of_element_located(self.CONFIRM_MODAL))    # Ждем появления всплявающего окна с подтверждением заказа
        # Ждем пока кнопка "Да" появится в DOM
        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, "//button[@class='Button_Button__ra12g Button_Middle__1CSJM' and text()='Да']")))

        # Небольшая пауза для полной отрисовки, вдруг поможет
        time.sleep(1)

        # Находим кнопку и кликаем через JS
        confirm_button = self.driver.find_element(By.XPATH, "//button[@class='Button_Button__ra12g Button_Middle__1CSJM' and text()='Да']")
        self.driver.execute_script("arguments[0].click();", confirm_button)

        WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located(self.SUCCESS_MESSAGE))    # Ждем появления сообщения об успехе

    def get_success_message(self):
        return self.wait.until(EC.visibility_of_element_located(self.SUCCESS_MESSAGE)).text
