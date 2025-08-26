import flet as ft
import os
from Homework.Copy_file import copy_file
from Homework.Delete_file import delete_file
from Homework.Count_files import count_files_in_folder
from Homework.Rename_file import rename_file

def main(page: ft.Page):
    page.title = "Homework File Manager"
    page.window_width = 100
    page.window_height = 100
    page.window_left = 100
    page.window_top = 50
    page.window_maximizable = True
    page.window_minimizable = True
    page.window_resizable = True


    page.update()


    source = ft.TextField(label="Файл (source)", width=300, height=30)
    destination = ft.TextField(label="Копия (destination)", width=300, height=30)
    source_box = ft.Container(content=source, margin=ft.margin.only(bottom=12))
    dest_box = ft.Container(content=destination, margin=ft.margin.only(bottom=28))
    delete_path = ft.TextField(label="Файл для удаления", width=300, height=30)
    count_path = ft.TextField(label="Папка для подсчета файлов", width=300, height=30)
    rename_path = ft.TextField(label="Файл для переименования", width=300, height=30)
    result1 = ft.Text(value="", color="green")
    result2 = ft.Text(value="", color="green")
    result3 = ft.Text(value="", color="green")
    result4 = ft.Text(value="", color="green")


    # обработчики
    def copy_action(e):
        try:
            copy_file(source.value, destination.value)
            result1.value = f"Файл скопирован в {destination.value}"
            result1.color = "green"
        except Exception as ex:
            result1.value = f"Ошибка: {ex}"
            result1.color = "red"
        result1.update()
        page.update()

    def delete_action(e):
        try:
            delete_file(delete_path.value)
            result2.value = f"Файл {delete_path.value} удален"
            result2.color = "green"
        except Exception as ex:
            result2.value = f"Ошибка: {ex}"
            result2.color = "red"
        result2.update()
        page.update()

    def count_action(e):
        try:
            cnt = count_files_in_folder(count_path.value)
            result3.value = f"Всего файлов: {cnt}"
            result3.color = "green"
        except Exception as ex:
            result3.value = f"Ошибка: {ex}"
            result3.color = "red"
        result3.update()
        page.update()

    def rename_action(e):
        try:
            rename_file(rename_path.value)
            result4.value = f"Файл {rename_path.value} успешно переименован"
            result4.color = "green"
        except Exception as ex:
            result4.value = f"Ошибка: {ex}"
            result4.color = "red"
        result4.update()
        page.update()

    page.add(
        ft.Column(

            [
                ft.Text("Копирование файла", weight="bold"),
                source_box,
                dest_box,
                ft.ElevatedButton("Копировать", on_click=copy_action, width=100, height=30),
                result1,

                ft.Divider(),
                ft.Text("Удаление файла", weight="bold"),
                delete_path,
                ft.ElevatedButton("Удалить", on_click=delete_action, width=100, height=30),
                result2,

                ft.Divider(),
                ft.Text("Подсчет файлов", weight="bold"),
                count_path,
                ft.ElevatedButton("Посчитать", on_click=count_action, width=100, height=30),
                result3,

                ft.Divider(),
                ft.Text("Переименование файла (добавление даты)", weight="bold"),
                rename_path,
                ft.ElevatedButton("Переименовать", on_click=rename_action, width=150, height=30),
                result4,
            ],
            spacing=1,
            expand=True
        )
    )


if __name__ == "__main__":
    ft.app(target=main, view=ft.AppView.FLET_APP)
