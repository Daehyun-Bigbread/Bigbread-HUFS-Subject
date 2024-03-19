# 수정 전
class Employee:
    def __init__(self, type_of_employee, base_salary):
        self.type_of_employee = type_of_employee
        self.base_salary = base_salary

    def calculate_salary(self):
        if self.type_of_employee == "permanent":
            return self.base_salary + 1000
        elif self.type_of_employee == "temporary":
            return self.base_salary + 500
        elif self.type_of_employee == "intern":
            return self.base_salary + 200

permanent_employee = Employee("permanent", 3000)
print(permanent_employee.calculate_salary())

temporary_employee = Employee("temporary", 3000)
print(temporary_employee.calculate_salary())

intern_employee = Employee("intern", 3000)
print(intern_employee.calculate_salary())

# 수정 후
class Employee(AB):
    def __init__(self, base_salary):
        self.base_salary = base_salary

    def calculate_salary(self):
        pass

class PermanentEmployee(Employee):
    def calculate_salary(self):
        return self.base_salary + 1000

class TemporaryEmployee(Employee):
    def calculate_salary(self):
        return self.base_salary + 500

class InternEmployee(Employee):
    def calculate_salary(self):
        return self.base_salary + 200


permanent_employee = Employee("permanent", 3000)
print(permanent_employee.calculate_salary())

temporary_employee = Employee("temporary", 3000)
print(temporary_employee.calculate_salary())

intern_employee = Employee("intern", 3000)
print(intern_employee.calculate_salary())
