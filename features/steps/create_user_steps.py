import time
from behave import *

from features.contexts.create_use_ctx import *


@given('click on the add new user button')
def step_impl(context):
    context.browser.find_element_by_xpath(CREATE_USER_BTN).click()


@when('user type username that already exists')
def step_impl(context):
    context.browser.find_element_by_id('username').send_keys('integra_tester')
    context.browser.find_element_by_id('password').send_keys('Senha@123')


@when('user type different passwords on the boxes')
def step_impl(context):
    pass


@when('user type all valid infos')
def step_impl(context):
    pass


@then('show message saying:')
def step_impl(context):
    pass