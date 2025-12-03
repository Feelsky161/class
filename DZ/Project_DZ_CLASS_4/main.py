from student import Student
from car import Car
from address import Address

def main():
    print("=== Создание объектов ===\n")

    # Создаём 3 студентов
    students = [
        Student("Анна", 20, "М-101"),
        Student("Иван", 19, "И-202"),
        Student("Мария", 21, "М-103")
    ]

    # Создаём 3 машины
    cars = [
        Car("А123ВС77", "Toyota Camry", "серебристый", 200),
        Car("В456ММ77", "Honda Accord", "чёрный", 180),
        Car("К789ТТ77", "Ford Focus", "синий", 120)
    ]

    # Создаём 3 адреса
    addresses = [
        Address("Москва", "Ленина", "15", "34"),
        Address("Санкт-Петербург", "Невский", "20", "56"),
        Address("Казань", "Татарстан", "10", "78")
    ]

    print("=== Вывод информации об объектах ===\n")

    # Выводим информацию о студентах
    for i, student in enumerate(students, 1):
        print(f"Студент {i}:")
        student.display_info()
        print(f"Пол: {student.get_gender()}")
        print('-' * 30)

    # Выводим информацию об автомобилях
    for i, car in enumerate(cars, 1):
        print(f"Автомобиль {i}:")
        car.display_info()
        print(f"Утилизационный сбор: {car.calculate_util_fee()} руб.")
        print(f"Транспортный налог: {car.calculate_transport_tax()} руб.")
        print('-' * 30)

    # Выводим информацию о местах жительства
    for i, addr in enumerate(addresses, 1):
        print(f"Адрес {i}:")
        addr.display_info()
        print('-' * 30)


if __name__ == "__main__":
    main()
