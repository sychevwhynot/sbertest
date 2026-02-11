import json
import os
from datetime import datetime

from load_data import save_tasks


def list_tasks(tasks):
    """Показывает задачи с возможностью фильтрации"""

    if not tasks:
        print("📭 Список задач пуст")
        return

    print("\n🔍 Показать:")
    print("1. 📋 Все задачи")
    print("2. ✅ Только выполненные")
    print("3. ⏳ Только невыполненные")

    choice = input("Выберите (1-3): ").strip()

    if choice == "2":
        filtered = [t for t in tasks if t["completed"]]
        status = "ВЫПОЛНЕННЫЕ"
    elif choice == "3":
        filtered = [t for t in tasks if not t["completed"]]
        status = "НЕВЫПОЛНЕННЫЕ"
    else:
        filtered = tasks
        status = "ВСЕ"

    if not filtered:
        print(f"📭 Нет {status.lower()} задач")
        return

    print("\n" + "="*50)
    print(f"📋 {status} ЗАДАЧИ ({len(filtered)} из {len(tasks)}):")

    for task in filtered:
        status_icon = "✅" if task["completed"] else "⏳"
        print(f"{status_icon} [{task['id']}] {task['title']}")
        print(f"     📅 {task['created_at']}")

    print("="*50 + "\n")


def add_task(tasks):
    """Добавляет новую задачу"""

    title = input("Введите название задачи: ").strip()

    if not title:
        print("❌ Название не может быть пустым!")
        return tasks

    task = {
        "id": len(tasks) + 1,
        "title": title,
        "completed": False,
        "created_at": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    }

    tasks.append(task)
    save_tasks(tasks)
    print(f"✅ Задача '{title}' добавлена (ID: {task['id']})")
    return tasks


def complete_task(tasks):
    """Отмечает задачу выполненной"""

    try:
        task_id = int(input("Введите ID задачи: ").strip())

        for task in tasks:
            if task["id"] == task_id:
                if task["completed"]:
                    print("⚠️ Задача уже выполнена")
                else:
                    task["completed"] = True
                    save_tasks(tasks)
                    print(f"✅ Задача '{task['title']}' отмечена выполненной")

                return tasks

        print(f"❌ Задача с ID {task_id} не найдена")

    except ValueError:
        print("❌ ID должен быть числом")

    return tasks


def delete_task(tasks):
    """Удаляет задачу"""

    try:
        task_id = int(input("Введите ID задачи для удаления: ").strip())

        for i, task in enumerate(tasks):
            if task["id"] == task_id:
                deleted = tasks.pop(i)

                for new_id, t in enumerate(tasks, start=1):
                    t["id"] = new_id
                save_tasks(tasks)
                print(f"🗑️ Задача '{deleted['title']}' удалена")

                return tasks

        print(f"❌ Задача с ID {task_id} не найдена")

    except ValueError:
        print("❌ ID должен быть числом")

    return tasks


def edit_task(tasks):
    """Редактирует существующую задачу"""

    try:
        task_id = int(input("Введите ID задачи для редактирования: "))
        
        for task in tasks:
            if task["id"] == task_id:
                print(f"Текущее название: {task['title']}")
                new_title = input(
                    "Введите новое название (Enter - оставить без изменений): "
                ).strip()
                
                if new_title:
                    old_title = task['title']
                    task['title'] = new_title
                    save_tasks(tasks)
                    print(
                        f"✏️ Задача '{old_title}' изменена на '{new_title}'"
                    )
                else:
                    print("⏭️ Изменений не внесено")
                
                return tasks
        
        print(f"❌ Задача с ID {task_id} не найдена")
        
    except ValueError:
        print("❌ ID должен быть числом")
    
    return tasks
