from behave import step


@step('I authenticate as Admin')
def authenticate(context):
    context.page.login_page.authenticate()


@step('I authenticate successfully')
def wait_for_successful_login(context):
    context.page.login_page.wait_for_successful_login()


@step('the welcome message should be {string}')
def check_welcome_message(context, string):
    greeting = context.user_menu.get_greeting()
    assert string == context.user_menu.get_greeting(), \
        (f'Expected welcome message to be {string}'
         f' but it was {greeting}')


@step('the header should be {header}')
def check_page_header(context, header):
    page_header = context.page.employee_list.get_page_header()
    assert header == page_header, \
        f'Expected header to be {header} but it was {page_header}'