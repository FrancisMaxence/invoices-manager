import os
import shutil

from datetime import datetime

import utils.paths as paths

class FileManager:
    def __init__(self):
        self.archives = paths.archives
        self.main = paths.main
        self.scan_ho = paths.scan_ho
        self.waiting = paths.waiting

    """
    Methods
    """
    def duplicate_file(self):
        main_files = os.listdir(paths.main)
        
        for main_file in main_files:
            shutil.copy(f'{self.main}/{main_file}', f'{self.scan_ho}')
            shutil.move(f'{self.main}/{main_file}', f'{self.waiting}')
    
    
    def archive_files(self):
        waiting_files = os.listdir(self.waiting)

        for waiting_file in waiting_files:
            shutil.move(f'{self.waiting}/{waiting_file}', f'{self.archives}')
    
    def invoices_cleaner(self, today=datetime.now()):
        archives_files = os.listdir(self.archives)
        #today = datetime.now() # <class 'datetime.datetime(YYYY, MMMM, DD, HH, MM, SS, mmmmmm)'>

        for file in archives_files:
            # Convert file name in datetime object
            file_datetime = file.split('_')
            file_date = datetime.strptime(file_datetime[1] + file_datetime[2][:-4], "%Y-%m-%d%H%M%S%f")
            
            # Remove file if date is over 6 months
            if (today - file_date).days > 183:
                os.remove(f'{self.archives}/{file}')
