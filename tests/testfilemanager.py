import os
import unittest

from testsetup import *

class TestFileManager(unittest.TestCase):
    def test_duplicate_file(self):
        # Setup
        create_files(main)
        fm.duplicate_file()

        # Test
        self.assertEqual(os.listdir(scan_ho), files)
        self.assertEqual(os.listdir(waiting), files)

        # Teardown
        delete_files(scan_ho)
        delete_files(waiting)
        

    def test_archive_files(self):
        # Setup
        create_files(waiting)
        fm.archive_files()

        # Test
        self.assertEqual(os.listdir(archives), files)

        # Teardown
        delete_files(archives)


if __name__ == '__main__':
    unittest.main(verbosity=2)
   