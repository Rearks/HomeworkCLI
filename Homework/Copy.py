def copy_file(source, destination):
    with open(source, "rb") as src:
        data = src.read()

    with open(destination, "wb") as dst:
        dst.write(data)

    return f"Файл скопирован из {source} в {destination}"
