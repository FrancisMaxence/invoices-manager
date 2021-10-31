import time
import datetime

from core.comparefolders import compare_folders

# Once at launch
#   if invoice date > 6 month:
#       remove invoice (regex or if [date] > 6 month)
app = True

while app:
    print(f'Checkout: {datetime.datetime.now()}')
    compare_folders()
    time.sleep(1800)