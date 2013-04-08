#! /usr/bin/env python

import os
import sys

if __name__ == "__main__":
    print "RAN", sys.argv
    os.system('fab %(command)s --rc=~/.fabricrc --fabricfile=')
