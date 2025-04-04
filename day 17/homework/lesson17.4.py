def filter_positive(numbers):
    negative_numbers = []

    for number in numbers:
        if number < 0:
            negative_numbers.append(number)
    
    return negative_numbers
print(filter_positive([1,-1, 2,-4, 5,-7]))
