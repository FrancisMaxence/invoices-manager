import time
from datetime import datetime

from core.filemanager import FileManager
from core.comparefolders import compare_folders


app = True
counter = 0
fm = FileManager()

# Remove invoices older than 6 months
fm.invoices_cleaner()

while app:
    print(f'Checkout: {datetime.now()}')
    
    # File manager
    counter += compare_folders()

    if counter == 5:
        print('\033[1;31;40m Is there someone at the Head Office ? \033[1;37;40m')
        counter = 0

    # Time to wait
    time.sleep(1800)