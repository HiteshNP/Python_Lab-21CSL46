"""By using the concept of inheritance write a python program to find the area of triangle,
circle and rectangle."""


class Employee:
    def __init__(self):
        self.name = input("Enter Employee name: ")
        self.empId = input("Enter Employee ID: ")
        self.dept = input("Enter Employee Dept: ")
        self.salary = int(input("Enter Employee Salary: "))

    def show_emp_details(self):
        print("Employee Details")
        print("Name:", self.name)
        print("ID:", self.empId)
        print("Dept:", self.dept)
        print("Salary:", self.salary)

    def update_salary(self):
        self.salary = int(input("Enter new Salary: "))
        print("Updated Salary:", self.salary)


e1 = Employee()
e1.show_emp_details()
e1.update_salary()
