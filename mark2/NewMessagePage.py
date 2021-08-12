from BasePage import BasePage
from selenium.webdriver.common.by import By


class Locators:
    ADDRESS_TO = (By.XPATH, '//div[@class="composeYabbles"][1]')              # Тип локатора, локатор поля "Кому"
    TITLE = (By.XPATH, '//input[contains(@class, "composeTextField")]')       # Тип локатора, локатор поля "Тема"
    MESSAGE_BODY = (By.XPATH, '//div[contains(@class, "cke_contents_ltr")]')  # Тип локатора, локатор поля тела письма
    SEND_BUTTON = (By.XPATH, '//div[contains(@class, "-SendButton")]')        # Тип локатора, локатор кнопки "Отправить"
    IS_SENT = (By.XPATH, '//div[@class="ComposeDoneScreen-Title"]/span')      # Тип локатора, локатор заголовка "Письмо отправлено"

class NewMessagePage(BasePage):

    def enter_address_to(self, login):
        address_field = self.find_element(Locators.ADDRESS_TO, time=20)
        address_field.send_keys(login + '@yandex.ru')
        return address_field

    def enter_title(self, title_string):
        title_field = self.find_element(Locators.TITLE)
        title_field.send_keys(title_string)
        return title_field

    def enter_body(self, messages_qty):
        body_field = self.find_element(Locators.MESSAGE_BODY)
        body_field.send_keys(f'найдено писем: {messages_qty}')
        return body_field

    def click_on_send_button(self):
        return self.find_element(Locators.SEND_BUTTON).click()

    def check_if_message_sent(self):
        return self.find_element(Locators.IS_SENT).text
