# 雇员
class Employee:
    def __init__(self, name):
        self.name = name

    def calculate_salary(self):
        pass


# 经理
class Manager(Employee):
    def __init__(self, name, fix_salary):
        super().__init__(name)
        self.fix_salary = fix_salary

    def calculate_salary(self):
        # 固定工资
        return self.fix_salary


# 销售人员
class Salesman(Employee):
    def __init__(self, name, base_salary, commission):
        super().__init__(name)
        self.base_salary = base_salary
        self.commission = commission

    def calculate_salary(self):
        # 基本工资加销售提成
        return self.base_salary + self.commission


# 一般工人
class Worker(Employee):
    def __init__(self, name, daily_salary, days):
        super().__init__(name)
        self.daily_salary = daily_salary
        self.days = days

    def calculate_salary(self):
        # 按每月工作的天数计算工资
        return self.daily_salary * self.days


if __name__ == '__main__':
    manager = Manager('张三', 6000)
    salesman = Salesman('李四', 5000, 1000)
    worker = Worker('王五', 200, 20)
    print(f"经理{manager.name}的工资：{manager.calculate_salary()}")
    print(f"销售人员{salesman.name}的工资：{salesman.calculate_salary()}")
    print(f"工人{worker.name}的工资：{worker.calculate_salary()}")
