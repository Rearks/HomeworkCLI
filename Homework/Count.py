import os

def count_files_in_folder(folder):
    total = 0
    for root, dirs, files in os.walk(folder):
        total += len(files)
    return total
