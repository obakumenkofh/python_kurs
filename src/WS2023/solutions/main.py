from solutions.Pet_Shop_solution import *
from solutions.Animal_solution import *
# here we can test the class

animals = generate_animals([2, 2, 2, 2])
best_buy = Pet_Shop("Oleg's Pets", 1000)
equipment = generate_equipment()

for equp in equipment:
    best_buy.add_equipment(equp)

for animal in animals:
    best_buy.add_animal(animal)

best_buy.print_information()
best_buy.black_friday_adjustment()
best_buy.print_information()