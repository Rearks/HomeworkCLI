import os


def copy_file(source, destination):
    try:
        file1 = open(source, "rb")
        data = file1.read()
        file1.close()

        file2 = open(destination, "wb")
        file2.write(data)
        file2.close()
        return f"Файл скопирован из {source} в {destination}"

    except FileNotFoundError:
        with open(source, "w") as f:
            pass
        print(f"{source} не найден, поэтому был создан пустой файл")
        return copy_file(source, destination)

