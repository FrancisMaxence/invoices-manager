import unittest

testsuite = unittest.TestLoader().discover('./tests')
unittest.TextTestRunner(verbosity=2).run(testsuite)
