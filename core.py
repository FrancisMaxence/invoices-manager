import os
import shutil
import time

# Custom modules for tests
import paths

class FileManager:
    def __init__(self):
        self.archives = paths.archives
        self.main = paths.main
        self.scan_ho = paths.scan_ho
        self.waiting = paths.waiting

    """ 
    Getters
    """
    def get_archives(self):
        return self.archives

    def get_main(self):
        return self.main
    
    def get_scan_ho(self):
        return self.scan_ho
    
    def get_waiting(self):
        return self.waiting
    

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
        scan_ho_files = os.listdir(self.scan_ho)

        if len(waiting_files) == 0 and len(scan_ho_files) == 0:
            #self.testing_file_move()
            
            self.duplicate_file()
        elif len(waiting_files) == 0 and len(scan_ho_files) > 0:
            #self.testing_file_move()
            
            self.duplicate_file()
        elif waiting_files != scan_ho_files:
            for waiting_file in waiting_files:
                shutil.move(f'{self.waiting}/{waiting_file}', f'{self.archives}')
            
            #time.sleep(3)
            #self.testing_file_move()
            
            self.duplicate_file()

    def testing_file_move(self):
        self.duplicate_file()

        time.sleep(3)

        waiting_files = os.listdir(self.waiting)
        scan_ho_files = os.listdir(self.scan_ho)

        for waiting_file in waiting_files:
            shutil.move(f'{self.waiting}/{waiting_file}', f'{self.main}')
        
        for scan_ho_file in scan_ho_files:
            os.remove(f'{self.scan_ho}/{scan_ho_file}')




if __name__ == '__main__':
    a = FileManager()
    a.testing_file_move()
