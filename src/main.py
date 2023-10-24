from Animal import *
from Pet_Shop import *

# Example usage:
animals = generate_animals([2, 2, 2, 2])

for animal in animals:
    print(animal.get_info())

dogs = animals[:2]
cats = animals[2:4]

for i, dog in enumerate(dogs):
    print(dog.greet(cats[i]))