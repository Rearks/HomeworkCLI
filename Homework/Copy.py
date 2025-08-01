def copy_file(source, destination):
    file1 = open(source, "rb")
    data = file1.read()
    file1.close()

    file2 = open(destination, "wb")
    file2.write(data)
    file2.close()
    return f"Файл скопирован из {source} в {destination}"

