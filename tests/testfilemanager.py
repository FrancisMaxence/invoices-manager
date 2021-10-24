import os
import unittest

import testsetup as ts
from core.filemanager import FileManager

fm = FileManager()

class TestFileManager(unittest.TestCase):
    def test_duplicate_file(self):
        # Setup
        ts.create_files(ts.main)
        fm.duplicate_file()

        # Test
        self.assertEqual(os.listdir(ts.scan_ho), ts.files)
        self.assertEqual(os.listdir(ts.waiting), ts.files)

        # Teardown
        ts.delete_files(ts.scan_ho)
        ts.delete_files(ts.waiting)
        

    def test_archive_files(self):
        # Setup
        ts.create_files(ts.waiting)
        fm.archive_files()

        # Test
        self.assertEqual(os.listdir(ts.archives), ts.files)

        # Teardown
        ts.delete_files(ts.archives)


if __name__ == '__main__':
    unittest.main(verbosity=2)
   