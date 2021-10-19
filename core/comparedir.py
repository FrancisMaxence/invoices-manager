import os
from core.filemanager import FileManager

def compare_directories():
    fm = FileManager()

    scan_ho_files = os.listdir(fm.scan_ho)
    scan_ho_len = len(scan_ho_files)
    waiting_files = os.listdir(fm.waiting)
    waiting_len = len(waiting_files)

    if waiting_len == 0 and scan_ho_len == 0:
        fm.duplicate_file()
    elif waiting_len == 0 and scan_ho_len > 0:
        fm.duplicate_file()
    elif waiting_files != scan_ho_files:
        fm.archive_files()
        fm.duplicate_file()
