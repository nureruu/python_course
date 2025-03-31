import flet as ft
from datetime import datetime


class Task:
    def __init__(self, text, created_at, is_completed=False):
        self.text = text
        self.created_at = created_at
        self.is_completed = is_completed

    def __str__(self):
        return f"{self.text} (Создано: {self.created_at.strftime('%Y-%m-%d %H:%M:%S')}) {'✅' if self.is_completed else '❌'}"

def main(page: ft.Page):
    page.title = "Управление задачами"
    page.theme_mode = ft.ThemeMode.LIGHT

    task_list = []

    task_input = ft.TextField(label="Введите задачу", autofocus=True)
    task_history = ft.Text("Список задач:")

    def add_task(e):
        task_text = task_input.value.strip()
        if task_text:
            created_at = datetime.now()
            new_task = Task(task_text, created_at)
            task_list.append(new_task)
            task_input.value = ''
            update_task_list()
        else:
            task_history.value = "Введите текст задачи!"

        page.update()

    def update_task_list():
        task_history.value = "Список задач:\n"
        for task in task_list:
            task_history.value += f"{task}\n"
        page.update()

    def sort_by_date(e):
        task_list.sort(key=lambda task: task.created_at, reverse=True)
        update_task_list()

    def sort_by_status(e):
        task_list.sort(key=lambda task: task.is_completed)
        update_task_list()


    add_task_button = ft.ElevatedButton("Добавить задачу", on_click=add_task)
    sort_date_button = ft.TextButton("Сортировать по дате", on_click=sort_by_date)
    sort_status_button = ft.TextButton("Сортировать по статусу", on_click=sort_by_status)


    page.add(
        task_input,
        add_task_button,
        sort_date_button,
        sort_status_button,
        task_history
    )

ft.app(target=main)


#hw 4
# ft.app(target=main, view=ft.WEB_BROWSER)


