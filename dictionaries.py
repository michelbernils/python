alien_0 = {'x_position': 0, 'y_position': 25, 'speed': 'medium', 'color': 'blue', 'points': 5}
print(alien_0['color'])
print(alien_0['points'])

new_points = alien_0['points']
print("You just earned " + str(new_points) + " points!")


alien_1 = {}
print(alien_1)

alien_1['color'] = 'blue'
alien_1['points'] = '10'
alien_1['x_position'] = 15
alien_1['y_position'] = 25

print(alien_1)

if alien_0['speed'] == 'slow':
   x_increment = 1
elif (alien_0['x_position'] == 'medium'):
   x_increment = 2
else:
    # This must be a fast alien.
    x_increment = 3

print("Original x-position: " + str(alien_0['x_position']))

alien_0['x_position'] = alien_0['x_position'] + x_increment
print("New x-position: " + str(alien_0['x_position']))

del alien_0['points']
print(alien_0)


print("-------------------------------------------")

user_0 = {
    'username': 'efermi',
    'first': 'enrico',
    'last': 'fermi'
}

for key, value in user_0.items():
    print("\nKey: " + key)
    print("Value: " + value)

print("-------------------------------------------")

favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
}   

for name, language in favorite_languages.items():
    print(name.title() + "'s favorite language is " + language.title() + ".")
