class Dog:
    def __init__(self, name, color, age):
        self.name = name
        self.color = color
        self.age = age

    def get(self):
        print(f"姓名：{self.name}, 颜色：{self.color}, 年龄：{self.age}")


if __name__ == '__main__':
    dog = Dog('旺旺', '白色', 3)
    dog.get()
