from selenium.webdriver import *


# FUNCTION THAT INSTANCES THAT THE BROWSER IS CHROME AND THAT IT QUITS ONCE THE TEST IS OVER
def browser_chrome(context):
    # -- BEHAVE-FIXTURE: Similar to @contextlib.contextmanager
    context.browser = Chrome(executable_path='C:/Selenium WebDriver/chromedriver.exe')
    # context.browser.
    yield context.browser
    # -- CLEANUP-FIXTURE PART:
    context.browser.quit()


# FUNCTION TO TIMEOUT THE TEST IF NECESSARY
def timeout_for_page_load(context):
    context.browser.set_page_load_timeout(8)


# -- NOTE: Change False for True if you want ipdb debugger running when an error happens
BEHAVE_DEBUG_ON_ERROR = False


def setup_debug_on_error(userdata):
    global BEHAVE_DEBUG_ON_ERROR
    BEHAVE_DEBUG_ON_ERROR = userdata.getbool("BEHAVE_DEBUG_ON_ERROR")
