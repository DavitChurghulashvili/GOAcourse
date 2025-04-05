cars = ["BMW", "Porsche", "Mercedes", "BMW"]
print(cars.count("BMW"))
for car in cars:
    if cars.count(car) > 1:
        cars.remove(car)
        print(cars)


           