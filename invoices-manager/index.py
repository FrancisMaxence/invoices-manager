# modules
import core
import paths
import utils

fm = core.File_manager(paths.src, paths.scan_ho, utils.test_file)

# For test only, remove when app is ready !
fm.testing_file_move()
