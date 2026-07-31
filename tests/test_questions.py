import allure
import pytest
from pages.main_page import MainPage
from data import FAQ_DATA

@allure.feature('Вопросы о важном')
class TestQuestions:
    @allure.story('Проверка текста ответов')
    @pytest.mark.parametrize("index, expected_text", 
                             [(i, item[1]) for i, item in enumerate(FAQ_DATA)])
    def test_faq_answer_text(self, driver, index, expected_text):
        main_page = MainPage(driver)
        main_page.accept_cookies()
        main_page.click_question(index)
        actual_text = main_page.get_answer_text(index)
        assert actual_text == expected_text, f"Ожидался текст: {expected_text}, получен: {actual_text}"
