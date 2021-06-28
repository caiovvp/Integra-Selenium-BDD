import time
from json import loads
from behave import *
from selenium import webdriver

from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys

from features.contexts.change_password_ctx import *
from features.contexts.login_context import LOGIN_URL, LOGIN_BTN, DASHBOARD_URL


@given('that I am logged in Integra')
def step_impl(context):
    context.browser.get(LOGIN_URL)
    context.browser.find_element_by_id('username').send_keys('integra_tester')
    context.browser.find_element_by_id('password').send_keys('Senha@123')
    context.browser.find_element_by_xpath(LOGIN_BTN).click()
    assert context.browser.current_url == DASHBOARD_URL


@given('enter the user profile')
def step_impl(context):
    context.browser.find_element_by_xpath(USER_PROFILE).click()


@when('type password')
def step_impl(context):
    text_from_step = loads(context.text)
    context.browser.find_element_by_id('password').send_keys(text_from_step['password'])
    context.browser.find_element_by_id('confirm').send_keys(text_from_step['password'] + Keys.ENTER)
    time.sleep(0.5)


@when('type different passwords')
def step_impl(context):
    text_from_step = loads(context.text)
    context.browser.find_element_by_id('password').send_keys(text_from_step['password'] + 'long')
    context.browser.find_element_by_id('confirm').send_keys(text_from_step['password'] + Keys.ENTER)


@then('log out of Integra')
def step_impl(context):
    webdriver.ActionChains(context.browser).send_keys(Keys.ESCAPE).perform()
    context.browser.find_element_by_class_name('icon-logout').click()


@when('try to log in with the new password')
def step_impl(context):
    text_from_step = loads(context.text)
    for i in range(2):
        context.browser.find_element_by_id('username').send_keys(text_from_step['user'])
        context.browser.find_element_by_id('password').send_keys(text_from_step['password'][i])
        context.browser.find_element_by_xpath(LOGIN_BTN).click()
    assert context.browser.current_url == DASHBOARD_URL
