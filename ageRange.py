#!/usr/bin/env python3
#-*- coding:utf-8 -*-

#this script is to assert your type after age typing
import sys
age= int(sys.argv[1])
#age = int(input("please input your age:"))
if 0 <= age < 10:
    print("you belong to kids")
elif 10 <= age < 18:
    print("you belong to teenager")
elif 18 <= age < 30:
    print("you belong to adult")
elif 30 <= age <60:
    print("you belong to older")
elif 60 <= age <120:
    print("you belong to oldest")
else:
    pass 
