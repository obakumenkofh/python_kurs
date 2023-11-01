from Animal import *
from Pet_Shop import *

animals = generate_animals([2, 2, 2, 2])

for animal in animals:
    print(animal.get_info())

dogs = animals[:2]
cats = animals[2:4]

for i, dog in enumerate(dogs):
    print(dog.greet(cats[i]))

best_buy = Pet_Shop("Oleg's Pets", 50)
best_buy.add_animal(animals[0])
best_buy.buy_animal(animals[-1])
best_buy.print_information()
