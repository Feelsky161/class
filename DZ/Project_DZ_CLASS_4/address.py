class Address:
    def __init__(self, city, street, house, apartment):
        self.city = city
        self.street = street
        self.house = house
        self.apartment = apartment

    def display_info(self):
        """Вывести всю информацию о месте жительства"""
        print(f"Город: {self.city}")
        print(f"Улица: {self.street}")
        print(f"Дом: {self.house}")
        print(f"Квартира: {self.apartment}")
