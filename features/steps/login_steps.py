from json import loads
import time
from behave import *
from features.contexts.login_context import *


@given('that I am on the login page')
def check_login_page(context):
    context.browser.get(LOGIN_URL)
    time.sleep(1)
    assert context.browser.current_url == LOGIN_URL


@when('type valid credentials')
def attempt_login(context):
    text_from_step = loads(context.text)
    context.browser.find_element_by_id('username').send_keys(text_from_step['user'])
    context.browser.find_element_by_id('password').send_keys(text_from_step['password'])
    context.browser.find_element_by_xpath(LOGIN_BTN).click()
    time.sleep(2)


@then('the dashboard page should open')
def check_open_dashboard(context):
    assert context.browser.current_url == DASHBOARD_URL
    time.sleep(1)


# %% Scenario 2 specific:

@when('type invalid credentials')
def step_impl(context):
    text_from_step = loads(context.text)
    for i in range(2):
        context.browser.find_element_by_id('username').send_keys(text_from_step["user"][i])
        context.browser.find_element_by_id('password').send_keys(text_from_step["password"][i])
        context.browser.find_element_by_xpath(LOGIN_BTN).click()
        time.sleep(1)


@then('the website should show an error message saying invalid user or password')
def check_error_message(context):
    error_box = context.browser.find_element_by_xpath(ERROR_BOX)
    error_message = loads(context.text)
    assert error_message['msg_error'] in error_box.text
    time.sleep(1)
# %
