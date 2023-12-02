class Employee:
    def __init__(self, name, employee_id, salary):
        self.name = name
        self.employee_id = employee_id
        self.salary = salary

    def __str__(self):
        return f"Employee ID: {self.employee_id}, Name: {self.name}, Salary: ${self.salary}/year"


class Manager(Employee):
    def __init__(self, name, employee_id, salary, department):
        super().__init__(name, employee_id, salary)
        self.department = department

    def __str__(self):
        return super().__str__() + f", Department: {self.department}"

    def manage_team(self):
        return f"{self.name} is managing the {self.department} department."


class Engineer(Employee):
    def __init__(self, name, employee_id, salary, programming_language):
        super().__init__(name, employee_id, salary)
        self.programming_language = programming_language

    def __str__(self):
        return super().__str__() + f", Programming Language: {self.programming_language}"

    def write_code(self):
        return f"{self.name} is writing code in {self.programming_language}."


class Salesperson(Employee):
    def __init__(self, name, employee_id, salary, sales_target):
        super().__init__(name, employee_id, salary)
        self.sales_target = sales_target

    def __str__(self):
        return super().__str__() + f", Sales Target: ${self.sales_target}"

    def meet_sales_target(self):
        return f"{self.name} is working to meet the sales target of ${self.sales_target}."


def main():
    # Example usage:
    manager = Manager("Sabie", 124, 80000, "Marketing")
    engineer = Engineer("Cordu_nean", 457, 75000, "COBOL")
    salesperson = Salesperson("JoEY_ca_napolitana", 926, 50000, 15)

    print(manager)
    print(manager.manage_team())

    print(engineer)
    print(engineer.write_code())

    print(salesperson)
    print(salesperson.meet_sales_target())


if __name__ == "__main__":
    main()