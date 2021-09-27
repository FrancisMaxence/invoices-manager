data = './data'
archives = f'{data}/archives'
main = f'{data}/main'
waiting = f'{data}/waiting'

# Change the value by False for production
is_dev = True
scan_ho = ''

if is_dev:
    scan_ho = f'{data}/scan-ho'
else:
    scan_ho = '//PC01-LANGELIER/Scan Ho'