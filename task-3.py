list_of_numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
for numbers in list_of_numbers:
    if numbers == 1:
        percentage_by_text = 'процент'
    elif numbers in [2, 3, 4]:
        percentage_by_text = 'процента'
    else:
        percentage_by_text = 'процентов'
    print(f'{numbers} {percentage_by_text}')

