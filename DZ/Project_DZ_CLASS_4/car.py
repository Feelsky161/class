class Car:
    def __init__(self, gov_number, model, color, horsepower):
        self.gov_number = gov_number
        self.model = model
        self.color = color
        self.horsepower = horsepower  # л.с.

    def display_info(self):
        """Вывести всю информацию об автомобиле"""
        print(f"Гос. номер: {self.gov_number}")
        print(f"Модель: {self.model}")
        print(f"Цвет: {self.color}")
        print(f"Мощность (л.с.): {self.horsepower}")

    def calculate_util_fee(self):
        """Рассчитать стоимость утилизационного сбора (базовая ставка + надбавка за мощность)"""
        base_fee = 20000  # базовая ставка в рублях
        power_surcharge = self.horsepower * 50  # 50 руб. за каждую л.с.
        total_fee = base_fee + power_surcharge
        return total_fee

    def calculate_transport_tax(self, tax_rate_per_hp=150):
        """
        Рассчитать транспортный налог
        :param tax_rate_per_hp: ставка налога за 1 л.с. (по умолчанию 150 руб.)
        """
        return self.horsepower * tax_rate_per_hp
