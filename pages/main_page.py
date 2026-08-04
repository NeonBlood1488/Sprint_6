from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

class MainPage:
    # Локаторы элементов главной страницы. По их названиям понятно, что каждый из них значит
    COOKIE_BUTTON = (By.ID, "rcc-confirm-button")   # Кукисы
    QUESTION_LOCATOR = (By.XPATH, "//div[@id='accordion__heading-{}']")
    ANSWER_LOCATOR = (By.XPATH, "//div[@id='accordion__panel-{}']/p")
    ORDER_BUTTON_TOP = (By.XPATH, "(//button[text()='Заказать'])[1]")
    ORDER_BUTTON_BOTTOM = (By.XPATH, "(//button[text()='Заказать'])[2]")
    SCOOTER_LOGO = (By.XPATH, "//img[@alt='Scooter']")
    YANDEX_LOGO = (By.XPATH, "//img[@alt='Yandex']")

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def accept_cookies(self):    # Принимаем куки, когда баннер отображается
        try:
            self.wait.until(EC.element_to_be_clickable(self.COOKIE_BUTTON)).click()
        except:
            pass

    def click_question(self, index):    # Кликаем на вопрос по индексу (0-7) и ждём появления ответа
        question = self.driver.find_element(self.QUESTION_LOCATOR[0], self.QUESTION_LOCATOR[1].format(index))
        self.driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", question)
        self.driver.execute_script("arguments[0].click();", question)
        self.wait.until(EC.visibility_of_element_located((By.ID, f"accordion__panel-{index}")))  # Ждем, когда панель с ответом станет видимой

    def get_answer_text(self, index):   # Возврат текста ответа на вопрос по индексу
        answer = self.driver.find_element(self.ANSWER_LOCATOR[0], self.ANSWER_LOCATOR[1].format(index))
        return answer.text

    def click_order_button_top(self):
        self.wait.until(EC.element_to_be_clickable(self.ORDER_BUTTON_TOP)).click()  # Кликаем на кнопку "Заказать" (верхняя к-рая)

    def click_order_button_bottom(self):   # Прокручиваем и кликаем на нижнюю кнопку "Заказать" (через JS для надёжности, а то там проблемки были)
        button = self.driver.find_element(*self.ORDER_BUTTON_BOTTOM)
        self.driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", button)
        self.driver.execute_script("arguments[0].click();", button)

    def click_scooter_logo(self):
        self.wait.until(EC.element_to_be_clickable(self.SCOOTER_LOGO)).click()  # Клик на лого Самоката

    def click_yandex_logo(self):
        self.wait.until(EC.element_to_be_clickable(self.YANDEX_LOGO)).click()   # Кликаем на лого Яндекса
