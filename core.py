import os
import shutil
import time

# Custom modules for tests
import paths
import utils

class File_manager:
    def __init__(self, src, dest, files=False):
        self.src = src
        self.dest = dest
        self.waiting = paths.waiting
        self.files = os.listdir(self.src)
        self.files_length = len(self.files)
        

    """ 
    Getters
    """
    def get_src(self):
        return self.src
    
    def get_dest(self):
        return self.dest
    
    def get_files(self):
        return self.files
    
    def get_waiting(self):
        return self.waiting

    def get_files_length(self):
        return self.files_length
    

    """
    Methods
    """
    def copy_file(self):
        for i in range(self.files_length):
            shutil.copy(f'{self.src}/{self.files[i-1]}', f'{self.dest}')
    
    def move_file(self):
        for i in range(self.files_length):
            shutil.move(f'{self.src}/{self.files[i-1]}', f'{self.waiting}')
    
    def duplicate_file(self):
        self.copy_file()
        self.move_file()

    def testing_file_move(self):
        self.duplicate_file()

        time.sleep(3)

        for i in range(self.files_length):
            shutil.move(f'{self.waiting}/{self.files[i-1]}', f'{self.src}')
            os.remove(f'{self.dest}/{self.files[i-1]}')




if __name__ == '__main__':
    a = File_manager(paths.src, paths.scan_ho, utils.test_files)
    a.testing_file_move()
