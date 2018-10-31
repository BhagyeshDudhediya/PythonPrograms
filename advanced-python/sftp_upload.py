from customsshclient import CustomSSHClient
from archives import make_archive, glob

def main():
    make_archive('temp.zip').save(*glob('*.py'))

    ssh = CustomSSHClient('localhost', 22, 'training', 'training')
    ssh.upload('temp.zip')

if __name__ == '__main__':
    main()
