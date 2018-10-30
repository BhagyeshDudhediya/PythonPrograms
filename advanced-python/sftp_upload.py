from customsshclient import CustomSSHClient
from archives import make_archive, glob

def main():
    make_archive('temp.zip').save(*glob('*.py'))

    ssh = CustomSSHClient('perf-c856.datadomain.com', 22, 'ptc', 'ABC1234')
    ssh.upload('temp.zip')

if __name__ == '__main__':
    main()
