numbers = {
    '0': 'Zero',
    '1': 'One',
    '2': 'Two',
    '3': 'Three',
    '4': 'Four',
    '5': 'Five',
    '6': 'Six',
    '7': 'Seven',
    '8': 'Eight',
    '9': 'Nine'
}

phone = str(input('Write your phone number: '))
output = ' '

for number in phone:
    output += numbers.get(number, '-') + ' '

print(output)