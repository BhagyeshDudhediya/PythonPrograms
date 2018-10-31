"""
tests should be named as test_XYZ
tests are always executed in alphabetical order
"""

import unittest
#from myutils import power

class CustomTestCase(unittest.TestCase):
    """test case"""
    def test_power(self):
        """test"""
        self.assertEqual(pow(2,3), 8)

    def test_for_failure(self):
        self.assertEqual(pow(2,2), 4)

    # skip the test for testing
    @unittest.SkipTest
    def test_dummy(self):
        assert 1 == 1, 'a failed dummy test'


if __name__ == '__main__':
    # Invoke the test
    unittest.main()

"""
From command line how to involke particular test:
$ python -m unittest unit-testing.CustomTestCase.test_power -v

or run all tests:
$ python -m unittest unit-testing.CustomTestCase -v

"""