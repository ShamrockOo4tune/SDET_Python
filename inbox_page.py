from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec


class Messages:
    def __init__(self, driver, message_title):
        self.driver = driver
        self.messages_selector = f'//span[@title="{message_title}"]'  # Селектор (локатор) для заданной темы сообщения
        self.new_message_selector = '//span[@class="mail-ComposeButton-Text"]'  # Локатор для кнопки "написать"

    def get_mesages_qty(self) -> int:
        """Ждем подгрузки листинга входящих сообщений удовлетворяющих заданной теме сообщения. Получаем их в список,
        замеряем длину списка и возвращаем ее (количество сообщений с заданной темой сообщения)"""
        message_title_messages = WebDriverWait(self.driver, 40) \
            .until(ec.visibility_of_all_elements_located((By.XPATH, self.messages_selector)))
        message_title_qty = len(message_title_messages)
        return message_title_qty

    def start_new_message(self):
        """ Простое нажатие кнопки "Написать"
        На выход передается обновленный драйвер"""
        self.driver.find_element_by_xpath(self.new_message_selector).click()
        return self.driver
