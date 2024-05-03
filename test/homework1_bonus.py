def count_occurrences(input1, input2, case_sensitive=True):
    input1 = str(input1)
    input2 = str(input2)

    if not input2:  # If the length of the input2 is zero, we can return immediately 0
        return 0

    if len(input1) < len(input2):  # If input1 is shorter than input2, return 0
        return 0

    if not case_sensitive:
        input1 = input1.lower()
        input2 = input2.lower()

    return input1.count(input2)