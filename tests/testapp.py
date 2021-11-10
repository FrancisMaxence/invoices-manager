import unittest
import os

import testsetup as ts
from core.comparefolders import compare_folders

class TestApp(unittest.TestCase):
    def test_head_office_has_received_invoices(self):
        """
        Simple scenario
        """
        ts.create_files(ts.main)
        # first duplication
        compare_folders()

        self.assertListEqual(os.listdir(ts.main), [])
        self.assertListEqual(os.listdir(ts.waiting), ts.files)
        self.assertListEqual(os.listdir(ts.scan_ho), ts.files)
        self.assertListEqual(os.listdir(ts.archives), [])

        # Head office takes invoices
        ts.delete_files(ts.scan_ho)
        compare_folders()

        self.assertListEqual(os.listdir(ts.main), [])
        self.assertListEqual(os.listdir(ts.waiting), [])
        self.assertListEqual(os.listdir(ts.scan_ho), [])
        self.assertListEqual(os.listdir(ts.archives), ts.files)

        ts.delete_files(ts.archives)

    
    def test_head_office_has_not_received_invoices_yet(self):
        """
        Complex scenario
        """
        ts.create_files(ts.main)
        # first duplication
        compare_folders()

        self.assertListEqual(os.listdir(ts.main), [])
        self.assertListEqual(os.listdir(ts.waiting), ts.files)
        self.assertListEqual(os.listdir(ts.scan_ho), ts.files)
        self.assertListEqual(os.listdir(ts.archives), [])
    
        # Receptionner scan a new invoice, Head Office don't took the former invoices
        for file in ts.second_scan:
            with open(f'{ts.main}/{file}', 'a'):
                pass
    
        compare_folders()

        self.assertListEqual(os.listdir(ts.main), ts.second_scan)
        self.assertListEqual(os.listdir(ts.waiting), ts.files)
        self.assertListEqual(os.listdir(ts.scan_ho), ts.files)
        self.assertListEqual(os.listdir(ts.archives), [])

        # Finally, Head Office took the invoices
        ts.delete_files(ts.scan_ho)
        compare_folders()

        self.assertListEqual(os.listdir(ts.main), [])
        self.assertListEqual(os.listdir(ts.waiting), ts.second_scan)
        self.assertListEqual(os.listdir(ts.scan_ho), ts.second_scan)
        self.assertListEqual(os.listdir(ts.archives), ts.files)

        # Head office took the next invoices
        os.remove(f'{ts.scan_ho}/{ts.second_scan[0]}')
        compare_folders()

        self.assertListEqual(os.listdir(ts.main), [])
        self.assertListEqual(os.listdir(ts.waiting), [])
        self.assertListEqual(os.listdir(ts.scan_ho), [])
        self.assertListEqual(os.listdir(ts.archives), ts.files + ts.second_scan)

        ts.delete_files(ts.archives)
    
    def test_head_office_striking(self):
        counter = 0
        ts.create_files(ts.scan_ho)
        ts.create_files(ts.waiting)

        while counter < 5:
            counter += compare_folders()
            self.assertEqual(os.listdir(ts.scan_ho), os.listdir(ts.waiting))

        if counter == 5:
            print('\033[1;31;40m Is there someone at the Head Office ? \033[1;37;40m')
            counter = 0
        
        ts.delete_files(ts.scan_ho)
        ts.delete_files(ts.waiting)
   

if __name__ == '__main__':
    unittest.main(verbosity=2)