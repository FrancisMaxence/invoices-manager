import unittest
import core
import paths

fm = core.FileManager()

class TestFileManager(unittest.TestCase):
    def test_archives_name(self):
        self.assertEqual(fm.get_archives(), './data/archives')

    def test_main_name(self):
        self.assertEqual(fm.get_main(), './data/main')
    
    def test_scan_ho_name(self):
        if paths.is_dev:
            self.assertEqual(fm.get_scan_ho(), './data/scan-ho')
        else:
            self.assertEqual(fm.get_scan_ho(), '//PC01-LANGELIER/Scan Ho')
    
    def test_waiting_name(self):
        self.assertEqual(fm.get_waiting(), './data/waiting')


if __name__ == '__main__':
    unittest.main()