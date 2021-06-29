import time
from behave import *

from features.contexts.view_scheduled_ctx import VIEW_SCHEDULE_BTN, SCHEDULE_SELECT, SCHEDULE_TITLE


@when('go to the Schedules tab')
def step_impl(context):
    context.browser.find_element_by_xpath('/html/body/aside/nav/ul/a[3]').click()


@when('select each schedule and click on the button')
def step_impl(context):
    form = context.browser.find_element_by_xpath(SCHEDULE_SELECT)
    options = form.find_elements_by_tag_name('option')
    for i in options:
        form.click()
        options[0].click()
        context.browser.find_element_by_xpath(VIEW_SCHEDULE_BTN)
        schedule_name = context.browser.find_element_by_xpath(SCHEDULE_TITLE)
        option_name = options[0].text
        assert schedule_name.text == option_name


@then('show the list of processes found in that schedule')
def step_impl(context):
    # Validation is already being done on the last step
    pass
