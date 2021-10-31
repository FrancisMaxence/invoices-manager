import os
import sys

# Allow user to launch tests in root or tests folders
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

# Change files name for cleanup module (*_[date-us].pdf)
files = ['file1.txt','file2.txt', 'file3.txt']
second_scan = ['file4.txt'] # For TestApp only


def create_files(path):
    for file in files:
        with open(f'{path}/{file}', 'a'):
            pass

def delete_files(path):
    for file in files:
        os.remove(f'{path}/{file}')
