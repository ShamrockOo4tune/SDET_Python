from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec


class Messages:
    def __init__(self, driver, message_title):
        self.driver = driver
        self.messages_selector = f'//span[@title="{message_title}"]'            # Локатор заданной темы сообщения
        self.new_message_selector = '//span[@class="mail-ComposeButton-Text"]'  # Локатор кнопки "написать"

    def get_mesages_qty(self) -> int:
        """Ждет подгрузки листинга входящих сообщений, удовлетворяющих заданной теме сообщения. Получает их в список,
        замеряет и возвращает ее длину (количество сообщений с заданной темой сообщения)"""
        message_title_messages = WebDriverWait(self.driver, 40) \
            .until(ec.visibility_of_all_elements_located((By.XPATH, self.messages_selector)))
        message_title_qty = len(message_title_messages)
        return message_title_qty

    def start_new_message(self):
        self.driver.find_element_by_xpath(self.new_message_selector).click()
        return self.driver
