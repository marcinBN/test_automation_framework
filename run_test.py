import argparse
import unittest
import sys
import os
from framework_config import MyConfig


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("-f", "--file", help="Test filename", required=True,
                        choices=[f for f in os.listdir('.') if os.path.isfile(f) and f.startswith("test_") and f.endswith(".py")])
    parser.add_argument("-e", "--env", help="Environment", choices=MyConfig.environments_URLS.keys(), default="dev")

    args = parser.parse_args()

    MyConfig.ENV_in_use = args.env

    loader = unittest.TestLoader()
    suite = unittest.TestSuite()
    loaded_tc = loader.discover(".", pattern=args.file)
    suite.addTest(loaded_tc)
    runner = unittest.TextTestRunner(verbosity=3)
    returned_code = not runner.run(suite).wasSuccessful()
    sys.exit(returned_code)
