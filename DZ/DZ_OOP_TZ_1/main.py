from task import Task
from task_manager import TaskManager

def main():
    manager = TaskManager()

    print("Программа управления списком дел. Доступные команды:")
    print("  add    — добавить задачу")
    print("  done   — отметить задачу как выполненную")
    print("  show   — показать список задач")
    print("  exit   — сохранить и выйти")

    while True:
        command = input("\nВведите команду: ").strip().lower()

        if command == "add":
            title = input("Введите название задачи: ").strip()
            if title:
                manager.add_task(title)
            else:
                print("Название задачи не может быть пустым.")

        elif command == "done":
            title = input("Введите название задачи: ").strip()
            if title:
                manager.mark_task_done(title)
            else:
                print("Название задачи не может быть пустым.")

        elif command == "show":
            manager.show_tasks()

        elif command == "exit":
            manager.save_to_file()
            print("Программа завершена.")
            break

        else:
            print("Неизвестная команда. Попробуйте: add, done, show, exit.")

if __name__ == "__main__":
    main()
