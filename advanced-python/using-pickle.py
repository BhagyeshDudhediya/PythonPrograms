# Syncronisation-----------
# There are few cases where we want to store the oject like list, dictionary into file.
# Simply it is not possible, and hence there are modules like pickle, json, etc which
# dumps and loads and does extra things into a file or a string.
# Dumping i.e list, hash, json-code can be done in files or string
# Loading i.e getting back list, hash, json code can be done from files or string

import pickle
list1 = [10,20,30]

# There is another function dump which dumps it to the file
# dumps func dumps the data to string.. Similar is the case for load and loads
str1=pickle.dumps(list1)
print str1
list2=pickle.loads(str1)
print list2

