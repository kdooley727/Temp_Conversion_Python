'''Here is what you asked for'''

def temp_conversion(temp, unit=None):
    if unit is None:
        if temp[-1] == 'K':
            unit = 'K'
            temp = float(temp[:-1])
        elif temp[-1] == 'F':
            unit = 'F'
            temp = float(temp[:-1])
        elif temp[-1] == 'C':
            unit = 'C'
            temp = float(temp[:-1])
        else:
            return "Invalid temperature unit"

    if unit == 'K':
        k = str(temp) + 'K'
        c = str(temp - 273.15) + 'C'
        f = str((temp - 273.15) * 9 / 5 + 32) + 'F'
        return c, k, f
    elif unit == 'F':
        f = str(temp) + 'F'
        c = str((temp - 32) * 5 / 9) + 'C'
        k = str((temp - 32) * 5 / 9 + 273.15) + 'K'
        return c, k, f
    elif unit == 'C':
        c = str(temp) + 'C'
        f = str((temp * 9 / 5) + 32) + 'F'
        k = str(temp + 273.15) + 'K'
        return f, k, c
    else:
        return "Invalid temperature unit"

user_input = input('Enter temp with measurement: ')
result = temp_conversion(user_input)
print(result)




''' Feature that asks what the output temperature measurement you want

def convert_temperature(value, input_scale, output_scale):
    if input_scale == 'C':
        if output_scale == 'F':
            return value * 1.8 + 32
        elif output_scale == 'K':
            return value + 273.15
        else:
            return value
    elif input_scale == 'F':
        if output_scale == 'C':
            return (value - 32) / 1.8
        elif output_scale == 'K':
            return (value + 459.67) * 5 / 9
        else:
            return value
    elif input_scale == 'K':
        if output_scale == 'C':
            return value - 273.15
        elif output_scale == 'F':
            return value * 9 / 5 - 459.67
        else:
            return value
    else:
        return value

while True:
    # Prompt the user for input
    print('Enter the input temperature value:')
    value = float(input())
    print('Enter the input temperature scale (C, F, or K):')
    input_scale = input().upper()
    print('Enter the output temperature scale (C, F, or K):')
    output_scale = input().upper()
    result = convert_temperature(value, input_scale, output_scale)
    print(f'{value} {input_scale} = {result} {output_scale}')

    # Prompt the user to continue or quit
    print('Enter q to quit, or any other key to continue:')
    choice = input()
    if choice.lower() == 'q':
        break'''



