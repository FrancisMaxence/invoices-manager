import os

data = f'{os.environ["USERPROFILE"]}/Desktop/vincent/codes/invoices-manager/data'
pc01 = os.environ["LOGONSERVER"]

main = f'{data}/main'
waiting = f'{data}/waiting'

################################################
##  Change the value by False for production  ##
################################################
is_dev = True

scan_ho = ''
archives = ''

if is_dev:
    archives = f'{data}/archives'
    scan_ho = f'{data}/scan-ho'
else:
    scan_ho = f'{pc01}/Scan Ho'
    archives = f'{pc01}/Archives Factures'
