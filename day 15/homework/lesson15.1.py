user_input = input("Type something: ")
def Small():
    return user_input.lower()
def Big():
    return user_input.upper()
def Capital():
    return user_input.capitalize()
print(Small())
print(Big())
print(Capital())

