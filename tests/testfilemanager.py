import os
import unittest

# move to testsetup.py
import sys

# Allow user to launch tests in root or tests directory
if 'tests' not in os.getcwd():
    sys.path.insert(1, os.getcwd())
    data = './data'
else:
    sys.path.insert(1, os.path.dirname(os.getcwd()))
    data = '../data'

from core.filemanager import FileManager

fm = FileManager()
archives = f'{data}/archives'
main = f'{data}/main'
scan_ho = f'{data}/scan-ho'
waiting = f'{data}/waiting'
files = ['file1.txt','file2.txt', 'file3.txt']
# import testsetup.py

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
   