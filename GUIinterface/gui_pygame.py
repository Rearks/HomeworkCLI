import sys
import os
import pygame
import tkinter as tk
from tkinter import filedialog
from Homework.Copy_file import copy_file
from Homework.Delete_file import delete_file
from Homework.Count_files import count_files_in_folder
from Homework.Rename_file import rename_file

pygame.init()

WIDTH, HEIGHT = 640, 700
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Менеджер файлов")

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GRAY  = (210, 210, 210)
BLUE  = (80, 140, 250)
GREEN = (0, 160, 60)
RED   = (200, 40, 40)
font  = pygame.font.SysFont("Arial", 18)

class Label:
    def __init__(self, x, y, text):
        self.text = text
        self.pos = (x, y)

    def draw(self, surf):
        txt = font.render(self.text, True, BLACK)
        surf.blit(txt, self.pos)
        surf.blit(txt, self.pos)

class InputBox:
    def __init__(self, x, y, w, h, text='', is_folder_picker=False, is_file_picker=False):
        self.rect = pygame.Rect(x, y, w, h)
        self.color = GRAY
        self.text = text
        self.txt_surface = font.render(self.text, True, BLACK)
        self.active = False
        self.hover = False
        self.is_folder_picker = is_folder_picker
        self.is_file_picker = is_file_picker

    def handle_event(self, event):
        if event.type == pygame.MOUSEMOTION:
            self.hover = self.rect.collidepoint(event.pos)
        if event.type == pygame.MOUSEBUTTONDOWN:
            if self.rect.collidepoint(event.pos):
                if self.is_folder_picker:
                    root = tk.Tk()
                    root.withdraw()
                    folder = filedialog.askdirectory()
                    if folder:
                        self.text = folder
                        self.txt_surface = font.render(self.text, True, BLACK)
                    root.destroy()

                if self.is_file_picker:
                    root = tk.Tk()
                    root.withdraw()
                    file = filedialog.askopenfilename()
                    if file:
                        self.text = file
                        self.txt_surface = font.render(self.text, True, BLACK)
                    root.destroy()
                else:
                    self.active = True
            else:
                self.active = False

        if event.type == pygame.KEYDOWN and self.active:
            if event.key == pygame.K_RETURN:
                print(self.text)
                self.text = ''
            elif event.key == pygame.K_BACKSPACE:
                self.text = self.text[:-1]
            else:
                self.text += event.unicode
            self.txt_surface = font.render(self.text, True, BLACK)

    def draw(self, screen):
        if self.active:
            color = (0, 200, 0)
        elif self.hover:
            color = (180, 180, 180)
        else:
            color = GRAY
        pygame.draw.rect(screen, color, self.rect, 0)
        pygame.draw.rect(screen, BLACK, self.rect, 2)
        screen.blit(self.txt_surface, (self.rect.x + 5, self.rect.y + 5))
        screen.blit(self.txt_surface, (self.rect.x + 5, self.rect.y + 5))

    def choose_folder():
        root = tk.Tk()
        root.withdraw()
        folder = filedialog.askdirectory()
        if folder:
            source_box3.text = folder
            source_box3.txt_surface = font.render(source_box3.text, True, BLACK)
        return folder

    def choose_file():
        root = tk.Tk()
        root.withdraw()
        file = filedialog.askopenfilename()
        if file:
            source_box4.text = file
            source_box4.txt_surface = font.render(source_box4.text, True, BLACK)
        return file

class Button:
    def __init__(self, x, y, w, h, text, action):
        self.rect = pygame.Rect(x, y, w, h)
        self.text = text
        self.action = action
        self.hover = False

    def handle_event(self, event):
        if event.type == pygame.MOUSEMOTION:
            self.hover = self.rect.collidepoint(event.pos)

        if event.type == pygame.MOUSEBUTTONDOWN:
            if self.rect.collidepoint(event.pos):
                self.action()

    def draw(self, surf):
        if self.hover:
            color = (180, 180, 180)
        else:
            color = (150, 150, 150)

        pygame.draw.rect(surf, color, self.rect)
        txt = font.render(self.text, True, BLACK)
        surf.blit(txt, (self.rect.centerx - txt.get_width() // 2,
                        self.rect.centery - txt.get_height() // 2))


# Создание элементов интерфейса
source_label = Label(40, 20, "Введите имя файла")
source_box = InputBox(40, 40, 260, 34, "")

destination_label = Label(40, 80, "Введите имя скопированного файла")
destination_box = InputBox(40, 100, 260, 34, "")

source_label2 = Label(40, 240, "Файл для удаления")
source_box2 = InputBox(40, 260, 560, 34, "", is_file_picker=True)

source_label3 = Label(40, 400, "Папка для подсчета")
source_box3 = InputBox(40, 420, 560, 34, "", is_folder_picker=True)

source_label4 = Label(40, 540, "Файл для переименования")
source_box4 = InputBox(40, 560, 560, 34, "", is_file_picker=True)

result_text = ""
result_text2 = ""
result_text3 = ""
result_text4 = ""

def copy_action():
    global result_text
    try:
        copy_file(source_box.text, destination_box.text)
        result_text = f"Файл скопирован в {destination_box.text}"
    except Exception as ex:
        result_text = f"Ошибка: {ex}"

copy_btn = Button(40, 140, 150, 40, "Копировать", copy_action)

def delete_action():
    global result_text2
    try:
        delete_file(source_box2.text)
        result_text2 = f"Файл удален: {os.path.basename(source_box2.text)}"
    except Exception as ex:
        result_text2 = f"Ошибка: {ex}"

delete_btn = Button(40, 300, 150, 40, "Удалить", delete_action)

def count_action():
    global result_text3
    try:
        count_files_in_folder(source_box3.text)
        total = count_files_in_folder(source_box3.text)
        result_text3 = f"Число файлов: {total}"
    except Exception as ex:
        result_text3 = f"Ошибка: {ex}"

count_btn = Button(40, 460, 150, 40, "Посчитать", count_action)

def rename_action():
    global result_text4
    try:
        new_name = rename_file(source_box4.text)
        result_text4 = f"Новое имя: {os.path.basename(new_name)}"
    except Exception as ex:
        result_text4 = f"Ошибка: {ex}"

rename_btn = Button(40, 600, 150, 40, "Переименовать", rename_action)

clock = pygame.time.Clock()
running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False


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

    title = font.render("Копирование файла", True, BLACK)
    screen.blit(title, (5, 3))
    title2 = font.render("Удаление файла", True, BLACK)
    screen.blit(title2, (5, 220))
    title3 = font.render("Подсчет файлов", True, BLACK)
    screen.blit(title3, (5, 380))
    title4 = font.render("Переименование файла", True, BLACK)
    screen.blit(title4, (5, 520))

    source_label.draw(screen)
    source_box.draw(screen)

    source_label2.draw(screen)
    source_box2.draw(screen)

    source_label3.draw(screen)
    source_box3.draw(screen)

    source_label4.draw(screen)
    source_box4.draw(screen)

    destination_label.draw(screen)
    destination_box.draw(screen)

    copy_btn.draw(screen)
    delete_btn.draw(screen)
    count_btn.draw(screen)
    rename_btn.draw(screen)

    # Отображение результата
    color = GREEN if "скопирован" in result_text else (RED if "Ошибка" in result_text else BLACK)
    status = font.render(result_text, True, color)
    screen.blit(status, (40, 190))
    color2 = GREEN if "удален" in result_text2 else (RED if "Ошибка" in result_text2 else BLACK)
    status2 = font.render(result_text2, True, color2)
    screen.blit(status2, (40, 340))
    color3 = GREEN if "файлов" in result_text3 else (RED if "Ошибка" in result_text3 else BLACK)
    status3 = font.render(result_text3, True, color3)
    screen.blit(status3, (40, 500))
    color4 = GREEN if "имя" in result_text4 else (RED if "Ошибка" in result_text4 else BLACK)
    status4 = font.render(result_text4, True, color4)
    screen.blit(status4, (40, 650))

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
sys.exit()