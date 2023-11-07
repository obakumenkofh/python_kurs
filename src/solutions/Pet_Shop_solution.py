from Animal_solution import *
import datetime


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
        out = []
        for animal in self.animals:
            if animal.name == name:
                out.append(animal)
        return out

    def find_animal_by_species(self, species):
        out = []
        for animal in self.animals:
            if animal.species == species:
                out.append(animal)
        return out

    def get_total_inventory_value(self):
        total_value = 0
        for animal in self.animals:
            total_value += animal.price
        for equip in self.equipment:
            total_value += equip.price
        return total_value

    def buy_animal(self, animal: Animal):
        # check if we have enough money
        if self.budget >= animal.price:
            self.animals.append(animal)  # add animal to the list
            self.budget -= animal.price  # subtract money
            # make an entry in the sales history
            self.sales_history.append(f"Bought animal: {animal.get_info()},  for €{animal.price:.2f}")
        else:
            print("Not enough money to buy the animal.")

    def sell_animal(self, animal):
        # Check if animal is in the shop
        if animal in self.animals:
            self.animals.remove(animal)  # remove animal from the list
            self.budget += animal.price  # add the price of the animal to the budget
            # make an entry in the sales history
            self.sales_history.append(f"Sold animal: {animal.get_info()} for €{animal.price:.2f}")
        else:
            print("Animal not found in inventory.")

    def print_receipt(self, customer, items):
        # Generate a receipt for the customer
        print(f"Receipt for Customer: {customer}")
        total_price = 0
        for item in items:
            print(f"{item.name} - €{item.price:.2f}")
            total_price += item.price
        print(f"Total: €{total_price:.2f}")

    def print_information(self):
        print(f"All information about the shop {self.name}:")
        print(f"The budget is: {self.budget}:")
        for animal in self.animals:
            print(animal.get_info())
        for equip in self.equipment:
            print(equip.get_info())

    def black_friday_adjustment(self):
        # increase all prices of equipment in the shop by 20 if today is black friday

        # Get the current date
        year, month, day = str(datetime.date.today()).split('-')

        if day == '11' and month == '11' and year == '2023':
            for equip in self.equipment:
                equip.price += 20


"""
more stuf to do:
Attributes:
1. `name`: A name or identifier for the pet shop.
2. `location`: The physical location of the pet shop.
3. `employees`: A list of employees working in the pet shop, each represented by an employee object.
4. `customers`: A list of customers who have made purchases at the pet shop.
5. `sales_history`: A list to keep track of all sales made at the pet shop.
6. `opening_hours`: A schedule or time range indicating when the pet shop is open.
7. `loyalty_program`: Information about the pet shop's loyalty program or membership system.

Methods:
9. `hire_employee(employee)`: Add an employee to the list of employees working in the pet shop.
10. `fire_employee(employee)`: Remove an employee from the list of employees.
11. `make_sale(customer, items)`: Record a sale, including the customer and the items purchased. Update the revenue and sales history.
12. `list_employees()`: Display a list of all employees with their information.
13. `list_customers()`: Display a list of all customers who have made purchases.
14. `get_daily_sales(date)`: Retrieve and display the sales made on a specific date.
15. `set_opening_hours(hours)`: Set or update the opening hours of the pet shop.
16. `add_to_loyalty_program(customer)`: Enroll a customer in the loyalty program.
17. `loyalty_discount(customer)`: Apply a discount to a purchase for loyalty program members.
18. `print_receipt(customer, items)`: Generate and print a receipt for a customer's purchase.
19. `report_revenue()`: Generate a report showing the pet shop's revenue over a specific time period.
20. `promote_product(product)`: Promote a specific product or item for marketing purposes.
"""


def generate_equipment():
    equipment_list = [
        Equipment("Leash", 10.00),
        Equipment("Collar", 15.00),
        Equipment("Food Bowl", 7.50),
        Equipment("Bed", 30.00),
        Equipment("Toy", 5.00),
        Equipment("Brush", 8.00),
        Equipment("Shampoo", 12.00),
        Equipment("Crate", 25.00),
        Equipment("Water Dispenser", 11.00),
        Equipment("Grooming Kit", 26.00),
        Equipment("Pet Carrier", 42.00),
    ]
    return equipment_list


if __name__ == "__main__":
    # here we can test the class
    best_buy = Pet_Shop("Best's Pets", 1000)
    equipment = generate_equipment()
    animals = generate_animals([3, 2, 3, 2])
    for equp in equipment:
        best_buy.add_equipment(equp)

    for animal in animals:
        best_buy.add_animal(animal)

    best_buy.print_information()
    best_buy.black_friday_adjustment()
    best_buy.print_information()
