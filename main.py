from load_data import load_tasks
from users_actions import (
    add_task,
    complete_task,
    delete_task,
    edit_task,
    list_tasks
)


def main():
    """Главное меню приложения"""

    tasks = load_tasks()

    while True:
        print("\n" + "="*50)
        print("📌 УПРАВЛЕНИЕ СПИСКОМ ДЕЛ")
        print("1. ➕ Добавить задачу")
        print("2. 📋 Показать все задачи")
        print("3. ✅ Отметить выполненной")
        print("4. 🗑️ Удалить задачу")
        print("5. ✏️ Редактировать задачу")
        print("6. 🚪 Выход")
        print("="*50)

        choice = input("Выберите действие (1-6): ")

        if choice == "1":
            tasks = add_task(tasks)
        elif choice == "2":
            list_tasks(tasks)
        elif choice == "3":
            tasks = complete_task(tasks)
        elif choice == "4":
            tasks = delete_task(tasks)
        elif choice == "5":
            tasks = edit_task(tasks)
        elif choice == "6":
            print("👋 До свидания!")
            break
        else:
            print("❌ Неверный выбор. Введите 1-6.")


if __name__ == "__main__":
    main()
