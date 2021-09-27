import os
import shutil
import time

# Custom modules for tests
import paths

class File_manager:
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
        main_list = os.listdir(paths.main)
        main_length = len(main_list)
        
        for i in range(main_length):
            shutil.copy(f'{self.main}/{main_list[i-1]}', f'{self.scan_ho}')
            shutil.move(f'{self.main}/{main_list[i-1]}', f'{self.waiting}')
    
    
    def archive_files(self):
        waiting_list = os.listdir(self.waiting)
        scan_ho_list = os.listdir(self.scan_ho)
        waiting_length = len(waiting_list)

        if waiting_list != scan_ho_list:
            for i in range(waiting_length):
                shutil.move(f'{self.waiting}/{waiting_list[i-1]}', f'{self.archives}')

            self.duplicate_file()

    def testing_file_move(self):
        self.duplicate_file()

        time.sleep(3)

        waiting_list = os.listdir(self.waiting)
        scan_ho_list = os.listdir(self.scan_ho)
        waiting_length = len(waiting_list)

        for i in range(waiting_length):
            shutil.move(f'{self.waiting}/{waiting_list[i-1]}', f'{self.main}')
            os.remove(f'{self.scan_ho}/{scan_ho_list[i-1]}')




if __name__ == '__main__':
    a = File_manager()
    a.testing_file_move()
