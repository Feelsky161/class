import json
import os
from task import Task

class TaskManager:
    def __init__(self, filename="tasks.json"):
        self.filename = filename
        self.tasks = []
        self.load_from_file()  # Загружаем задачи при создании менеджера

    def add_task(self, title):
        """Добавляет новую задачу"""
        task = Task(title)
        self.tasks.append(task)
        print(f'Задача "{title}" добавлена.')

    def mark_task_done(self, title):
        """Помечает задачу как выполненную по названию"""
        for task in self.tasks:
            if task.title == title:
                task.mark_done()
                print(f'Задача "{title}" отмечена как выполненная.')
                return
        print(f'Задача "{title}" не найдена.')

    def show_tasks(self):
        """Выводит список всех задач с номерами и статусами"""
        if not self.tasks:
            print("Список задач пуст.")
            return

        for i, task in enumerate(self.tasks, 1):
            print(f"{i}. {task.title} - {task.get_status()}")

    def save_to_file(self):
        """Сохраняет список задач в JSON-файл"""
        data = [
            {"title": task.title, "is_done": task.is_done}
            for task in self.tasks
        ]
        with open(self.filename, 'w', encoding='utf-8') as f:
            json.dump(data, f, ensure_ascii=False, indent=2)
        print("Данные сохранены.")

    def load_from_file(self):
        """Загружает список задач из JSON-файла"""
        if not os.path.exists(self.filename):
            self.tasks = []
            return

        try:
            with open(self.filename, 'r', encoding='utf-8') as f:
                data = json.load(f)
            self.tasks = [
                Task(item["title"])
                for item in data
            ]
            # Восстанавливаем статусы
            for i, item in enumerate(data):
                if item["is_done"]:
                    self.tasks[i].mark_done()
        except (json.JSONDecodeError, IOError):
            print("Ошибка при загрузке файла. Список задач инициализирован пустым.")
            self.tasks = []
