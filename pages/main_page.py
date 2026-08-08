import allure
from selenium.webdriver.common.by import By
from pages.base_page import BasePage
from locators import MainPageLocators

class MainPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    @allure.step("Принять куки, если баннер отображается")
    def accept_cookies(self):
        try:
            self.click(MainPageLocators.COOKIE_BUTTON, timeout=5)
        except:
            pass

    @allure.step("Клик по вопросу с индексом {index}")
    def click_question(self, index):
        question_locator = (By.XPATH, f"//div[@id='accordion__heading-{index}']")
        self.scroll_and_click(question_locator)
        answer_panel = (By.ID, f"accordion__panel-{index}")
        self.wait_for_visibility(answer_panel)

    @allure.step("Получить текст ответа на вопрос {index}")
    def get_answer_text(self, index):
        answer_locator = (By.XPATH, f"//div[@id='accordion__panel-{index}']/p")
        return self.get_text(answer_locator)

    @allure.step("Клик по верхней кнопке 'Заказать'")
    def click_order_button_top(self):
        self.click(MainPageLocators.ORDER_BUTTON_TOP)

    @allure.step("Клик по нижней кнопке 'Заказать'")
    def click_order_button_bottom(self):
        self.scroll_and_click(MainPageLocators.ORDER_BUTTON_BOTTOM)

    @allure.step("Клик по логотипу 'Самокат'")
    def click_scooter_logo(self):
        self.click(MainPageLocators.SCOOTER_LOGO)

    @allure.step("Клик по логотипу 'Яндекс'")
    def click_yandex_logo(self):
        self.click(MainPageLocators.YANDEX_LOGO)
