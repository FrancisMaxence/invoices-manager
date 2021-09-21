# modules
import core
import paths


fm = core.File_manager(paths.src, paths.scan_ho)

# For test only, remove when app is ready !
fm.testing_file_move()
