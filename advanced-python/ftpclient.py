from ftplib import FTP

ftp = FTP()
ftp.connect('localhost')
ftp.login('training', 'training')
ftp.retrlines('LIST')

ftp.close()
