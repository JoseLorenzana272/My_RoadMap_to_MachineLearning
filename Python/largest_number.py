numbers = [4,5,78,41,25,69,85,41,23,65,99,87,45,100,25,45,10,25,78,554,85]
max_number = numbers[0]

for i in numbers:
    if i > max_number:
        max_number = i

print(f'The largest number is: {max_number}')