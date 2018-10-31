import subprocess
"""
from os import getpgid

print('parent process id :', getpgid())

op = subprocess.check_output(['bash', '-c', 'echo $$'])
print('child process:', op)
"""
status = subprocess.call(['ipconfig'])
print ('exit status:', status)
