import unittest
import core

fm = core.FileManager()
data = './data'
archives = f'{data}/archives'
main = f'{data}/main'
scan_ho = f'{data}/scan-ho'
waiting = f'{data}/waiting'

class TestFileManager(unittest.TestCase):
    def test_archives_path(self):
        self.assertEqual(fm.get_archives(), archives)

    def test_main_path(self):
        self.assertEqual(fm.get_main(), main)
    
    def test_scan_ho_path(self):
        self.assertEqual(fm.get_scan_ho(), scan_ho)
    
    def test_waiting_path(self):
        self.assertEqual(fm.get_waiting(), waiting)


if __name__ == '__main__':
    unittest.main()