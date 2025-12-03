class Student:
    def __init__(self, name, age, group_number):
        self.name = name
        self.age = age
        self.group_number = group_number

    def display_info(self):
        """Вывести всю информацию о студенте"""
        print(f"Студент: {self.name}")
        print(f"Возраст: {self.age}")
        print(f"Группа: {self.group_number}")

    def get_gender(self):
        """Определить пол по имени (если заканчивается на 'а' — женский)"""
        if self.name.endswith('а') or self.name.endswith('я'):
            return "женский"
        else:
            return "мужской"
