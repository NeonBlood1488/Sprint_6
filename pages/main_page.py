from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class MainPage(BasePage):
    # Локаторы
    COOKIE_BUTTON = (By.ID, "rcc-confirm-button")
    QUESTION_LOCATOR = (By.XPATH, "//div[@id='accordion__heading-{}']")
    ANSWER_LOCATOR = (By.XPATH, "//div[@id='accordion__panel-{}']/p")
    ORDER_BUTTON_TOP = (By.XPATH, "(//button[text()='Заказать'])[1]")
    ORDER_BUTTON_BOTTOM = (By.XPATH, "(//button[text()='Заказать'])[2]")
    SCOOTER_LOGO = (By.XPATH, "//img[@alt='Scooter']")
    YANDEX_LOGO = (By.XPATH, "//img[@alt='Yandex']")

    def __init__(self, driver):
        super().__init__(driver)

    # Принимаем кукисы, если баннер отображается
    def accept_cookies(self):
        try:
            self.click(self.COOKIE_BUTTON, timeout=5)
        except:
            pass

    def click_question(self, index):
        question_locator = (By.XPATH, f"//div[@id='accordion__heading-{index}']")
        self.scroll_and_click(question_locator)
        answer_panel = (By.ID, f"accordion__panel-{index}")
        self.wait_for_visibility(answer_panel)   # Ждем появления панельки с ответом

    def get_answer_text(self, index):
        answer_locator = (By.XPATH, f"//div[@id='accordion__panel-{index}']/p")
        return self.get_text(answer_locator)

    def click_order_button_top(self):
        self.click(self.ORDER_BUTTON_TOP)

    def click_order_button_bottom(self):
        self.scroll_and_click(self.ORDER_BUTTON_BOTTOM)

    def click_scooter_logo(self):
        self.click(self.SCOOTER_LOGO)

    def click_yandex_logo(self):
        self.click(self.YANDEX_LOGO)
