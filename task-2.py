

def summation_result(odd_numbers_cubed):
    resulted = 0
    for number in odd_numbers_cubed:
        sum_numbers = 0
        number_copy = number
        while number_copy:
            sum_numbers += number_copy % 10
            number_copy = number_copy // 10
        if (sum_numbers % 7) == 0:
            resulted += number
    print(resulted)

odd_numbers_cubed = []
for odd_numbers in range(1, 1000, 2):
    odd_numbers_cubed.append(odd_numbers ** 3)
summation_result(odd_numbers_cubed)

i = 0
while (i < len(odd_numbers_cubed)):
    odd_numbers_cubed[i] += 17
    i += 1

summation_result(odd_numbers_cubed)

