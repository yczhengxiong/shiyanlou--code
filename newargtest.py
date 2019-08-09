#!/usr/bin/env python3
#-*- coding:utf-8 -*-

#print argv in sys.argvs that len is bigger than 3

import sys
for arg in sys.argv[1:]:
    if len(arg) > 3:
        print(arg)
    else:
        pass
