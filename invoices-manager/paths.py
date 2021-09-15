is_dev = True

src = './directory-testing/main' # Replace by /Desktop (find absolute path) in production mode

if is_dev:
    scan_ho = './directory-testing/scan-ho'
else:
    scan_ho = '//PC01-LANGELIER/Scan Ho' # The Head Office repository dist