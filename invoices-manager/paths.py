# Change the value by False for production
is_dev = True

data = './data'
src = f'{data}/main'
waiting = f'{data}/waiting'

if is_dev:
    scan_ho = f'{data}/scan-ho'
else:
    scan_ho = '//PC01-LANGELIER/Scan Ho'