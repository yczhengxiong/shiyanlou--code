#!/usr/bin/env python3
#-*- coding:utf-8 -*-

#this script is to introduce how to use list in python

import sys
list1 = sys.argv[1:]
list_short = []
list_long = []
for arg in list1:
    if len(arg)>3:
        list_long.append(arg)
    else: 
        list_short.append(arg)
print(" ".join(list_short))
print(" ".join(list_long))
