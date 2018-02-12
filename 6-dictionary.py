#!/usr/bin/python3

# Python's dictionaries are kind of hash-table type. They work like associative arrays or hashes found in Perl
# and consist of key-value pairs.
# A dictionary key can be almost any Python type, but are usually numbers or strings.
# Values, on the other hand, can be any arbitrary Python object. 
# Dictionaries are enclosed by curly braces ({ }) and values can be assigned and accessed using square braces ([])

dict = {}
dict['one'] = "This is one"
dict[2]     = "This is two"
tinydict = {'name': 'john','code':6734, 'dept': 'sales'}
print ("dict: ", dict)                              # Prints entire dictionary
print ("dict['one]: ", dict['one'])                 # Prints value for 'one' key
print ("dict[2]: ", dict[2])                        # Prints value for 2 key
print ("tinydict: ", tinydict)                      # Prints complete dictionary
print ("tinydict.keys(): ", tinydict.keys())        # Prints all the keys
print ("tinydict.values(): ", tinydict.values())    # Prints all the values
dict['one'] = 1
print("dict['one']: ", dict['one'])
key = 'bhagyesh';
dict[key] = 'dudhediya'
print("key=bhagyesh, dict[key]: ", dict[key])
