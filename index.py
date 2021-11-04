import time
from datetime import datetime

from core.comparefolders import compare_folders

# Once at launch
#   if invoice date > 6 month:
#       remove invoice (regex or if [date] > 6 month)

app = True
counter = 0

while app:
    # log (Create a function for display more informations)
    print(f'Checkout: {datetime.now()}')
    
    # File manager
    counter += compare_folders()

    if counter == 5:
        print('\033[1;31;40m Is there someone at the Head Office ? \033[1;37;40m')
        counter = 0

    # Time to wait
    time.sleep(1800)