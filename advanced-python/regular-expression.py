import re

s = 'the python and perl scripting'
pattern = 'P.+?N'

m = re.search(pattern, s, re.IGNORECASE)
if m:
    print ('matched string:',m.group())
    print (m.start())
    print (m.end())
    print (m.span())
    before = s[:m.start()]
    after = s[m.end():]
    print ('before: {}|'.format(before))
    print ('after: |{}'.format(after))
else:
    print ('Failed to match')

print ('=== Extracting from matches ===')
"""Grouping aka Back referencing"""
s='123.12.1.199'
pattern = '(\d+)\.(\d+)\.(\d+)\.(\d+)'
m = re.search(pattern, s, re.IGNORECASE)
if m:
    print ('match string:', m.group())
    print (m.group(0))
    print (m.group(4))
else:
    print('No match found')

"""Match multiples in same line"""
print ('=== Multiple matches in a string ===')
s = 'the python and perl scripting'
pattern = 'P.+?N'
for m in re.finditer(pattern, s, re.IGNORECASE):
    print (m.group())
    print (m.span())

print (re.findall(pattern, s, re.IGNORECASE)) # list of matched strings