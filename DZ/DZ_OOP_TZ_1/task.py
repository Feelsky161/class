class Task:
    def __init__(self, title):
        self.title = title
        self.is_done = False  # False = "Не выполнено", True = "Выполнено"

    def mark_done(self):
        """Помечает задачу как выполненную"""
        self.is_done = True

    def get_status(self):
        """Возвращает текстовое представление статуса"""
        return "Выполнено" if self.is_done else "Не выполнено"
