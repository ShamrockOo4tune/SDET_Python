from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec


class NewMessage:
    def __init__(self, driver, mailbox_login, message_title_qty):
        self.driver = driver
        self.address_to = mailbox_login + '@yandex.ru'  # склеиваем логин с доменом яндекса и получаем e-mail адрес
        self.title = 'Simbirsoft Тестовое задание. Гумеров'  # тема сообщения, в котором сообщаем результат подсчетов
        self.message_body = f'найдено писем: {message_title_qty}'  # шаблон для тела письма
        self.address_to_selector = '//div[@class="composeYabbles"][1]'  # Селектор по которому подбираем поле "Кому"
        self.title_selector = '//input[contains(@class, "composeTextField")]'  # Селектор поля "Тема"
        self.message_body_selector = '//div[contains(@class, "cke_contents_ltr")]'  # Селектор области тела письма
        self.send_button_selector = '//div[contains(@class, "-SendButton")]'  # Селектор кнопки "Отправить"

    def send_message(self):
        new_message = WebDriverWait(self.driver, 20) \
            .until(ec.visibility_of_element_located((By.XPATH, self.address_to_selector)))  # Ждем подгрузки полей
        new_message.send_keys(self.address_to)  # Указываем адрессата
        self.driver.find_element_by_xpath(self.title_selector).send_keys(self.title)  # Тема исходящего письма
        self.driver.find_element_by_xpath(self.message_body_selector).send_keys(self.message_body)  # Тело письма
        self.driver.find_element_by_xpath(self.send_button_selector).click()  # Жмем "отправить"
