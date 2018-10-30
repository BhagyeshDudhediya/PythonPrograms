"""Read passwd.txt file and for 1st 10 lines replace all occurences of ':' with ','
Also, the changes should be recorded bck to the same file"""
import re
from fileinput import input, filelineno

# input file takes arg/flags as backup and inplace which takes backup
# and also does inplace replacement i.e it writs to temp file and renames
# temp file to original file
for line in input('passwd.txt', inplace=True, backup='.bak'):
    if (filelineno() <= 10):
        line = re.sub(':', ',', line)
    print (line, end='')

