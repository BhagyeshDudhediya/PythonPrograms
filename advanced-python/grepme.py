
"""Get lines that match the regular expression and also print the lines that match from one or more
file names as argument.
Demonstration of pattern matching"""

from glob import glob
import re
from fileinput import input, filelineno, filename # stream readers

class GrepMe:
    def __init__(self, pattern, *args):
        self.pattern = pattern
        self.files = args
        self.__do_match()

    def __do_match(self):
        for line in input(self.files):
            if re.search(self.pattern, line, re.IGNORECASE):
                print('{}:{}:{}'.format(filename(), filelineno(), line), end='') # print by default prints new line so use end='' to omit that new line


if __name__ == '__main__':
    GrepMe('class', *glob('*.py'))