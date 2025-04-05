food = ["egg", "tomato", "bread", "pork", "cheese"]
user_input = input("would you like to clear list? : ")
if user_input == "yes":
    food.clear()
    if user_input == "no":
        print(food)
print(food)

