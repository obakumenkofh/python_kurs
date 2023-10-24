from Animal import Animal


# class Employee():
#     # we can in theory create a list of employees that own the equipment
#     def __init__(self, name):
#         self.name = name
#         self.salary_per_hour = 12


class Equipment:
    def __init__(self, name, price):
        self.name = name
        self.price = price
        self.id = None
        self.owner = None


class Pet_Shop:
    def __init__(self):
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
        for animal in self.animals:
            if animal.name == name:
                return animal
        return None

    def feed_all_animals(self):
        for animal in self.animals:
            animal.feed()

    def get_total_inventory_value(self):
        total_value = 0
        for animal in self.animals:
            total_value += animal.price
        for equip in self.equipment:
            total_value += equip.price
        return total_value


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
