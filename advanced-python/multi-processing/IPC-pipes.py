import subprocess

cat = subprocess.Popen(['python', 'my-cat.py', 'hosts.xml'], stdout=subprocess.PIPE)
tr = subprocess.Popen(['python', 'my-tr-command.py'], stdin=cat.stdout, stdout=subprocess.PIPE)
nl = subprocess.Popen(['python', 'my-nl-command.py'], stdin=tr.stdout, stdout=subprocess.PIPE)

for line in nl.communicate():
    if line:
        print(line.decode('ascii'))