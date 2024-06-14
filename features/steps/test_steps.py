from behave import given, when, then
from faker import Faker


@given('my word is {name}')
@given('my last name is {name}')
@given('my name is {name}')
def get_input(context, name):
    if hasattr(context, "input_name"):
        context.input_name += name
    else:
        context.input_name = name

@given('I choose a word at random')
def generate_word(context):
    # context.fake_data:Faker
    context.input_name = context.fake_data.word()



@when('I count the letters in my word')
@when('I count the letters in my name')
def count_letters(context):
    context.name_length = len(context.input_name)


@then('there should be {letter_count} letters in total')
def check_count(context, letter_count):
    assert context.name_length == int(letter_count),\
        (f'Expected name length to be {letter_count}'
         f' characters, but it was {context.name_length}')