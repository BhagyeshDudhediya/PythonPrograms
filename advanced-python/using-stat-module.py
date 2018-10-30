import os
import stat

x=os.stat("oop1.py")
print x
print stat.S_ISDIR(x[stat.ST_MODE])
