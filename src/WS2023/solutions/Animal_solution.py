import random
from PIL import Image, ImageTk
import tkinter as tk
import os, sys

random.seed(0)


class Animal:
    """
        :param name:
        :param species:
        :param age:
        :param sex:
        :param size:
        :param breed:
        :param number_legs:
        :param happiness:
        :param price:
    """

    def __init__(self, name, species, age, sex, size, breed=None, number_legs=None, happiness=0, price=0):
        self.name = name
        self.species = species
        self.age = age
        self.sex = sex
        self.size = size
        self.number_legs = number_legs
        self.breed = breed
        self.price = price
        self.happiness = happiness

    def play_gif(self, gif_name):
        # this function loads a .gif file and plots in a window, nothing fancy
        # copied from google
        gif_path = "../gifs/" + gif_name
        animated_gif = Image.open(gif_path)

        window = tk.Tk()
        window.title("Animated GIF Viewer")

        # Create a list to store individual frames
        frames = []

        # Load each frame of the animated GIF
        try:
            while True:
                frames.append(ImageTk.PhotoImage(animated_gif))
                animated_gif.seek(animated_gif.tell() + 1)
        except EOFError:
            pass

        # Create a label to display the animated GIF
        label = tk.Label(window)
        label.pack()

        # Function to update the animated GIF
        def update_gif(frame_num):
            label.configure(image=frames[frame_num])
            window.after(100, update_gif, (frame_num + 1) % len(frames))

        # Start the main event loop
        update_gif(0)
        window.mainloop()

    def greet(self, animal):
        return ""

    def speak(self):
        return ""

    # this is an example for super() method, the naming for this function is actually bad
    def play(self):
        toys = [
            "Feather wands",
            "Laser pointers",
            "Tennis balls",
            "Frisbees",
            "Mirrors",
            "Swings",
            "Hay-filled tunnels",
            "Cardboard boxes",
            "Exercise wheels",
            "Tubes",
            "Floating basking platforms",
            "Jolly balls"
        ]
        return random.choice(toys)

    def __len__(self):
        # let's define a magic function for the super-class
        return self.size

    def get_info(self):
        return (f"Animal: {self.species}, name: {self.name}, sex: {self.sex}, breed: {self.breed}, age: {self.age}, "
                f"size: {self.size}, price: {self.price}")


class Dog(Animal):
    # if we not specify __init__ method, it will be taken from the super-class
    # theoretically we could use:
    def __init__(self, name, age, sex, size, breed=None, happiness=0, price=0):
        super().__init__(name, "Dog", age, sex, size, breed=breed, number_legs=4, happiness=happiness, price=price)

    def run(self):
        self.play_gif("dog.gif")

    def speak(self):
        return f"{self.name} the {self.species} says Woof!"

    def greet(self, animal):
        return f"Dog {self.name} sniffs {animal.name} the {animal.species}"

    def play(self):
        toy = super().play()
        return f"{self.species} plays with {toy}!"

    def __eq__(self, other):
        # let's define a magic function for the child-class
        # this function must return True is the objects are equal
        # we can compare sprecies, breed and name for example.
        if self.name == other.name and self.species == other.species and self.breed == other.breed:
            return True
        else:
            return False


class Cat(Animal):
    """
        Let's create a docstring for this function
        Class Cat() inherit class Animal.
        Methods:
            jump: plays a cat jumping gif
            speak: the cat says Meow
            greet(animal): The cat will wig tail for the animal's name
    """

    def jump(self):
        self.play_gif("cat.gif")

    def speak(self):
        return f"{self.name} the {self.species} says Meow!"

    def greet(self, animal):
        return f"Cat {self.name} wags his tail for {animal.name} the {animal.species}"

    def __add__(self, other):
        # with the probabilty 30% the cats can mate and bord a new kitten,
        # which will have the same breed as his parents and no name
        # we have not added age to the atributes so we cant set the age of th
        probability = 0.3
        if random.random() < probability:
            # new kitten is bord
            if random.random() < 0.5:
                breed = self.breed
            else:
                breed = other.breed
                Animal
            return Cat(name="no_name", species="Cat", age=0, sex=random.choice(["male", "female"]), size=0,
                       breed=breed, number_legs=4, happiness=100, price=0)

    def __str__(self):
        return f"Cat: {self.name}, breed: {self.breed}, price: {self.price}"


class Parrot(Animal):
    def march(self):
        self.play_gif("parrots.gif")

    def speak(self):
        phrases = [f"{self.name} the {self.species} says Squawk!",
                   f"Give {self.name} a cracker",
                   f"Hi, how are you?",
                   f"I love you!",
                   f"Hello there! \nGeneral {self.name}!",
                   f"Peekaboo!",
                   f"Bye-bye!",
                   f"Thank you!",
                   f"The pirate {self.name} shouts Yo-ho-ho!",
                   f"No, no, bad bird!",
                   f"Good morning!",
                   f"Pretty bird!",
                   f"There once was a bird that was put in cage \nThe name of the bird was the {self.name} the {self.breed}",
                   f"Who's a good bird?",
                   f"I'm hungry!",
                   f"Time for bed."]
        return random.choice(phrases)

    def greet(self, animal):
        return f"Parrot {self.name} says Hello! to {animal.name} the {animal.species}"


class Fish(Animal):
    def swim(self):
        self.play_gif("fish.gif")

    def speak(self):
        return f"{self.name} the {self.species} is a silent swimmer."


def generate_animals(number_animals):
    # Define lists of names for each category of animal
    dog_names = ["Buddy", "Charlie", "Max", "Luna", "Daisy", "Bailey", "Rocky", "Bella", "Coco", "Sadie"]
    cat_names = ["Oliver", "Milo", "Simba", "Whiskers", "Lily", "Nala", "Felix", "Zoe", "Misty", "Shadow"]
    other_names = ["Bubbles", "Spike", "Cupcake", "Peanut", "Muffin", "Snickers", "Sunny", "Popcorn", "Pickle", "Oreo"]

    # Define lists of breeds for each animal
    dog_breeds = ["Labrador", "Poodle", "German Shepherd", "Golden Retriever", "Bulldog"]
    cat_breeds = ["Siamese", "Persian", "Maine Coon", "Sphynx", "Bengal"]
    parrot_breeds = ["African Grey", "Cockatiel", "Macaw", "Amazon Parrot", "Budgerigar"]
    fish_breeds = ["Goldfish", "Guppy", "Betta Fish", "Koi", "Angelfish"]
    animals = []

    # Generate dogs with different names, breeds, and random prices
    for _ in range(number_animals[0]):
        name = random.choice(dog_names)
        breed = random.choice(dog_breeds)
        price = random.randint(50, 500)
        age = random.randint(1, 15)
        sex = random.choice(["male", "female"])
        size = random.randint(10, 30)
        dog = Dog(name=name, age=age, sex=sex, size=size, breed=breed, price=price)
        animals.append(dog)

    # Generate cats with different names, breeds, and random prices
    for _ in range(number_animals[1]):
        name = random.choice(cat_names)
        breed = random.choice(cat_breeds)
        price = random.randint(20, 200)
        age = random.randint(1, 15)
        sex = random.choice(["male", "female"])
        size = random.randint(5, 15)
        cat = Cat(name=name, species="Cat", age=age, sex=sex, size=size, breed=breed, price=price)
        animals.append(cat)

    # Generate parrots with different names, breeds, and random prices
    for _ in range(number_animals[2]):
        name = random.choice(other_names)
        breed = random.choice(parrot_breeds)
        price = random.randint(100, 1000)
        age = random.randint(1, 15)
        sex = random.choice(["male", "female"])
        size = random.randint(5, 20)
        parrot = Parrot(name=name, species="Parrot", age=age, sex=sex, size=size, breed=breed, price=price)
        animals.append(parrot)

    # Generate fish with different names, breeds, and random prices
    for _ in range(number_animals[3]):
        name = random.choice(other_names)
        breed = random.choice(fish_breeds)
        price = random.randint(5, 50)
        age = random.randint(1, 15)
        size = random.randint(5, 20)
        fish = Fish(name=name, species="Fish", age=age, sex="N/A", size=size, breed=breed, price=price)
        animals.append(fish)

    return animals


if __name__ == "__main__":
    # here we can test the class
    animals = generate_animals([2, 2, 2, 2])
    for animal in animals:
        print(animal.get_info())
