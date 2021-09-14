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
    
    def copy_file(self):
        shutil.copy(f'{self.src}/{self.files}', f'{self.dest}')
    
    def move_file(self):
        shutil.move(f'{self.src}/{self.files}', f'{self.src}/archives')
    
    def duplicate_file(self):
        self.copy_file()
        self.move_file()

    def testing_file_move(self):
        self.duplicate_file()

        time.sleep(3)
        shutil.move(f'{self.src}/archives/{self.files}', f'{self.src}/{self.files}')
        os.remove(f'{self.dest}/{self.files}')




if __name__ == '__main__':
    a = File_manager(paths.src, paths.fake_scan_ho, utils.test_file)
    a.testing_file_move()
