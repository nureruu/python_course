import flet as ft
from datetime import datetime

def main(page: ft.Page):
    page.title = "Моё первое приложение"
    page.theme_mode = ft.ThemeMode.LIGHT
    
    greeting_text = ft.Text("Привет, мир!")

    greeting_history = []

    history_text = ft.Text("История приветствий:", style='bodyMedium')

    def on_button_click(e):
        name = name_input.value.strip()

        if name:
            greeting, greeting_color = hour(e)
            greeting_text.value = f"{greeting}, {name}!"
            greeting_text.color = greeting_color  
            greet_button.text = 'Поздороваться снова'
            name_input.value = ''

            timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            greeting_history.append(f"{timestamp}: {name}")
            history_text.value = "История приветствий:\n" + "\n".join(greeting_history)
        else:
            greeting_text.value = "Пожалуйста, введите ваше имя!"

        page.update()

    name_input = ft.TextField(label="Введите ваше имя:", autofocus=True, on_submit=on_button_click)

    def clear_history(e):
        greeting_history.clear()
        history_text.value = "История приветствий:"
        page.update()
    
    def toggle_theme(e):
        if page.theme_mode == ft.ThemeMode.LIGHT:
            page.theme_mode = ft.ThemeMode.DARK
        else:
            page.theme_mode = ft.ThemeMode.LIGHT

        page.update()

    def hour(e):
        current_hour = datetime.now().hour

        if 6 <= current_hour < 12:
            greeting = 'Доброе утро, '
            greeting_color = ft.colors.YELLOW  
        elif 12 <= current_hour < 18:
            greeting = 'Добрый день, '
            greeting_color = ft.colors.ORANGE  
        elif 18 <= current_hour < 24:
            greeting = 'Добрый вечер, '
            greeting_color = ft.colors.RED 
        elif 0 <= current_hour < 6:
            greeting = 'Доброй ночи, '
            greeting_color = ft.colors.BLUE  
        return greeting, greeting_color

    theme_button = ft.IconButton(icon=ft.icons.BRIGHTNESS_6, tooltip="Сменить тему", on_click=toggle_theme)

    clear_button = ft.TextButton("Очистить историю", on_click=clear_history)

    clear_button_icon = ft.IconButton(icon=ft.icons.DELETE, tooltip="Очиститка", on_click=clear_history)

    greet_button = ft.ElevatedButton("Поздороваться", on_click=on_button_click)

    page.add(ft.Row([theme_button, clear_button,
                     clear_button_icon], alignment=ft.MainAxisAlignment.CENTER),
             greeting_text,
             name_input,
             greet_button,
             history_text,
    )

ft.app(target=main)

#hw 
# ft.app(target=main, view=ft.WEB_BROWSER)


