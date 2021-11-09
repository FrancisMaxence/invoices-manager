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

files = ['file1_2020-12-25_102033568.txt','file2_2021-11-09_161545123.txt', 'file3_2021-08-12_085942816.txt']
second_scan = ['file4_2021-03-29_045113946.txt'] # For TestApp only


def create_files(path):
    for file in files:
        with open(f'{path}/{file}', 'a'):
            pass

def delete_files(path):
    for file in os.listdir(path):
        os.remove(f'{path}/{file}')
