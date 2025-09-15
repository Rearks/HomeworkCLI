import sys
import os
import pygame
from Homework.Copy_file import copy_file
from Homework.Delete_file import delete_file
from Homework.Count_files import count_files_in_folder
from Homework.Rename_file import rename_file
import easygui

pygame.init()

WIDTH, HEIGHT = 640, 700
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Менеджер файлов")

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GRAY = (210, 210, 210)
BLUE = (80, 140, 250)
GREEN = (0, 160, 60)
RED = (200, 40, 40)
font = pygame.font.SysFont("Arial", 18)


class Tooltip:
    def __init__(self, text):
        self.text = text
        self.visible = False
        self.pos = (0, 0)

    def show(self, pos):
        self.visible = True
        self.pos = pos

    def hide(self):
        self.visible = False

    def draw(self, screen):
        if self.visible:
            txt_surface = font.render(self.text, True, BLACK)
            screen.blit(txt_surface, self.pos)

class Label:
    def __init__(self, x, y, text):
        self.x = x
        self.y = y
        self.text = text

    def draw(self, screen):
        txt = font.render(self.text, True, BLACK)
        screen.blit(txt, (self.x, self.y))

class InputBox:
    def __init__(self, x, y, w, h, text='', is_folder_picker=False, is_file_picker=False, tooltip_text=None):
        self.rect = pygame.Rect(x, y, w, h)
        self.color = GRAY
        self.text = text
        self.txt_surface = font.render(self.text, True, BLACK)
        self.active = False
        self.hover = False
        self.is_folder_picker = is_folder_picker
        self.is_file_picker = is_file_picker
        self.tooltip = Tooltip(tooltip_text) if tooltip_text else None

    def handle_event(self, event):
        if event.type == pygame.MOUSEMOTION:
            self.hover = self.rect.collidepoint(event.pos)
            if self.tooltip:
                if self.hover:
                    self.tooltip.show(event.pos)
                else:
                    self.tooltip.hide()

        if event.type == pygame.MOUSEBUTTONDOWN:
            if self.rect.collidepoint(event.pos):
                if self.is_folder_picker:
                    folder = easygui.diropenbox(title="Выберите папку")
                    if folder:
                        self.text = folder
                        self.txt_surface = font.render(self.text, True, BLACK)
                elif self.is_file_picker:
                    file_path = easygui.fileopenbox(title="Выберите файл")
                    if file_path:
                        self.text = file_path
                        self.txt_surface = font.render(self.text, True, BLACK)
                else:
                    self.active = True
            else:
                self.active = False

        if event.type == pygame.KEYDOWN and self.active:
            if event.key == pygame.K_BACKSPACE:
                self.text = self.text[:-1]
            else:
                self.text += event.unicode
            self.txt_surface = font.render(self.text, True, BLACK)

    def draw(self, screen):
        if self.active:
            color = GREEN
        elif self.hover:
            color = BLUE
        else:
            color = GRAY

        pygame.draw.rect(screen, color, self.rect, 0)
        pygame.draw.rect(screen, BLACK, self.rect, 2)

        display_text = self.text
        txt_surface = font.render(display_text, True, BLACK)
        screen.blit(txt_surface, (self.rect.x + 5, self.rect.y + 5))


class Button:
    def __init__(self, x, y, w, h, text, action, tooltip_text=None):
        self.rect = pygame.Rect(x, y, w, h)
        self.text = text
        self.action = action
        self.hover = False
        self.tooltip = Tooltip(tooltip_text) if tooltip_text else None

    def handle_event(self, event):
        if event.type == pygame.MOUSEMOTION:
            self.hover = self.rect.collidepoint(event.pos)
            if self.tooltip:
                if self.hover:
                    self.tooltip.show(event.pos)
                else:
                    self.tooltip.hide()
        if event.type == pygame.MOUSEBUTTONDOWN:
            if self.rect.collidepoint(event.pos):
                self.action()

    def draw(self, screen):
        if self.hover:
                color = GREEN
        else:
            color = GRAY

        pygame.draw.rect(screen, color, self.rect)
        pygame.draw.rect(screen, BLACK, self.rect, 2)
        txt = font.render(self.text, True, BLACK)
        screen.blit(txt, (self.rect.centerx - txt.get_width() // 2,
                          self.rect.centery - txt.get_height() // 2))


# Создание элементов интерфейса с подсказками
source_label = Label(40, 20, "Введите имя файла")
source_box = InputBox(40, 40, 260, 34, "",
                      tooltip_text="Введите любое имя файла")

destination_label = Label(40, 80, "Введите имя скопированного файла")
destination_box = InputBox(40, 100, 260, 34, "",
                           tooltip_text="Введите имя для копии файла")

source_label2 = Label(40, 240, "Файл для удаления")
source_box2 = InputBox(40, 260, 560, 34, "", is_file_picker=True,
                       tooltip_text="Нажмите для выбора файла")

source_label3 = Label(40, 400, "Папка для подсчета")
source_box3 = InputBox(40, 420, 560, 34, "", is_folder_picker=True,
                       tooltip_text="Нажмите для выбора папки")

source_label4 = Label(40, 540, "Файл для переименования")
source_box4 = InputBox(40, 560, 560, 34, "", is_file_picker=True,
                       tooltip_text="Нажмите для выбора файла для переименования")

result_text = ""
result_text2 = ""
result_text3 = ""
result_text4 = ""


def copy_action():
    global result_text
    if not source_box.text.strip() or not destination_box.text.strip():
        result_text = "Ошибка: Заполните оба поля"
        return
    try:
        if not os.path.exists(source_box.text):
            result_text = "Ошибка: Файл не найден"
            return
        copy_file(source_box.text, destination_box.text)
        result_text = f"Файл скопирован: {os.path.basename(destination_box.text)}"
    except Exception as ex:
        result_text = f"Ошибка копирования: {str(ex)}"


def delete_action():
    global result_text2
    if not source_box2.text.strip():
        result_text2 = "Ошибка: Выберите файл для удаления"
        return
    try:
        delete_file(source_box2.text)
        result_text2 = f"Файл удален: {os.path.basename(source_box2.text)}"
    except Exception as ex:
        result_text2 = f"Ошибка: {str(ex)}"


def count_action():
    global result_text3
    if not source_box3.text.strip():
        result_text3 = "Ошибка: Выберите папку"
        return
    try:
        total = count_files_in_folder(source_box3.text)
        result_text3 = f"Число файлов: {total}"
    except Exception as ex:
        result_text3 = f"Ошибка: {str(ex)}"


def rename_action():
    global result_text4
    if not source_box4.text.strip():
        result_text4 = "Ошибка: Выберите файл"
        return
    try:
        new_name = rename_file(source_box4.text)
        result_text4 = f"Новое имя: {os.path.basename(new_name)}"
    except Exception as ex:
        result_text4 = f"Ошибка: {str(ex)}"


def result_color(result_text):
    if any(word in result_text for word in ["скопирован", "удален", "файлов", "имя"]):
        color = GREEN
    elif "Ошибка" in result_text:
        color = RED
    else:
        color = BLACK
    return color


# Создание кнопок
copy_btn = Button(40, 140, 150, 40, "Копировать", copy_action,
                  "Скопировать файл с новым именем")
delete_btn = Button(40, 300, 150, 40, "Удалить", delete_action,
                    "Удалить выбранный файл")
count_btn = Button(40, 460, 150, 40, "Посчитать", count_action,
                   "Подсчитать файлы в папке")
rename_btn = Button(40, 600, 150, 40, "Переименовать", rename_action,
                    "Переименовать файл с меткой времени")

clock = pygame.time.Clock()
running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        # Обработка событий всех элементов
        source_box.handle_event(event)
        destination_box.handle_event(event)
        copy_btn.handle_event(event)
        source_box2.handle_event(event)
        delete_btn.handle_event(event)
        source_box3.handle_event(event)
        count_btn.handle_event(event)
        source_box4.handle_event(event)
        rename_btn.handle_event(event)

    screen.fill(WHITE)

    # Заголовки секций
    title = font.render("Копирование файла", True, BLACK)
    screen.blit(title, (5, 3))
    title2 = font.render("Удаление файла", True, BLACK)
    screen.blit(title2, (5, 220))
    title3 = font.render("Подсчет файлов", True, BLACK)
    screen.blit(title3, (5, 380))
    title4 = font.render("Переименование файла", True, BLACK)
    screen.blit(title4, (5, 520))

    # Отрисовка всех элементов
    source_label.draw(screen)
    source_box.draw(screen)
    destination_label.draw(screen)
    destination_box.draw(screen)
    copy_btn.draw(screen)

    source_label2.draw(screen)
    source_box2.draw(screen)
    delete_btn.draw(screen)

    source_label3.draw(screen)
    source_box3.draw(screen)
    count_btn.draw(screen)

    source_label4.draw(screen)
    source_box4.draw(screen)
    rename_btn.draw(screen)

    # Отображение результатов
    color = result_color(result_text)
    status = font.render(result_text, True, color)
    screen.blit(status, (40, 190))

    color = result_color(result_text2)
    status = font.render(result_text2, True, color)
    screen.blit(status, (40, 340))

    color = result_color(result_text3)
    status = font.render(result_text3, True, color)
    screen.blit(status, (40, 500))

    color = result_color(result_text4)
    status = font.render(result_text4, True, color)
    screen.blit(status, (40, 650))

    # Отрисовка tooltips
    for element in [source_box, destination_box, source_box2, source_box3, source_box4,
                    copy_btn, delete_btn, count_btn, rename_btn]:
        if element.tooltip:  # Проверяем, что tooltip существует
            element.tooltip.draw(screen)

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
sys.exit()