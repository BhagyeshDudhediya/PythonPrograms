import fileinput

print "###### Using fileinput module now ######"
for line in fileinput.input():
    print line

print "###### Using sys module now ######"

import sys
for x in sys.argv[1:]:
    f1 = open(x, "r")
    for myline in f1.readlines():
        print myline
    f1.close()
