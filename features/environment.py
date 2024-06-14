# before_all / after_all
# before_feature / after_feature
# before_step / after_step
# before_tag / after_tag
from faker import Faker
from selenium.webdriver.support.wait import WebDriverWait

from fixtures.pages import Pages
from lib.base_methods import BaseMethods
from lib.browser import get_browser
from menus.main_menu import MainMenu
from menus.user_menu import UserMenu
from tests import DOMAIN, DEFAULT_WAIT


def before_scenario(context, scenario):
    context.fake_data = Faker()

    if "no-browser" in scenario.effective_tags:
        return
    context.url = DOMAIN
    browser = get_browser()

    context.browser = browser
    context.base_methods = BaseMethods(browser)
    context.wait = WebDriverWait(browser, DEFAULT_WAIT)
    context.page = Pages(browser)
    context.user_menu = UserMenu(browser)
    context.main_menu = MainMenu(browser)

    browser.get(context.url)





def after_scenario(context, scenario):
    if "no-browser" in scenario.effective_tags:
        return
    context.browser.quit()