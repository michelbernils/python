magicians = ['alice', 'david', 'carolina']
for magician in magicians:
    print(magician.title() + ", that was a good trick")

print("----------------------------------------------")

for value in range (1,5):
    print(value)

print("----------------------------------------------")

numbers = list(range(1,6))
print(numbers)

print("----------------------------------------------")

even_numbers = list(range(2,12,2))
print(even_numbers)

print("----------------------------------------------")

squares = []
for value in range(1,11):
    square = value**2
    squares.append(square)

print(squares)

print("----------------------------------------------")

digits = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print(min(digits))
print(max(digits))
print(sum(digits))

print("----------------------------------------------")

players = ['charles',  'martina', 'michael', 'floresce', 'eli']
print(players[0:3])

for player in  players[:3]:
    print(player.title())

print("----------------------------------------------")

my_foods = ['pizza', 'falafel', 'carrot cake']
friend_foods = my_foods[:]

my_foods.append('cannoli')
friend_foods.append('ice cream')

print("My favorites foods are: ")
print(my_foods)

print("\nMy friend's favorite foods are:")
print(friend_foods)
