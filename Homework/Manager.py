import argparse
from .Copy import copy_file
from .Delete import delete_file
from .Count import count_files_in_folder
from .Rename import rename_file

def main():
    parser = argparse.ArgumentParser(description="Простой файловый менеджер")

    subparsers = parser.add_subparsers(dest="command")

    # Копирование файла
    copy_parser = subparsers.add_parser("copy")
    copy_parser.add_argument("source")
    copy_parser.add_argument("destination")

    # Удаление файла
    delete_parser = subparsers.add_parser("delete")
    delete_parser.add_argument("path")

    # Подсчёт файлов
    count_parser = subparsers.add_parser("count")
    count_parser.add_argument("folder")

    # Переименование с датой
    rename_parser = subparsers.add_parser("rename")
    rename_parser.add_argument("filename")

    args = parser.parse_args()

    if args.command == "copy":
        print(copy_file(args.source, args.destination))

    elif args.command == "delete":
        delete_file(args.path)

    elif args.command == "count":
        print(count_files_in_folder(args.folder))

    elif args.command == "rename":
        rename_file(args.filename)


if __name__ == "__main__":
    main()