from ftplib import FTP

ftp = FTP()
ftp.connect('perf-c856.datadomain.com')
ftp.login('ptc', 'ABC1234')
ftp.retrlines('LIST')

ftp.close()