import unittest
import os

import testsetup as ts
from core.comparefolders import compare_folders

class TestCompareFolders(unittest.TestCase):
    def test_waiting_and_scan_ho_empty(self):
        compare_folders()
        self.assertEqual(len(os.listdir(ts.main)), 0)
        self.assertListEqual(os.listdir(ts.waiting), os.listdir(ts.scan_ho))
        self.assertEqual(len(os.listdir(ts.archives)), 0)

    def test_waiting_greater_than_scan_ho(self):
        # Waiting folder have still files, Scan Ho folder is empty
        pass

    def test_waiting_and_scan_ho_equal(self):
        # Waiting folder and Scan Ho folder have the same files
        pass

    def test_waiting_less_than_scan_ho(self):
        # Waiting directory is empty but not Scan Ho directory
        pass

if __name__ == '__main__':
    unittest.main(verbosity=2)