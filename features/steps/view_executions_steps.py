from behave import *

from features.contexts.view_executions_ctx import EXECUTIONS_TAB, ALL_PROCESSES, PROCESS_TITLE, OPEN_LIST_BTN, \
    UL_OPTIONS, SHOW_EXECUTIONS_BTN, EXECUTION_TITLE
from features.fixtures import find_by_link


@given('go to the Executions tab')
def step_impl(context):
    find_by_link(context, '/integra/execucoes').click()


@when('go to all processes')
def step_impl(context):
    context.browser.find_element_by_xpath(ALL_PROCESSES).click()


@then('show the all the executions of all processes')
def step_impl(context):
    process_title = context.browser.find_element_by_xpath(PROCESS_TITLE)
    assert process_title.text == 'Todos as execuções do processo'
    executions_length = get_executions_length(context)
    assert executions_length == 10


@when('choose a filter')
def step_impl(context):
    select_filter = context.browser.find_element_by_id('filter-by-status')
    select_options = select_filter.find_elements_by_tag_name('option')
    all_length = get_executions_length(context)
    max_length = all_length * 2
    for i in select_options:
        select_filter.click()
        i.click()
        executions_length = get_executions_length(context)
        max_length -= executions_length
    assert max_length == 0


def get_executions_length(context):
    executions_div = context.browser.find_element_by_xpath('/html/body/main/div[2]/div[1]/div[2]/div')
    executions_empty = executions_div.find_elements_by_class_name('d-none')
    executions_length = 10 - len(executions_empty)
    return executions_length


@then('show only processes according with that filter')
def step_impl(context):
    # Validation being done on the step before
    pass


@when('select a process of the list')
def open_list(context):
    context.browser.find_element_by_xpath(OPEN_LIST_BTN).click()


def get_executions(context):
    list_itens = context.browser.find_element_by_xpath(UL_OPTIONS)
    executions_li = list_itens.find_elements_by_tag_name('li')
    return executions_li


@then('show a list of all executions on that process')
def step_impl(context):
    i = 0
    for li in get_executions(context):
        if i >= 1:
            open_list(context)
            li = (get_executions(context))[i]
        execution_name = li.find_element_by_class_name('text').text
        li.click()
        context.browser.find_element_by_xpath(SHOW_EXECUTIONS_BTN).click()
        execution_title = context.browser.find_element_by_xpath(EXECUTION_TITLE).text
        assert execution_name in execution_title
        i += 1
