import time
from json import loads

from behave import *
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from features.contexts.create_user_ctx import *
from features.contexts.login_context import LOGIN_BTN
from features.fixtures import fill_form, confirm_message


@given('enter the users page')
def step_impl(context):
    context.browser.find_element_by_xpath(USERS_TAB).click()


@given('click on the add new user button')
def step_impl(context):
    context.browser.find_element_by_xpath(CREATE_USER_BTN).click()


@when('type an username that is already registered')
def step_impl(context):
    fill_form(context, INVALID_USER, VALID_EMAIL)


@when('type an email that is already registered')
def step_impl(context):
    fill_form(context, VALID_USER, INVALID_EMAIL)


@when('type all valid infos')
def step_impl(context):
    fill_form(context, VALID_USER, VALID_EMAIL)


@then('show message saying')
def step_impl(context):
    text_from_step = loads(context.text)
    confirm_message(context, text_from_step['web_ele'], text_from_step['message'])


@then('find new user in users page')
def step_impl(context):
    WebDriverWait(context.browser, 10).until(EC.element_to_be_clickable((By.NAME, "busca"))) \
        .send_keys('Nome Sobrenome')
    context.browser.find_element_by_name('busca').send_keys(Keys.ENTER)
    users_box = context.browser.find_element_by_xpath(USERS_BOX)
    assert 'Nome Sobrenome' in users_box.text


@when('delete new user successfully')
def step_impl(context):
    context.browser.find_element_by_xpath(DELETE_USER_BTN).click()
    time.sleep(.5)
    context.browser.find_element_by_xpath(CONFIRM_DELETION).click()
    context.browser.find_element_by_class_name('icon-logout').click()


@when('try to log in with deleted user')
def step_impl(context):
    context.browser.find_element_by_id('username').send_keys('new_integra_user')
    context.browser.find_element_by_id('password').send_keys('Senhas@123')
    context.browser.find_element_by_xpath(LOGIN_BTN).click()

