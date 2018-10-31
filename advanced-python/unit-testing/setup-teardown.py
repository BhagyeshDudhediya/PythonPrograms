import unittest
from random import randint

"""
setup and tear down are executed for each unit test
setup does pre-reqs for the tests
teardown does cleanup of the test
"""

class SetupAndTearDownTestCase(unittest.TestCase):
    def setUp(self):
        self.data_set = [randint(1, 10) for i in range(50)]
        print(self.data_set)

    def test_check_status(self):
        self.assertIn(15, self.data_set)

    def test_list_len(self):
        self.assertEqual(len(self.data_set), 50)

    def tearDown(self):
        print(self.data_set)
        del self.data_set

if __name__ == '__main__':
    unittest.main()