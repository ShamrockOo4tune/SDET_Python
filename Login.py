from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec


class Login:
    def __init__(self, driver, mailbox_login, mailbox_pswd):
        self.driver = driver
        self.mailbox_login = mailbox_login
        self.mailbox_pswd = mailbox_pswd
        self.mailbox_login_locator = 'passp-field-login'  # Локатор ID поля ввода логина на странице
        self.mailbox_pswd_locator = 'passp-field-passwd'  # Локатор ID поля ввода пароля на странице
        self.enter_button = 'passp:sign-in'               # Локатор кнопки "Войти"

    def enter_login(self):
        self.driver.find_element_by_id(self.mailbox_login_locator).send_keys(self.mailbox_login)
        self.driver.find_element_by_id(self.enter_button).click()

        # Ждем подгрузки на страницу поля для ввода пароля
        self.passw = WebDriverWait(self.driver, 10).until(ec.visibility_of_element_located((By.ID,
                                                                                            self.mailbox_pswd_locator)))
        self.passw.send_keys(self.mailbox_pswd)
        self.driver.find_element_by_id(self.enter_button).click()
        return self.driver
