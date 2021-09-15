import os
import shutil
import time

# Custom modules for tests
import paths
import utils

class File_manager:
    def __init__(self, src, dest, files):
        self.src = src
        self.dest = dest
        self.files = files
        self.waiting = self.src + "/waiting"

    def get_src(self):
        return self.src
    
    def get_dest(self):
        return self.dest
    
    def get_files(self):
        return self.files
    
    def get_waiting(self):
        return self.waiting
    
    def copy_file(self):
        shutil.copy(f'{self.src}/{self.files}', f'{self.dest}')
    
    def move_file(self):
        shutil.move(f'{self.src}/{self.files}', f'{self.waiting}')
    
    def duplicate_file(self):
        self.copy_file()
        self.move_file()

    def testing_file_move(self):
        self.duplicate_file()

        time.sleep(3)
        shutil.move(f'{self.waiting}/{self.files}', f'{self.src}/{self.files}')
        os.remove(f'{self.dest}/{self.files}')




if __name__ == '__main__':
    a = File_manager(paths.src, paths.scan_ho, utils.test_file)
    a.testing_file_move()
