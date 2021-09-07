# python modules
from os import remove
from shutil import copy, move
from time import sleep

# custom modules
from paths import src, scan_ho

test_file = 'hello-world.txt' # The test file

copy(f'{src}/{test_file}', f'{scan_ho}') # copy original file to Head Office repository
move(f'{src}/{test_file}', f'{src}/archives') # Move original file to ./archives


# Only for testing. Comments those lines when API is ready for production
sleep(3)

move(f'{src}/archives/{test_file}', f'{src}/{test_file}')
remove(f'{scan_ho}/{test_file}')
