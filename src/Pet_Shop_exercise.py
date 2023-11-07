import datetime
from solutions.Animal_solution import *


class Equipment:
    def __init__(self, name, price):
        self.name = name
        self.price = price
        self.id = None
        self.owner = None

    def get_info(self):
        return f"Equipment {self.name}, price {self.price}"


class Pet_Shop:
    def __init__(self, name, budget=None):
        self.name = name
        if budget is None:
            self.budget = 0
        else:
            self.budget = budget
        self.animals = []
        self.equipment = []
        self.sales_history = []

    def add_animal(self, animal):
        self.animals.append(animal)

    def remove_animal(self, animal):
        if animal in self.animals:
            self.animals.remove(animal)

    def add_equipment(self, equipment):
        self.equipment.append(equipment)

    def remove_equipment(self, equipment):
        if equipment in self.equipment:
            self.equipment.remove(equipment)

    def list_animals(self):
        for animal in self.animals:
            print(animal.get_info())

    def list_equipment(self):
        for equip in self.equipment:
            print(f"{equip.name} - €{equip.price:.2f}")

    def find_animal_by_name(self, name):
        for animal in self.animals:
            if animal.name == name:
                return animal
        return None

    def find_animal_by_species(self, species):
        for animal in self.animals:
            if animal.species == species:
                return animal
        return None

    def get_total_inventory_value(self):
        total_value = 0
        for animal in self.animals:
            total_value += animal.price
        for equip in self.equipment:
            total_value += equip.price
        return total_value

    def buy_animal(self, animal):
        # check if we have enough money
        # add animal to the list
        # subtract money
        # make an entry in the sales history
        pass

    def sell_animal(self, animal):
        pass

    def print_information(self):
        # print all information about the shop including
        # its name, budget, all animals and all equipment
        print("the best shop")

    def black_friday_adjustment(self):
        # increase all prices of equipment in the shop by 20 if today is black friday
        # Get the current date
        year, month, day = str(datetime.date.today()).split('-')
        # check if today is 23.11.2023 and increase prices


if __name__ == "__main__":
    animals = generate_animals([2, 2, 2, 2])
    for animal in animals:
        print(animal.get_info())

"""
more stuf to do:

Attributes:
* 'location': The physical location of the pet shop.
* 'employees': A list of employees working in the pet shop, each represented by an employee object.
* 'customers': A list of customers who have made purchases at the pet shop.

* 'opening_hours': A schedule or time range indicating when the pet shop is open.

* 'loyalty_program': Information about the pet shop's loyalty program or membership system.
* 'loyalty_points': Track loyalty points for each customer.

* 'online_store': Indicate whether the pet shop also has an online store.

Methods:
* 'hire_employee(employee)': Add an employee to the list of employees working in the pet shop.
* 'fire_employee(employee)': Remove an employee from the list of employees.
* 'set_working_hours(employee, wanted_schedule)': Find the perfect schedule for the employee (may not be so perfect for everybody)
* 'allow_vacation(employee, vacation_days)': If there are enough employees in shop, allow somebody do start his/her vacation

* 'make_sale(customer, items)': Record a sale, including the customer and the items purchased. Update the revenue and sales history.
* 'list_employees()': Display a list of all employees with their information.
* 'list_customers()': Display a list of all customers who have made purchases.

* 'accept_returns(item, customer, quantity)': Handle returns or exchanges of items.

* 'set_opening_hours(hours)': Set or update the opening hours of the pet shop.

* 'add_to_loyalty_program(customer)': Enroll a customer in the loyalty program.
* 'loyalty_discount(customer)': Apply a discount to a purchase for loyalty program members.

* 'print_receipt(customer, items)': Generate and print a receipt for a customer's purchase.

* 'process_online_order(order)': If the pet shop has an online store, process and fulfill online order. 
"""
