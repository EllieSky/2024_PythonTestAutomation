

first_name = input('Please enter your name:  ')

age = int(input(' How old are you? '))

message = f'So very nice to meet you, {first_name}!'
# two possible ways to do this ::

# if age <= 18:
#     message = message + ' '+ 'Hope you had a great day at school.'
# else:
#     message = message + ' '+'Hope you had a fantastic day at work.'
if age <= 18:
    message2 = 'Hope you had a great day at school'
else:
    message2 = 'Hope you had a fantastic day at work'

print(message +' ' + message2)


def chat():
    food = input('what is your fav food? ')
    print(f"oohh! i like {food} too!!!")

    answer = input('keep chatting? y/n: ')
    if answer == 'y':
        chat()

chat()


