"""single thread ssh client"""

import paramiko

class CustomSSHClient:
    def __init__(self, host, port, user, pwd):
        self.host = host
        self.user = user
        self.port = port
        self.ssh = paramiko.SSHClient()
        self.ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        self.ssh.connect(self.host, self.port, self.user, pwd)

    def upload(self, filename):
        """sftp upload"""
        print('Uploading', filename)
        sftp = self.ssh.open_sftp()
        sftp.put(filename, '/tmp/'+filename)
        print('Done uploading', filename)
        sftp.close()

    def check_output(self, cmd):
        stdin, stdout, stderr = self.ssh.exec_command(cmd)
        return stdout.read().decode('ascii')

    def __del__(self):
        self.ssh.close()

if __name__ == '__main__':
    ssh = CustomSSHClient('localhost', 22, 'training', 'training')
    op = ssh.check_output('ls')
    print(op)
