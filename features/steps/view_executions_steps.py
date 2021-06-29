from behave import *

from features.contexts.view_executions_ctx import EXECUTIONS_TAB, ALL_PROCESSES, PROCESS_TITLE


@given('go to the Executions tab')
def step_impl(context):
    context.browser.find_element_by_xpath(EXECUTIONS_TAB).click()


@when('go to all processes')
def step_impl(context):
    context.browser.find_element_by_xpath(ALL_PROCESSES).click()


@then('show the all the executions of all processes')
def step_impl(context):
    process_title = context.browser.find_element_by_xpath(PROCESS_TITLE)
    assert process_title.text == 'Todos as execuções do processo'