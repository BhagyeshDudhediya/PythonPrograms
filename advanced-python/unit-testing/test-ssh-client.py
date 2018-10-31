from customsshclient import CustomSSHClient
import unittest

class TestCaseSSHClient(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.ssh_client = CustomSSHClient('localhost', '22', 'training', 'training')

    def test_ssh_client(self):
        op = self.ssh_client.check_output('whoami')
        self.assertIn('localhost', op)
    @classmethod
    def tearDownClass(cls):
        del cls.ssh_client

if __name__ == '__main__':
    unittest.main()