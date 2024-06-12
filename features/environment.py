# before_all / after_all
# before_feature / after_feature
# before_step / afetr_step
# before_tag / after_tag
from lib.base_methods import BaseMethods
from lib.browser import get_browser
from tests import DOMAIN


def before_scenario(context, scenario):
    if "no-browser" in scenario.effective_tags:
        return
    context.url = DOMAIN
    browser = get_browser()

    context.browser = browser
    context.base_methods = BaseMethods(browser)
    browser.get(context.url)





def after_scenario(context, scenario):
    if "no-browser" in scenario.effective_tags:
        return
    context.browser.quit()