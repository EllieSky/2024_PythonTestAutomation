def make_xmas_tree(height):
    for i in range(1, height + 1):
        print(" " * (height - i) + "*" * (2 * i - 1))
    print(" " * (height - 1) + "|")


print("Basic: make_xmas_tree(3)")
make_xmas_tree(3)


def make_xmas_tree(height):
    for i in range(1, height + 1):
        print(" " * (height - i) + "*" * (2 * i - 1))
    print(" " * (height - 1) + "|")


print("\nBasic: make_xmas_tree(5)")
make_xmas_tree(5)


def make_num_xmas_tree(num_rows):
    for i in range(1, num_rows + 1):
        print(" " * (num_rows - i), end="")
        for j in range(1, 2 * i):
            print(j, end="")
        print()

    trunk_spaces = num_rows - 1
    print(" " * trunk_spaces + "|")


print("\nIntermediate:  make_num_xmas_tree(4)")
make_num_xmas_tree(4)


def palindrome_xmas_tree(num_rows):
    for i in range(1, num_rows + 1):
        print(" " * (num_rows - i), end="")
        for j in range(1, i + 1):
            print(j, end="")
        for j in range(i - 1, 0, -1):
            print(j, end="")
        print()

    trunk_spaces = num_rows - 1
    print(" " * trunk_spaces + "|")


print("\nAdvanced: palindrome_xmas_tree(5)")
palindrome_xmas_tree(5)
