import os
from core.filemanager import FileManager

def compare_folders():
    fm = FileManager()

    main_files = os.listdir(fm.main)
    scan_ho_files = os.listdir(fm.scan_ho)
    scan_ho_len = len(scan_ho_files)
    waiting_files = os.listdir(fm.waiting)
    waiting_len = len(waiting_files)

    log_main = f'\033[1;32;40m main/ -> waiting/ and scan-ho/:\033[1;37;40m {", ".join(main_files)}'
    log_waiting = f'\033[1;32;40m waiting/ -> archives/: \033[1;37;40m {", ".join(waiting_files)}'

    if waiting_len == 0 and scan_ho_len == 0:
        fm.duplicate_file()
        print(log_main)
    elif waiting_len > 0 and scan_ho_len == 0:
        fm.archive_files()
        fm.duplicate_file()
        if main_files:
            print(log_main)
        print(log_waiting)
    else:
        print('\033[1;33;40m Nothing changed \033[1;37;40m')
        return 1
