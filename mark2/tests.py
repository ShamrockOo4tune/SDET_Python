from LoginPage import LoginPage
from MessagesPage import MessagesPage
from NewMessagePage import NewMessagePage


def test_send_message(browser):
    yandex_mail_page = LoginPage(browser)
    yandex_mail_page.go_to_auth()
    yandex_mail_page.enter_login('test.sele')
    yandex_mail_page.click_on_sign_in()
    yandex_mail_page.enter_password('ytnybr')
    yandex_mail_page.click_on_sign_in()
    yandex_mail_messages_page = MessagesPage(browser)
    messages_qty = yandex_mail_messages_page.get_messages_qty()
    yandex_mail_messages_page.click_on_start_new_message()
    yandex_mail_new_message_page = NewMessagePage(browser)
    yandex_mail_new_message_page.enter_address_to('test.sele')
    yandex_mail_new_message_page.enter_title('Simbirsoft Тестовое задание. Гумеров')
    yandex_mail_new_message_page.enter_body(messages_qty=messages_qty)
    yandex_mail_new_message_page.click_on_send_button()
    result = yandex_mail_new_message_page.check_if_message_sent()
    assert result == 'Письмо отправлено'


if __name__ == '__main__':
    from selenium import webdriver
    test_send_message(browser=webdriver.Chrome(executable_path="./chromedriver.exe"))
