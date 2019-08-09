#!/usr/bin/env python3
# -*- coding:utf-8 -*-

import sys
list_argv = sys.argv[1:]
dics = {}

for argv in list_argv:
    string = argv.split(":")
    dics[string[0]] = string[1]

for key,value in dics.items():
    print("ID:{} Name:{}".format(key,value))
