names = []
for x in range(5):
    name = input("enter name: ")
    names.append(name)
    for name in names:
        if len(name) > 5:
            print("the name consists of more than five letters")