
first_name = input('Please enter your name:  ')

age = input('How old are you?  ')

message = f'So very nice to meet you, {first_name}!'

# if int(age) <= 18:
#     message = message + ' ' + 'Hope you had a great day at school.'
# else:
#     message = message + ' ' + 'Hope you had a fantastic day at work.'
# print(message)


if int(age) <= 18:
    message2 = 'Hope you had a great day at school.'
else:
    message2 = 'Hope you had a fantastic day at work.'
print(message + ' ' + message2)


def chat():
    food = input('What is one of your favorite foods? ')
    print(f'Oooh! I like {food} too!!!')

    answer = input('Keep chatting? y/n: ')
    if answer == 'y':
        chat()

chat()

