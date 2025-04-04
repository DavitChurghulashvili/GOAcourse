def even_only(numbers):
    result = []
    for number in numbers:
        if number % 2 == 0:
            result.append(number)
    return result
print(even_only([2,4,10,5,3,1,12,16]))