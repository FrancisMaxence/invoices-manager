import os
import unittest

from filemanager import FileManager

fm = FileManager()
data = './data'
archives = f'{data}/archives'
main = f'{data}/main'
scan_ho = f'{data}/scan-ho'
waiting = f'{data}/waiting'
files = ['file1.txt','file2.txt', 'file3.txt']


class TestFileManager(unittest.TestCase):
    def test_archives_path(self):
        self.assertEqual(fm.get_archives(), archives)

    def test_main_path(self):
        self.assertEqual(fm.get_main(), main)
    
    def test_scan_ho_path(self):
        self.assertEqual(fm.get_scan_ho(), scan_ho)
    
    def test_waiting_path(self):
        self.assertEqual(fm.get_waiting(), waiting)
    
    def test_duplicate_file(self):
        for file in files:
            with open(f'{main}/{file}', 'a'):
                pass
                
        fm.duplicate_file()

        self.assertEqual(os.listdir(scan_ho), files)
        self.assertEqual(os.listdir(waiting), files)

        for file in files:
            os.remove(f'{scan_ho}/{file}')
            os.remove(f'{waiting}/{file}')
        

    def test_archive_files(self):
        for file in files:
            with open(f'{waiting}/{file}', 'a'):
                pass
        
        fm.archive_files()

        self.assertEqual(os.listdir(archives), files)

        for file in files:
            os.remove(f'{archives}/{file}')


if __name__ == '__main__':
    unittest.main()
   