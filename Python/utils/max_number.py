def find_max(list_numbers):
    max_number = list_numbers[0]
    for i in list_numbers:
        if i > max_number:
            max_number = i

    return max_number

