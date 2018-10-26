alien_0 = {'color': 'red', 'points': 5}
alien_1 = {'color': 'blue', 'points': 10}
alien_2 = {'color': 'yellow', 'points': 15}

aliens = [alien_0, alien_1, alien_2]

for alien in aliens:
    print(alien)


#MORE REAL EXEMPLE
#MAKE 30 GOBLINS

goblins = []

for goblin_number in  range(30):
    new_goblin = {'color': 'green', 'points': 5, 'speed': 'slow'}
    goblins.append(new_goblin)

for goblin in goblins[:5]:
    print(goblin)

print("Total number of aliens: " + str(len(goblins)))

for goblin in goblins[0:3]:
    if goblin['color']
