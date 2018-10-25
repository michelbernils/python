anime_list = ['Boruto', 'Naruto', 'Death Note', 'Anime de Sumo']
print(anime_list[0])
print(anime_list[0].title())

anime_list[1] = 'Boku no Hero'
print(anime_list)

print('------------------------------------------------')

movie_list = []
movie_list.append('A origem')
movie_list.append('Sempre ao seu lado')
movie_list.append('Venom')
movie_list.insert(3, 'Batman')
movie_list.insert(3, 'Batman 2')
print(movie_list)
del movie_list[3]
print(movie_list)

print('------------------------------------------------')

motorcycles = ['honda', 'yamaha',  'suzuki']
print(motorcycles)
popped_motorcycles = motorcycles.pop()
print(motorcycles)
print(popped_motorcycles)

print('------------------------------------------------')

cars = ['bmw', 'audi', 'chevrolet', 'ford', 'fiat']
cars.sort()
print(cars)

print('------------------------------------------------')

cars = ['bmw', 'audi', 'chevrolet', 'ford', 'fiat']
cars.sort(reverse=True) #or cars.reverse()
print(cars)

print('------------------------------------------------')

cars = ['bmw', 'audi', 'chevrolet', 'ford', 'fiat']
len(cars)

#Pagina 75 livro
