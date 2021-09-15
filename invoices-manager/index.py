# modules
import core
import paths
import utils

# Change utils.test_file by utils.test_files for future improvment
# Replace utils.test_files by scan directory for production
fm = core.File_manager(paths.src, paths.scan_ho, utils.test_file)

# For test only, remove when app is ready !
fm.testing_file_move()
