class Employee:
    def __init__(self, id, name, salary, salary_add):
        self.id = id
        self.name = name
        self.salary = salary
        self.salary_add = salary_add

    def sum(self):
        return self.salary + self.salary_add


if __name__ == '__main__':
    employee = Employee(1, '荔枝', 10000, 100)
    print(f'员工编号：{employee.id}')
    print(f'员工姓名：{employee.name}')
    print(f'基本薪水：{employee.salary}')
    print(f'薪水增长额：{employee.salary_add}')
    print(f'增长后的工资总额：{employee.sum()}')
