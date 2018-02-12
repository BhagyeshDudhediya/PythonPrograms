#!/usr/bin/python

# A program to demonstrate use of multiline statements, quoted string in python

import sys;

item_1 = 10;
item_2 = 20;
item_3 = 30;

total_1 = item_1 + item_2 + item_3;
# Following is valid as well:
total_2 = item_1 + \
          item_2 + \
          item_3 + \
          10;
print("total_1 is:", total_1);
print("\ntotal_2 is:", total_2, "\nDone..");

# NOTE: Python does not have multi-line comment feature in it.
# Following is the way quotations are used for a string
# Python accepts single ('), double (") and triple (''' or """) quotes to denote string literals,
# as long as the same type of quote starts and ends the string. 
# The triple quotes are used to span the string across multiple lines

word = 'word'
statement = "This is a statement";
multiline_string = """This is a multi-line string
You can call it a paragraph if you wish..!!
Choice is yours..:P""";

print("\n\nWord:", word, "\n\nStatement:", statement, "\n\nMulti-line string: ", multiline_string);
