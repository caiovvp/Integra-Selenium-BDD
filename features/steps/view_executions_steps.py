import time

from behave import *

from features.contexts.view_executions_ctx import EXECUTIONS_TAB, ALL_PROCESSES, PROCESS_TITLE, OPEN_LIST_BTN, \
    UL_OPTIONS, SHOW_EXECUTIONS_BTN, EXECUTION_TITLE


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


@when('open list of processes')
def step_impl(context):
    context.browser.find_element_by_xpath(OPEN_LIST_BTN).click()


@when('select a process of the list')
def get_li(context):
    list_itens = context.browser.find_element_by_xpath(UL_OPTIONS)
    executions_li = list_itens.find_elements_by_tag_name('li')
    return executions_li


@then('show a list of all executions on that process')
def step_impl(context):
    executions_li = get_li(context)
    list_length = len(executions_li)
    for i in range(list_length):
        if i >= 1:
            context.execute_steps(u'''when open list of processes''')
            executions_li = get_li(context)
        execution_name = executions_li[i].find_element_by_tag_name('span').text
        executions_li[i].click()
        context.browser.find_element_by_xpath(SHOW_EXECUTIONS_BTN).click()
        execution_title = context.browser.find_element_by_xpath(EXECUTION_TITLE).text
        assert execution_name in execution_title
