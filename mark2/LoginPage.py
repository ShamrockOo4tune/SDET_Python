from BasePage import BasePage
from selenium.webdriver.common.by import By


class Locators:
    MAILBOX_LOGIN_LOCATOR = (By.ID, 'passp-field-login')        # тип локатора, локатор поля ввода логина на странице
    MAILBOX_PASSWORD_LOCATOR = (By.ID, 'passp-field-passwd')    # тип локатора, локатор поля ввода пароля на странице
    ENTER_BUTTON = (By.ID, 'passp:sign-in')                     # тип локатора, локатор кнопки "Войти"


class LoginPage(BasePage):

    def enter_login(self, login: str):
        login_field = self.find_element(Locators.MAILBOX_LOGIN_LOCATOR)
        login_field.send_keys(login)
        return login_field

    def click_on_sign_in(self):
        return self.find_element(Locators.ENTER_BUTTON).click()

    def enter_password(self, password: str):
        password_field = self.find_element(Locators.MAILBOX_PASSWORD_LOCATOR)
        password_field.send_keys(password)
        return password_field
