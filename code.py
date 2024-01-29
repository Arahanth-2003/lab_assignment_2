class Employee:
    def __init__(self, id,name, age, salary):
        self.id = id
        self.name = name
        self.age = age
        self.salary = salary

    def __str__(self):
        return f"{self.id} {self.name} ({self.age}): {self.salary}"

class Table:
    def __init__(self, employees):
        self.employees = employees

    def sort_by_age(self):
        self.employees.sort(key=lambda x: x.age)

    def sort_by_name(self):
        self.employees.sort(key=lambda x: x.name)

    def sort_by_salary(self):
        self.employees.sort(key=lambda x: x.salary)

    def print_table(self):
        for employee in self.employees:
            print(employee)

def main():
    employees = [
        Employee("161E90","Ramu", 35, 59000),
        Employee("171E22","Tejas", 30, 82100),
        Employee("171G55","Abhi", 25, 100000),
        Employee("152K46","Jaya", 32, 85000),
    ]

    table = Table(employees)

    while True:
        choice = input("Choose sorting parameter (1. Age, 2. Name, 3. Salary): ")
        if choice == "1":
            table.sort_by_age()
        elif choice == "2":
            table.sort_by_name()
        elif choice == "3":
            table.sort_by_salary()
        else:
            print("Invalid choice")
            break

        table.print_table()

if __name__ == "__main__":
    main()
