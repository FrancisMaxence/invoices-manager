import shutil, os
from time import sleep

# Replace Main and Archives by invoices/factures and archives

src = './directory-testing' # Replace by /Desktop (find absolute path) in production mode
# Create production and distribution file
# Find a way to switch between paths easily
scan_ho = '//PC01-LANGELIER/Scan Ho' # The Head Office repository dist
test_file = 'hello-world.txt' # The test file

shutil.copy(f'{src}/Main/{test_file}', f'{scan_ho}') # copy original file to Head Office repository
shutil.move(f'{src}/Main/{test_file}', f'{src}/Main/Archives') # Move original file to ./Archives


# Only for testing. Comments those lines when API is ready for production
sleep(3)

os.remove(f'{scan_ho}/{test_file}')
