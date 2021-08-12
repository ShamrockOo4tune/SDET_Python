from BasePage import BasePage
from selenium.webdriver.common.by import By


class Locators:
    MESSAGES_LOCATOR = (By.XPATH, f'//span[@title="Simbirsoft Тестовое задание"]')  # Тип и локатор темы входящих писем
    NEW_MESSAGE_BUTTON = (By.XPATH, '//span[@class="mail-ComposeButton-Text"]')     # Тип и локатор кнопки "написать"


class MessagesPage(BasePage):

    def get_messages_qty(self) -> int:
        messages = self.find_elements(Locators.MESSAGES_LOCATOR, time=40)
        messages_qty = len(messages)
        return messages_qty

    def click_on_start_new_message(self):
        return self.find_element(Locators.NEW_MESSAGE_BUTTON).click()
