import time
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By


@pytest.fixture(scope='function')
def browser():
    s = Service(r"C:\Users\nstrokova\Documents\test_ivi\chromedriver\chromedriver.exe")     # Прописываю путь к вебдрайверу
    wd = webdriver.Chrome(service=s)        # Создаю объект wd и с помощью вебдрайвера использую хром браузер
    wd.maximize_window()        # Открываю хром в полноэкранном режиме
    yield wd       # Возвращаю объект браузера
    wd.quit()

def preconditions(browser):
    # xpath и тестовые данные
    search_field = "//input[@title='Поиск']"
    search_text = "ivi"

    # неавторизованный пользователь заходит в https://www.google.com/\
    browser.get("https://www.google.ru/")  # Перехожу по url
    # ищет ivi
    browser.find_element(By.XPATH,search_field).send_keys(search_text)      # Нахожу элемент "Поле поиска" и пишу туда текст
    browser.find_element(By.XPATH,search_field).submit()        # Нахожу элемент "Поле поиска" и нажимаю клавишу enter
