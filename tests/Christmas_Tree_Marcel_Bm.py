# Basic:
def print_christmas_tree(height):
    for i in range(height):
        print(' ' * (height - i - 1), end='')
        print('*' * (2 * i + 1))
    print(' ' * (height - 1) + '|')

print_christmas_tree(4)


# Intermediate:
def make_num_xmas_tree(height):
    for i in range(height):
        start = 1
        end = 2 * i + 2
        numbers = ''.join(str(x % 10) for x in range(start, end))
        print(' ' * (height - i - 1) + numbers)
    print(' ' * (height - 1) + '|')

print("make_num_xmas_tree")
make_num_xmas_tree(5)


# Advanced:
def palindrome_xmas_tree(height):
    for i in range(height):
        left_half = ''.join(str(x % 10) for x in range(1, i + 2))
        right_half = left_half[-2::-1]
        print(' ' * (height - i - 1) + left_half + right_half)
    print(' ' * (height - 1) + '|')

print("palindrome_xmas_tree")
palindrome_xmas_tree(7)

