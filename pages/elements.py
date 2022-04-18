import time

from selenium.webdriver.common.by import By


class CommonObject:
    page_xpath = "//a[@aria-label='Page {index}']"



class Test1:

    header_search_pictures = "//div[@class='hdtb-mitem']/a[text()='Картинки']"
    pictures_href = "//div[@id='islrg']/div/div/a/div[text()='ivi.ru']"



class Test2:
    result_link = "//div[@data-async-context='query:ivi']/div//a[contains(@href, 'https://play.google.com')]"
    rate_xpath = "//div[@data-async-context='query:ivi']/div//a[contains(@href, 'https://play.google.com')][{index}]/../../../div//span[contains(text(), 'Рейтинг:')]"
    play_market_rate_xpath = "//div[contains(@aria-label, 'Средняя оценка:')][text()]"


def compare_raiting(browser):
    elements = browser.find_elements(By.XPATH, Test2.result_link)       # нахожу все элементы имеющие ссылку на play market
    for i in range(len(elements)):      # Для каждого из найденных элементвов:
        rate = browser.find_element(By.XPATH, Test2.rate_xpath.format(index=i + 1)).text  # Ищу рейтинг иви на google.com
        browser.find_element(By.XPATH, Test2.result_link).click()  # Перехожу на страницу play_market`а
        window = browser.window_handles  # Собирает все окна из открытой сессии
        browser.switch_to.window(window[1])  # Переключаюсь на второе окно
        play_market_rate = browser.find_element(By.XPATH, Test2.play_market_rate_xpath).text  # Ищу рейтинг иви на странице play_market`а
        assert (rate.split(': '))[1] == play_market_rate  # Сравниваю рейтинги
        browser.switch_to.window(window[0])  # Переключаюсь на первое окно


class Test3:
    result_link = "//div[@data-async-context='query:ivi']/div//a[contains(@href, 'https://ru.wikipedia.org')]/h3"
    result = "//div[@data-async-context='query:ivi']/div//a[contains(@href, 'https://ru.wikipedia.org')]//cite[{index}]/../../h3"
    href_ivi_on_wiki = "//a[@href='https://www.ivi.ru/']"
    page_xpath = "//a[@aria-label='Page {index}']"

def check_href(browser):
    elements = browser.find_elements(By.XPATH, Test3.result_link)       # нахожу все элементы имеющие ссылку на вики
    for i in range(len(elements)):
        browser.find_element(By.XPATH, (Test3.result.format(index=i + 1))).click()      # Перехожу по ссылке
        window = browser.window_handles  # Собирает все окна из открытой сессии
        browser.switch_to.window(window[1])  # Переключаюсь на второе окно
        assert browser.find_element(By.XPATH, Test3.href_ivi_on_wiki)       # Проверяю наличие прямой ссылки на иви
        browser.switch_to.window(window[0])  # Переключаюсь на первое окно
