import unittest
import os

import testsetup as ts
from core.comparefolders import compare_folders

class TestCompareFolders(unittest.TestCase):
    def test_waiting_and_scan_ho_empty(self):
        """
        Waiting folder and Scan Ho are empty -> duplicate_files()
        """
        ts.create_files(ts.main)
        compare_folders()

        self.assertListEqual(os.listdir(ts.main), [])
        self.assertListEqual(os.listdir(ts.waiting), ts.files)
        self.assertListEqual(os.listdir(ts.scan_ho), ts.files)
        self.assertListEqual(os.listdir(ts.archives), [])

        ts.delete_files(ts.waiting)
        ts.delete_files(ts.scan_ho)

    def test_waiting_greater_than_scan_ho(self):
        """
        Waiting folder have still files, Scan Ho folder is empty -> archive_files() then duplicate_files()
        """
        ts.create_files(ts.main)
        ts.create_files(ts.waiting)
        compare_folders()

        self.assertListEqual(os.listdir(ts.main), [])
        self.assertListEqual(os.listdir(ts.waiting), ts.files) 
        self.assertListEqual(os.listdir(ts.scan_ho), ts.files)
        self.assertListEqual(os.listdir(ts.archives), ts.files)
        
        ts.delete_files(ts.archives)
        ts.delete_files(ts.scan_ho)
        ts.delete_files(ts.waiting)

    def test_waiting_and_scan_ho_equal(self):
        """
        Waiting folder and Scan Ho folder have the same files -> pass
        """
        ts.create_files(ts.main)
        ts.create_files(ts.scan_ho)
        ts.create_files(ts.waiting)

        compare_folders()

        self.assertListEqual(os.listdir(ts.main), ts.files)
        self.assertListEqual(os.listdir(ts.waiting), ts.files)
        self.assertListEqual(os.listdir(ts.scan_ho), ts.files)
        self.assertListEqual(os.listdir(ts.archives), [])

        ts.delete_files(ts.main)
        ts.delete_files(ts.scan_ho)
        ts.delete_files(ts.waiting)

    def test_waiting_less_than_scan_ho(self):
        """
        Waiting directory is empty but not Scan Ho directory -> pass
        """
        ts.create_files(ts.main)
        ts.create_files(ts.scan_ho)

        compare_folders()
        
        self.assertListEqual(os.listdir(ts.main), ts.files)
        self.assertListEqual(os.listdir(ts.waiting), [])
        self.assertListEqual(os.listdir(ts.scan_ho), ts.files)
        self.assertListEqual(os.listdir(ts.archives), [])

        ts.delete_files(ts.main)
        ts.delete_files(ts.scan_ho)

if __name__ == '__main__':
    unittest.main(verbosity=2)
