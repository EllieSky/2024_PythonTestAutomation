from pages.pages.base_page import BasePage
from tests import BASE_URL


class AddEmployee(BasePage):
    PAGE_URL = f'{BASE_URL}/pim/addEmployee'