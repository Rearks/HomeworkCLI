import os

def delete_file(path):
    os.remove(path)
    print(f"Файл {path} удалён")
