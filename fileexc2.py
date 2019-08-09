#!/usr/bin/env python3
#-*- coding:utf-8 -*-

filename = str(input("enter file path:"))

try:
    f = open(filename)
    print(f.read())
    f.close()
except FileNotFoundError as err:
    print("Error:{}".format(err))
