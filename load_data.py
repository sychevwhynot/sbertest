import json
import os

from const import TASKS_FILE


def load_tasks():
    """Загружает задачи из JSON-файла"""

    if not os.path.exists(TASKS_FILE):
        with open(TASKS_FILE, "w", encoding="utf-8") as f:
            json.dump([], f)
        print("📁 Создан новый файл tasks.json")
        return []

    try:
        with open(TASKS_FILE, "r", encoding="utf-8") as f:
            content = f.read().strip()

            if not content:
                print("📄 Дел нет")
                return []
            
            tasks = json.loads(content)

            return tasks
    except Exception as e:
        print(f"❌ Непредвиденная ошибка: {e}")
        return []


def save_tasks(tasks):
    """Сохраняет задачи в JSON-файл"""

    with open(TASKS_FILE, "w", encoding="utf-8") as f:
        json.dump(tasks, f, ensure_ascii=False, indent=4)
