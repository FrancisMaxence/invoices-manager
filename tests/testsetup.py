import os
import sys

from core.filemanager import FileManager

fm = FileManager()

# Allow user to launch tests in root or tests directory
if 'tests' not in os.getcwd():
    sys.path.insert(1, os.getcwd())
    data = './data'
else:
    sys.path.insert(1, os.path.dirname(os.getcwd()))
    data = '../data'

archives = f'{data}/archives'
main = f'{data}/main'
scan_ho = f'{data}/scan-ho'
waiting = f'{data}/waiting'
files = ['file1.txt','file2.txt', 'file3.txt']
