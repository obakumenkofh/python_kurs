class Person:
    def __init__(self, name):
        self.name = name

    def get_info(self):
        return f"Employee {self.name}"


class Employee(Person):
    def __init__(self, name, salary_per_h):
        super().__init__(name)
        self.salary = salary_per_h


class Customer(Person):
    def __init__(self, name):
        super().__init__(name)
        self.purchases = []


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

    def print_information(self):
        print(f"All information about the shop {self.name}:")
        print(f"The budget is: {self.budget}:")
        for animal in self.animals:
            print(animal.get_info())
        for equip in self.equipment:
            print(equip.get_info())

    def add_animal(self, animal):
        self.animals.append(animal)

    def buy_animal(self, animal):
        if self.budget - animal.price > 0:
            self.animals.append(animal)
            self.budget -= animal.price
        else:
            print(f"The animal is too expensive, cant buy {animal.get_info()}")

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

    def get_total_inventory_value(self):
        total_value = 0
        for animal in self.animals:
            total_value += animal.price
        for equip in self.equipment:
            total_value += equip.price
        return total_value


if __name__ == "__main__":
    # here we can test the class
    alisa = Employee("Alisa", 12)
    alisa.get_info()


"""
more stuf to do:

Attributes:
* `location`: The physical location of the pet shop.
* `employees`: A list of employees working in the pet shop, each represented by an employee object.
* `customers`: A list of customers who have made purchases at the pet shop.
* `sales_history`: A list to keep track of all sales made at the pet shop.
* `opening_hours`: A schedule or time range indicating when the pet shop is open.
* `loyalty_program`: Information about the pet shop's loyalty program or membership system.

Methods:
* `hire_employee(employee)`: Add an employee to the list of employees working in the pet shop.
* `fire_employee(employee)`: Remove an employee from the list of employees.
* `make_sale(customer, items)`: Record a sale, including the customer and the items purchased. Update the revenue and sales history.
* `list_employees()`: Display a list of all employees with their information.
* `list_customers()`: Display a list of all customers who have made purchases.
* `get_daily_sales(date)`: Retrieve and display the sales made on a specific date.
* `set_opening_hours(hours)`: Set or update the opening hours of the pet shop.
* `add_to_loyalty_program(customer)`: Enroll a customer in the loyalty program.
* `loyalty_discount(customer)`: Apply a discount to a purchase for loyalty program members.
* `print_receipt(customer, items)`: Generate and print a receipt for a customer's purchase.
* `promote_product(product)`: Promote a specific product or item for marketing purposes.
"""
