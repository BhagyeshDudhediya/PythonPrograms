import re

s = 'my:name:is:khan'
pattern = ':'
replacement = ' '

s2 = re.sub(pattern, replacement, s)
print('new string: ', end='')
print (s2)
print('original string: ', end='')
print (s)

replacement = '*'
s3 = re.sub('[AEIOU]', replacement, s, flags=re.IGNORECASE)
print (s3)
