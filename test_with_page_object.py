from selenium import webdriver
from login_page import *
from new_message_page import *
from inbox_page import *


# setup cоздает объект драйвера с заданным типом браузера и путем к драйверу браузера (внешнему файлу)
def setup(webdriver_type, webdriver_path):
    return eval(f'webdriver.{webdriver_type}(executable_path="{webdriver_path}")')


# Сам тест здесь
def test(webdriver_type, webdriver_path, auth_url, mailbox_login, mailbox_pswd, message_title):
    driver = setup(webdriver_type=webdriver_type, webdriver_path=webdriver_path)
    driver.get(auth_url)  # передаем адрес точки входа в драйвер
    login_form = Login(driver, mailbox_login=mailbox_login, mailbox_pswd=mailbox_pswd)
    driver = login_form.enter_login()  # создаем экземпляр странички и входим в почту

    messages_form = Messages(driver, message_title=message_title)  # экземпляр странички с входящими сообщениями
    message_title_qty = messages_form.get_mesages_qty()  # считаем сообщения с указанной темой
    driver = messages_form.start_new_message()  # начинаем писать новое сообщение

    new_message = NewMessage(driver, mailbox_login=mailbox_login, message_title_qty=message_title_qty)  # заполняем
    new_message.send_message()  # отправляем сообщение с реультатом подсчета
    driver.close()
    print('done')
    return 'Pass'  # это для проверки assert Pass == Pass


if __name__ == "__main__":
    assert test(
        webdriver_type='Chrome',
        webdriver_path='./chromedriver.exe',
        auth_url='https://passport.yandex.ru/auth/welcome?origin=home_desktop_ru&'
                 'retpath=https%3A%2F%2Fmail.yandex.ru%2F&backpath=https%3A%2F%2Fyandex.ru',
        mailbox_login='test.sele',
        mailbox_pswd='ytnybr',
        message_title='Simbirsoft Тестовое задание') == 'Pass'
