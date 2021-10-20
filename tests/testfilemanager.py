import os
import unittest

from testsetup import *

class TestFileManager(unittest.TestCase):
    # Try setup() to use testsetup.py

    def test_duplicate_file(self):
        # Setup
        for file in files:
            with open(f'{main}/{file}', 'a'):
                pass
                
        fm.duplicate_file()

        # Test
        self.assertEqual(os.listdir(scan_ho), files)
        self.assertEqual(os.listdir(waiting), files)

        # Teardown
        for file in files:
            os.remove(f'{scan_ho}/{file}')
            os.remove(f'{waiting}/{file}')
        

    def test_archive_files(self):
        # Setup
        for file in files:
            with open(f'{waiting}/{file}', 'a'):
                pass
        
        fm.archive_files()

        # Test
        self.assertEqual(os.listdir(archives), files)

        # Teardown
        for file in files:
            os.remove(f'{archives}/{file}')


if __name__ == '__main__':
    unittest.main(verbosity=2)
   