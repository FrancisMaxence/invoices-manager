import unittest
import core
import paths

fm = core.FileManager()
data = './data'
archives = f'{data}/archives'
main = f'{data}/main'
dev_scan_ho = f'{data}/scan-ho'
prod_scan_ho = '//PC01-LANGELIER/Scan Ho'
waiting = f'{data}/waiting'

class TestFileManager(unittest.TestCase):
    def test_archives_name(self):
        self.assertEqual(fm.get_archives(), archives)

    def test_main_name(self):
        self.assertEqual(fm.get_main(), main)
    
    def test_scan_ho_name(self):
        if paths.is_dev:
            self.assertEqual(fm.get_scan_ho(), dev_scan_ho)
        else:
            self.assertEqual(fm.get_scan_ho(), prod_scan_ho)
    
    def test_waiting_name(self):
        self.assertEqual(fm.get_waiting(), waiting)


if __name__ == '__main__':
    unittest.main()