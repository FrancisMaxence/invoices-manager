# import testsetup
# use Setup() to initialize test ?

import unittest

class TestCompareDirectories(unittest.TestCase):
    def test_waiting_and_scan_ho_empty(self):
        # Nothing in the two folders
        pass

    def test_waiting_greater_than_scan_ho(self):
        # Waiting folder have still files, Scan Ho folder is empty
        pass

    def test_waiting_and_scan_ho_equal(self):
        # Waiting folder and Scan Ho folder have the same files
        pass

    def test_waiting_less_than_scan_ho(self):
        # Waiting directory is empty but not Scan Ho directory
        pass
