from behave import *

from features.contexts.graphic_ctx import *
from features.contexts.login_ctx import DASHBOARD_URL

from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


@when('time filter is chosen')
def step_impl(context):
    period_select = context.browser.find_element_by_name('period')
    period_options = period_select.find_elements_by_tag_name('option')
    for period in period_options:
        period.click()
        assert_canvas_present(context)


@when('integration filter is chosen')
def validation(context):
    i = 0
    for integration in get_integrations(context):
        if i != 0:
            integration_list = get_integrations(context)
            integration = integration_list[i]
        integration.click()
        context.browser.find_element_by_xpath(GENERATE_GRAPHIC).click()
        assert_dashboard_parameter(context, integration)
        i += 1


def assert_dashboard_parameter(context, integration):
    integration_selected = get_integrations(context, integration)
    value = integration_selected.get_attribute("value")
    assert context.browser.current_url == DASHBOARD_URL + f'?process={value}'


def get_integrations(context, integration=0):
    integration_select = context.browser.find_element_by_name('integration')
    integration_options = integration_select.find_elements_by_tag_name('option')
    if integration == 0:
        return integration_options
    else:
        for integra in integration_options:
            if integra.get_attribute('selected'):
                return integra


# def step_impl(context):
#     check_integrations_info(context, INTEGRATIONS_INFO_1)
#     check_integrations_info(context, INTEGRATIONS_INFO_2)


@then('show integrations information of the {div}')
def check_integrations_info(context, div):
    info_div = context.browser.find_element_by_xpath(div)
    info_list = info_div.find_elements_by_tag_name('h3')
    for info in info_list:
        assert info.text != ''


@then('show integrations graphic')
def assert_canvas_present(context):
    # ASSERTS ALL CANVAS ELEMENTS ARE PRESENT AND VISIBLE IN THE PAGE (INCLUDING THE GRAPHIC)
    canvas_list = context.browser.find_elements_by_tag_name('canvas')
    for canvas in canvas_list:
        WebDriverWait(context.browser, 5).until(EC.visibility_of(canvas))
