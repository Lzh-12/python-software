class Person:
    def __init__(self, name='', address='', sex='', age=0):
        self.name = name
        self.address = address
        self.sex = sex
        self.age = age

    def get(self):
        print(f"{self.name}, {self.address}, {self.sex}, {self.age}")


class Student(Person):
    def __init__(self, name='', address='', sex='', age=0, math_score=90., english_score=99):
        super().__init__(name, address, sex, age)  # 调用父类的构造方法
        self.__math_score = math_score
        self.__english_score = english_score

    def get(self):
        super().get()  # 调用父类的get方法显示基本信息
        print(f"Math Score: {self.__math_score}, English Score: {self.__english_score}")


if __name__ == '__main__':
    person = Person('叶子', '广州', '男', 20)
    person.get()

    student = Student('张三', '深圳', '男', 19, 90, 95)
    student.get()
