cars = ['audi', 'bmw', 'subaru', 'toyota']

for car in cars:
    if car == 'bmw':
        print(car.upper())
    else:
        print(car.title())

print("-----------------------------------------------")

age = 17
if (age >= 18):
    print("\nYou are old enough to drink!")
else:
    print("Sorry, you're too young to drinks!")


print("-----------------------------------------------")

my_age = 23

if (age < 4):
     print("Your admission cost is $0.")
elif (age < 18):
     print("Your admission cost is $5.")
else:
     print("Your admission cost is $10.")

print("-----------------------------------------------")

requested_toppings = ['mushrooms', 'extra cheese']

if 'mushrooms' in requested_toppings:
    print("Adding mushrooms.")
if 'pepperoni' in requested_toppings:
    print("Adding pepperoni.")
if 'extra cheese' in requested_toppings:
    print("Adding extra cheese.")

print("\nFinished making your pizza!")


print("-----------------------------------------------")

available_toppings = ['mushrooms', 'olives', 'green peppers','pepperoni', 'pineapple', 'extra cheese']
requested_toppings = ['mushrooms', 'french fries', 'extra cheese']

for requested_topping in requested_toppings:
    if requested_topping in available_toppings:
       print("Adding " + requested_topping + ".")
    else:
       print("Sorry, we don't have " + requested_topping + ".")

print("\nFinished making your pizza!")

print("-----------------------------------------------")
