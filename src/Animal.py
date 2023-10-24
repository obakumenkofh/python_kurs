import random
from PIL import Image, ImageTk
import tkinter as tk


class Animal:
    def __init__(self, name, species, number_legs=None, breed=None, price=0):
        self.name = name
        self.species = species
        self.number_legs = number_legs
        self.breed = breed
        self.price = price

    def move(self, gif_name):
        # this function loads a .gif file and plots in a window, nothing fancy
        # copied from google
        gif_path = gif_name
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

    def get_info(self):
        return f"Animal: {self.species}, name: {self.name}, breed: {self.breed}, price: {self.price}"


class Dog(Animal):
    def run(self):
        self.move("dog.gif")

    def speak(self):
        return f"{self.name} the {self.species} says Woof!"

    def greet(self, animal):
        return f"Dog {self.name} sniffs {animal.name} the {animal.species}"


class Cat(Animal):
    def jump(self):
        self.move("cat.gif")

    def speak(self):
        return f"{self.name} the {self.species} says Meow!"

    def greet(self, animal):
        return f"Cat {self.name} wags his tail for {animal.name} the {animal.species}"


class Parrot(Animal):
    def march(self):
        self.move("parrots.gif")

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
        index = random.randint(a=0, b=len(phrases) - 1)
        return phrases[index]

    def greet(self, animal):
        return f"Parrot {self.name} says Hello! to {animal.name} the {animal.species}"


class Fish(Animal):
    def swim(self):
        self.move("fish.gif")

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
        dog = Dog(name, "Dog", number_legs=4, breed=breed, price=price)
        animals.append(dog)

    # Generate cats with different names, breeds, and random prices
    for _ in range(number_animals[1]):
        name = random.choice(cat_names)
        breed = random.choice(cat_breeds)
        price = random.randint(20, 200)
        cat = Cat(name, "Cat", number_legs=4, breed=breed, price=price)
        animals.append(cat)

    # Generate parrots with different names, breeds, and random prices
    for _ in range(number_animals[2]):
        name = random.choice(other_names)
        breed = random.choice(parrot_breeds)
        price = random.randint(100, 1000)
        parrot = Parrot(name, "Parrot", number_legs=2, breed=breed, price=price)
        animals.append(parrot)

    # Generate fish with different names, breeds, and random prices
    for _ in range(number_animals[3]):
        name = random.choice(other_names)
        breed = random.choice(fish_breeds)
        price = random.randint(5, 50)
        fish = Fish(name, "Fish", number_legs=0, breed=breed, price=price)
        animals.append(fish)

    return animals
