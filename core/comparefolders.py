import os
from core.filemanager import FileManager

def compare_folders():
    fm = FileManager()

    main_files = os.listdir(fm.main)
    scan_ho_files = os.listdir(fm.scan_ho)
    scan_ho_len = len(scan_ho_files)
    waiting_files = os.listdir(fm.waiting)
    waiting_len = len(waiting_files)

    if waiting_len == 0 and scan_ho_len == 0:
        fm.duplicate_file()
    elif waiting_len > 0 and scan_ho_len == 0:
        fm.archive_files()
        fm.duplicate_file()
    
    # For utils.log()
    return main_files, waiting_files
