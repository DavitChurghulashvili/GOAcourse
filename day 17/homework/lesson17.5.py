def filter_negative(numbers):
    positive_numbers = []

    for number in numbers:
        if number > 0:
            positive_numbers.append(number)
    
    return positive_numbers
print(filter_negative([1,-1, 2,-4, 5,-7]))