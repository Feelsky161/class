import csv
import os

class CarCSVManager:
    def __init__(self, csv_file):
        self.csv_file = csv_file
        # Создаём файл, если его нет
        if not os.path.exists(csv_file):
            with open(csv_file, 'w', newline='', encoding='utf-8') as f:
                pass  # пустой файл

    def create(self, car_id, model, gov_number):
        """Добавить новый автомобиль"""
        # Проверяем, не существует ли ID
        if self._find_by_id(car_id):
            print(f"Ошибка: автомобиль с ID {car_id} уже существует.")
            return False

        with open(self.csv_file, 'a', newline='', encoding='utf-8') as file:
            writer = csv.writer(file)
            writer.writerow([car_id, model, gov_number])
        print(f"Автомобиль {model} (ID: {car_id}) добавлен.")
        return True

    def read_all(self):
        """Прочитать все автомобили"""
        try:
            with open(self.csv_file, 'r', encoding='utf-8') as file:
                reader = csv.reader(file)
                rows = list(reader)
                if not rows:
                    print("Файл пуст.")
                    return []

                print("Список автомобилей:")
                for row in rows:
                    print(f"ID: {row[0]}, Модель: {row[1]}, Гос.номер: {row[2]}")
                return rows
        except FileNotFoundError:
            print("Файл не найден.")
            return []

    def update(self, car_id, new_model=None, new_gov_number=None):
        """Обновить данные автомобиля по ID"""
        rows = []
        found = False

        try:
            with open(self.csv_file, 'r', encoding='utf-8') as file:
                reader = csv.reader(file)
                for row in reader:
                    if row[0] == str(car_id):
                        if new_model:
                            row[1] = new_model
                        if new_gov_number:
                            row[2] = new_gov_number
                        found = True
                    rows.append(row)

            if not found:
                print(f"Автомобиль с ID {car_id} не найден.")
                return False

            # Перезаписываем файл
            with open(self.csv_file, 'w', newline='', encoding='utf-8') as file:
                writer = csv.writer(file)
                writer.writerows(rows)
            print(f"Данные автомобиля с ID {car_id} обновлены.")
            return True

        except FileNotFoundError:
            print("Файл не найден.")
            return False

    def delete(self, car_id):
        """Удалить автомобиль по ID"""
        rows = []
        found = False

        try:
            with open(self.csv_file, 'r', encoding='utf-8') as file:
                reader = csv.reader(file)
                for row in reader:
                    if row[0] != str(car_id):
                        rows.append(row)
                    else:
                        found = True

            if not found:
                print(f"Автомобиль с ID {car_id} не найден.")
                return False

            # Перезаписываем файл
            with open(self.csv_file, 'w', newline='', encoding='utf-8') as file:
                writer = csv.writer(file)
                writer.writerows(rows)
            print(f"Автомобиль с ID {car_id} удалён.")
            return True

        except FileNotFoundError:
            print("Файл не найден.")
            return False

    def _find_by_id(self, car_id):
        """Вспомогательный метод: проверить, существует ли автомобиль с данным ID"""
        try:
            with open(self.csv_file, 'r', encoding='utf-8') as file:
                reader = csv.reader(file)
                for row in reader:
                    if row and row[0] == str(car_id):
                        return True
            return False
        except FileNotFoundError:
            return False



# Пример использования
if __name__ == "__main__":
    # Создаём менеджер для файла cars.csv
    manager = CarCSVManager('cars.csv')

    # 1. CREATE
    manager.create(1, 'Toyota Camry', 'А123ВС777')
    manager.create(2, 'Honda Accord', 'В456ММ777')

    # 2. READ
    manager.read_all()

    # 3. UPDATE
    manager.update(1, new_model='Toyota Corolla', new_gov_number='А777АА777')

    # 4. DELETE
    manager.delete(2)

    # Ещё раз читаем
    manager.read_all()
