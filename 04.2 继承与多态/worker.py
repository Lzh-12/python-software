class Worker:
    def __init__(self, name, age, sex):
        self.name = name
        self.age = age
        self.sex = sex

    def get(self):
        print(f"姓名：{self.name}, 年龄：{self.age}, 性别：{self.sex}")


class Manager(Worker):
    def __init__(self, name, age, sex, job, yearly_salary):
        super().__init__(name, age, sex)
        self.job = job
        self.yearly_salary = yearly_salary

    def get(self):
        super().get()
        print(f"职务：{self.job}, 年薪：{self.yearly_salary}")


class Staff(Worker):
    def __init__(self, name, age, sex, department, salary_per_month):
        super().__init__(name, age, sex)
        self.department = department
        self.salary_per_month = salary_per_month

    def get(self):
        super().get()
        print(f"所属部门：{self.department}")


if __name__ == '__main__':
    worker = Worker('张三', 20, '男')
    worker.get()

    manager = Manager('叶子', 26, '女', '主管经理', 60000)
    manager.get()

    staff = Staff('李四', 25, '男', '技术部', 10000)
    staff.get()
