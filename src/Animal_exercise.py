import random
from PIL import Image, ImageTk
import tkinter as tk
import os, sys

random.seed(0)




class Animal:
    # set name, species, age, sex, size as positional arguments
    # and breed, number_legs, happiness, price as keyword arguments
    def __init__(self, name, species, age, sex, size, breed=None, number_legs=4, happiness=100, price=0):
        self.name = name
        # some(*args, *krgs)
        self.species = species
        if age > 0:
            self.age = age
        self.sex = sex
        if size > 0:
            self.size = size
        self.number_legs = number_legs
        self.breed = breed
        self.price = price
        self.happiness = happiness

    def greet(self, animal):
        # Dog Willy says Hello to Cat Max!
        return ""

    def speak(self):
        # Dog Willy says Hello to you!
        return ""

    def __len__(self):
        # let's define a magic function for the super-class
        return ""

    def get_info(self):
        # make an output like
        # Animal: Dog, name: Max, sex: male, breed: Labrador, age: 4, size: 22, price: 0
        return ""

    # this has the same motivation but different implementation
    def __str__(self):
        return ""

    # this is an example for super() method, the naming for this function is actually bad
    def play(self):
        # pick a random toy and play with it
        # Dog Willy plays with the toy_name!
        toy = get_random_toy()
        return ""

    def play_gif(self, gif_name):
        # this function loads a .gif file and plots in a window, nothing fancy
        # copied from google
        gif_path = "gifs/" + gif_name
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

    def get_random_toy(self):
        toys = ["Feather wands", "Laser pointer", "Tennis ball", "Frisbee", "Mirror", "Swing", "Hay-filled tunnel",
                "Cardboard box", "Wheel", "Tube", "Floating platform", "LED lamp"]
        return random.choice(toys)


class Dog(Animal):
    # if we not specify __init__ method, it will be taken from the super-class
    # theoretically we could use:
    def __init__(self, name, age, sex, size, breed=None, happiness=0, price=0):
        super().__init__(name, "Dog", age, sex, size, breed=breed, number_legs=4, happiness=happiness, price=price)


    # this function overwrites the Animal.speak function
    def speak(self):
        # return a string of a Dog that speaks
        # output : Dog Name says Woof!
        pass

    def greet(self, animal):
        # return a string of a dog greeting another animal (dogs normally sniff)
        # output : Dog Willy sniffs Max the Cat
        pass

    def play(self):
        # get random toy from the parent class, play with it and
        # increase the happiness by 5
        pass

    def run(self):
        # use play_gif of the parent class to play running dog gif
        pass

    def __eq__(self, other):
        # let's define a magic function for the child-class
        # this function must return True is the objects are equal
        # we can compare sprecies, breed and name for example.
        return True


class Cat(Animal):
    """
        Let's create a docstring for this function
    """

    def jump(self):
        # play a jumping cat gif
        pass

    def speak(self):
        # say Meow
        pass

    def greet(self, animal):
        # wink the tail to another animal
        pass

    def __add__(self, other):
        # with the probability 30% the cats of the same sex can mate and born a new kitten,
        # which will have the same breed as one of his parents and no name
        probability = 0.3
        if random.random() < probability:
            return ""


# Change this for your animal:
class Your_animal(Animal):
    def __init__(self):
        super().__init__()

    def your_method(self):
        pass


if __name__ == "__main__":
    #  name, species, age, sex, size, breed, number_legs, happiness, price
    # here we can test the class
    dog1 = Animal("Willy",
                  "Dog",
                  12,
                  "male",
                  32,
                  "Retriever",
                  4,
                  100,
                  25)

    cat1 = Animal("Max",
                  "Cat",
                  9,
                  "female",
                  20,
                  "Ginger",
                  4,
                  100,
                  26)

    dog2 = Dog(name="Charlie",
               age=6,
               sex="female",
               size=10,
               breed="German Shepherd",
               happiness=100,
               price=25)
