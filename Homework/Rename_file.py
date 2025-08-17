import os
import datetime

def rename_file(filename):

    ctime = os.path.getctime(filename)
    date_str = datetime.datetime.fromtimestamp(ctime).strftime("%Y-%m-%d")

    name, ext = os.path.splitext(filename)
    new_name = f"{name}_{date_str}{ext}"


    os.rename(filename, new_name)
    print(f"Файл {filename} переименован в {new_name}")