from selenium import webdriver
from Login import *
from NewMessage import *
from Messages import *


def setup(webdriver_type, webdriver_path):
    """setup cоздает объект драйвера с заданным типом браузера (webdriver_type: str) и
    путем к драйверу браузера (webdriver_path: str) - внешнему файлу"""
    return eval(f'webdriver.{webdriver_type}(executable_path="{webdriver_path}")')


def test_send_message(webdriver_type, webdriver_path, auth_url, mailbox_login, mailbox_pswd, message_title):
    driver = setup(webdriver_type=webdriver_type, webdriver_path=webdriver_path)
    driver.get(auth_url)
    login_form = Login(driver=driver, mailbox_login=mailbox_login, mailbox_pswd=mailbox_pswd)
    driver = login_form.enter_login()  # создаем экземпляр странички с логином и входим в почту

    messages_form = Messages(driver, message_title=message_title)  # экземпляр странички с входящими сообщениями
    message_title_qty = messages_form.get_mesages_qty()
    assert message_title_qty >= 0

    driver = messages_form.start_new_message()
    new_message = NewMessage(driver, mailbox_login=mailbox_login, message_title_qty=message_title_qty)
    new_message.send_message()
    result = WebDriverWait(driver, 20).until(ec.visibility_of_element_located((
        By.XPATH, '//div[@class="ComposeDoneScreen-Title"]/span'))).text
    assert result == 'Письмо отправлено'
    driver.close()
    print('done')


if __name__ == "__main__":
    test_send_message(
        webdriver_type='Chrome',
        webdriver_path='./chromedriver.exe',
        auth_url='https://passport.yandex.ru/auth/welcome?origin=home_desktop_ru&'
                 'retpath=https%3A%2F%2Fmail.yandex.ru%2F&backpath=https%3A%2F%2Fyandex.ru',
        mailbox_login='test.sele',
        mailbox_pswd='ytnybr',
        message_title='Simbirsoft Тестовое задание')
