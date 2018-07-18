# Print names of python files in current folder

import os
os.system("ls *.py")

import glob
print glob.glob("*.py")

# Print numbers of occurences of abc in string
import re
str1 = "ABC jfdskfh abc Abc"
print str1.count("abc")
print re.findall('abc', str1)
print re.findall("abc", str1, re.IGNORECASE)

str2 = 'a.b'
print re.findall('a[.]b', str2)

# Get all words except , space and :
str3 = "EMC Bangalore,Karnataka:India"
print re.findall('[^\s,:]+', str3)
