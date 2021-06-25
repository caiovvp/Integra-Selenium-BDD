import time
from json import loads
from behave import *

from selenium.webdriver.common.by import By
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
    time.sleep(1)
    assert context.browser.current_url == DASHBOARD_URL


@when('enters the users page')
def step_impl(context):
    context.browser.find_element_by_xpath(USERS_TAB).click()


@when('changes the old password')
def step_impl(context):
    time.sleep(1)
    text_from_step = loads(context.text)
    for i in range(4):
        WebDriverWait(context.browser, 10).until(EC.element_to_be_clickable((By.NAME, "busca"))) \
            .send_keys('Integra Tester')
        time.sleep(1)
        context.browser.find_element_by_name('busca').send_keys(Keys.ENTER)
        time.sleep(1)
        context.browser.find_element_by_xpath(USER_PROFILE).click()
        time.sleep(1)
        context.browser.find_element_by_id('eye-password').click()
        context.browser.find_element_by_xpath(EYE_PASSWORD).click()
        context.browser.find_element_by_id('password').send_keys(text_from_step['password'][i])
        context.browser.find_element_by_id('confirm').send_keys(text_from_step['password'][i] + Keys.ENTER)
        time.sleep(1)


@when('try to log in with the new password')
def step_impl(context):
    WebDriverWait(context.browser, 10).until(EC.element_to_be_clickable((By.NAME, "busca")))
    context.browser.find_element_by_class_name('icon-logout').click()
    time.sleep(1)
    text_from_step = loads(context.text)
    for i in range(2):
        context.browser.find_element_by_id('username').send_keys(text_from_step['user'])
        context.browser.find_element_by_id('password').send_keys(text_from_step['password'][i])
        context.browser.find_element_by_xpath(LOGIN_BTN).click()
        time.sleep(1)
    assert context.browser.current_url == DASHBOARD_URL
