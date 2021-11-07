import os

import devsetup

data = './data'
pc01 = os.environ["LOGONSERVER"]

main = f'{data}/main'
waiting = f'{data}/waiting'

scan_ho = ''
archives = ''

if devsetup.is_dev:
    archives = f'{data}/archives'
    scan_ho = f'{data}/scan-ho'
else:
    scan_ho = f'{pc01}/Scan Ho'
    archives = f'{pc01}/Archives Factures'
