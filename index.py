import time
from datetime import datetime

from core.comparefolders import compare_folders

# Once at launch
#   if invoice date > 6 month:
#       remove invoice (regex or if [date] > 6 month)
app = True

while app:
    # log (Create a function for display more informations)
    print(f'Checkout: {datetime.now()}')
    
    # File manager
    compare_folders()

    # Time to wait
    time.sleep(1800)