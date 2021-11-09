import os
import shutil
import datetime

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
    
    def invoices_cleaner(self):
        archives_files = os.listdir(self.archives)
        today = datetime.datetime.now() # <class 'datetime.datetime(YYYY, MMMM, DD, HH, MM, SS, mmmmmm)'>
        # 6 months = 183 days

        for file in archives_files:
            file_date = file.split('_')
            # join file_date[1] with file_date[2] -> strptime("%Y%m%d%H%"m"%s%ms") (Find code for minutes and milliseconds)
            # file_date - today >= 183 day => remove file
