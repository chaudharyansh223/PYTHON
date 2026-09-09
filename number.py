numbers = [45, 12, 89, 74, 89, 23, 67]
largest_number = None
second_largest_number = None
for num in numbers:
    if largest_number is None or num > largest_number:
        second_largest_number = largest_number
        largest_number = num
    if largest_number != num and (second_largest_number is None or num > second_largest_number):
        second_largest_number = num
print(second_largest_number)