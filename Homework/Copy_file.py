import os

def copy_file(src, dst):
    # Проверяем, существует ли исходный файл
    if not os.path.exists(src):
        print("Файл отсутствует")
        return

    try:
        with open(src, "rb") as f_src:
            data = f_src.read()
        with open(dst, "wb") as f_dst:
            f_dst.write(data)
        print(f"Файл {src} скопирован как {dst}")
    except Exception as e:
        print(f"Ошибка: {e}")
