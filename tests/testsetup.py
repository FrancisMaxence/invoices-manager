import os
import sys

# Allow user to launch tests in root or tests directory
if 'tests' not in os.getcwd():
    sys.path.insert(1, os.getcwd())
    data = './data'
else:
    sys.path.insert(1, os.path.dirname(os.getcwd()))
    data = '../data'

# Must be importing AFTER sys.path.insert()
from core.filemanager import FileManager

fm = FileManager()

archives = f'{data}/archives'
main = f'{data}/main'
scan_ho = f'{data}/scan-ho'
waiting = f'{data}/waiting'
files = ['file1.txt','file2.txt', 'file3.txt']


def create_files(path):
    for file in files:
        with open(f'{path}/{file}', 'a'):
            pass

def delete_files(path):
    for file in files:
        os.remove(f'{path}/{file}')
