import allure
import pytest
from pages.main_page import MainPage
from data import FAQ_DATA

@allure.feature('Часто задаваемые вопросы')
class TestQuestions:
    @allure.title("Проверка ответа на вопрос #{index}")
    @allure.story('Проверка текста ответов на вопросы')
    @pytest.mark.parametrize("index, expected_text",                  # index – номер вопроса, expected_text – ожидаемый ответ
                             [(i, item[1]) for i, item in enumerate(FAQ_DATA)],
                             ids=[f"faq_{i}" for i in range(len(FAQ_DATA))])
    def test_faq_answer_text(self, driver, index, expected_text):
        main_page = MainPage(driver)
        main_page.accept_cookies()
        main_page.click_question(index)  # Раскрываем вопрос
        actual_text = main_page.get_answer_text(index)
        assert actual_text == expected_text, f"Ожидался текст: {expected_text}, получен: {actual_text}"
