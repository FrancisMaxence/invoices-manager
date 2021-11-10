import os
import unittest
from datetime import datetime

import testsetup as ts
from core.filemanager import FileManager

fm = FileManager()

class TestFileManager(unittest.TestCase):
    def test_duplicate_file(self):
        """
        Duplicate files from main folder to Scan Ho and Waiting folders
        """
        ts.create_files(ts.main)
        fm.duplicate_file()

        self.assertListEqual(os.listdir(ts.main), [])
        self.assertListEqual(os.listdir(ts.scan_ho), ts.files)
        self.assertListEqual(os.listdir(ts.waiting), ts.files)
        self.assertListEqual(os.listdir(ts.archives), [])

        ts.delete_files(ts.scan_ho)
        ts.delete_files(ts.waiting)
        

    def test_archive_files(self):
        """
        Move files from waiting folder to archives folder
        """
        ts.create_files(ts.waiting)
        fm.archive_files()

        self.assertListEqual(os.listdir(ts.main), [])
        self.assertListEqual(os.listdir(ts.scan_ho), [])
        self.assertListEqual(os.listdir(ts.waiting), [])
        self.assertEqual(os.listdir(ts.archives), ts.files)

        ts.delete_files(ts.archives)
    
    def test_invoices_cleaner(self):
        # Pass date in 1st argument of invoices_cleaner for passing tests
        today_test = datetime(2021,11,9)
        ts.create_files(ts.archives, ts.files + ts.second_scan)

        fm.invoices_cleaner(today_test)
        ts.files.pop(0)
        
        self.assertEqual(os.listdir(ts.archives), ts.files)

        ts.delete_files(ts.archives)


if __name__ == '__main__':
    unittest.main(verbosity=2)
   