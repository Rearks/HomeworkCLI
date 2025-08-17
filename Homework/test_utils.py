import unittest
import os
import datetime
from .Copy_file import copy_file
from .Delete_file import delete_file
from .Count_files import count_files_in_folder
from .Rename_file import rename_file


class TestUtils(unittest.TestCase):
    def test_copy_file(self):
        with open("test1.txt", "w") as f:
            pass

        copy_file("test1.txt", "copy.txt")

        self.assertTrue(os.path.exists("copy.txt"))

        os.remove("test1.txt")
        os.remove("copy.txt")

    def test_delete_file(self):
        with open("test2.txt", "w") as f:
            pass

        delete_file("test2.txt")
        self.assertFalse(os.path.exists("test2.txt"))

    def test_count_files(self):
        os.makedirs("testdir")
        with open("testdir/1.txt", "w") as f:
            pass
        with open("testdir/2.txt", "w") as f:
            pass

        count = count_files_in_folder("testdir")
        self.assertEqual(count, 2)
        os.remove("testdir/1.txt")
        os.remove("testdir/2.txt")
        os.rmdir("testdir")

    def test_rename_file(self):
        with open("test3.txt", "w") as f:
            pass
        ctime = os.path.getctime("test3.txt")
        rename_file("test3.txt")

        date_str = datetime.datetime.fromtimestamp(ctime).strftime("%Y-%m-%d")
        new_name = f"test3_{date_str}.txt"

        self.assertTrue(os.path.exists(new_name))
        self.assertFalse(os.path.exists("test3.txt"))
        os.remove(new_name)


if __name__ == "__main__":
    unittest.main()