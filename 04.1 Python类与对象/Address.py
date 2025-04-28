class Address:
    def __init__(self, country, province, city, street, postal_code):
        self.country = country
        self.province = province
        self.city = city
        self.street = street
        self.postal_code = postal_code

    def get(self):
        print(f"{self.street}, {self.city}, {self.province}" f", {self.postal_code}, {self.country}")


if __name__ == '__main__':
    my_address = Address('中国', '广东', '广州', '五山', 51009)
    my_address.get()
