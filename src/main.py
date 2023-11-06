from solutions.Pet_Shop_solution import *

animals = generate_animals([2, 2, 2, 2])
cat = animals[3]
cat.jump()
for animal in animals:
    print(animal.get_info())

dogs = animals[:2]
cats = animals[2:4]

for index, dog in enumerate(dogs):
    print(dog.greet(cats[index]))

best_buy = Pet_Shop("Best's Pets", 50)
best_buy.add_animal(animals[0])
best_buy.buy_animal(animals[-1])
best_buy.print_information()
