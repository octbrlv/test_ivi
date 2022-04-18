import time
from selenium.webdriver.common.by import By
from main import browser
from main import preconditions
from pages.elements import *


class TestIVI:

    def test_1(self, browser):
        preconditions(browser)
        # переходит в картинки
        browser.find_element(By.XPATH, Test1.header_search_pictures).click()  # Нахожу элемент "Картинки" и перехожу в них
        # выбирает большие
        # убеждается, что не менее 3 картинок в выдаче ведут на сайт ivi.ru
        elems = browser.find_elements(By.XPATH, Test1.pictures_href)    # Нахожу элементы у которых есть ссылка на ivi.ru
        assert (len(elems) >= 3)


    def test_2(self,browser):
        # Шаги:
        preconditions(browser)
        # на первых 5 страницах находит ссылки на приложение ivi в play.google.com
        # убеждается, что рейтинг приложения на кратком контенте страницы совпадает с рейтингом при переходе
        compare_raiting(browser)    # Функция, которая ищет и сравнивает рейтинги
        for j in range(2, 6):
            browser.find_element(By.XPATH, (CommonObject.page_xpath.format(index=j))).click()  # Переключаюсь на сл страницу поиска
            time.sleep(2)
            compare_raiting(browser)    # Функция, которая ищет и сравнивает рейтинги


    def test_3(self,browser):
        # Шаги:
        preconditions(browser)
        # на первых 5 страницах находит ссылку на статью в wikipedia об ivi
        # убеждается, что в статье есть ссылка на официальный сайт ivi.ru
        check_href(browser)     # Функция, которая проверяется наличие прямой ссылке на статье в вики
        for f in range(2, 6):
            browser.find_element(By.XPATH, (Test3.page_xpath.format(index=f))).click()  # Переключаюсь на сл страницу поиска
            time.sleep(2)
            check_href(browser)     # Функция, которая проверяется наличие прямой ссылке на статье в вики
