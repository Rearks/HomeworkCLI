import os

def delete_file(path):
    try:
        os.remove(path)
        print(f"Файл {path} удалён")
    except FileNotFoundError:
        with open(path, "w") as f:
            pass
        print(f"{path} создан, так как файла не было")
        os.remove(path)
        print(f"Файл {path} удалён")
