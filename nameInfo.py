#!/usr/bin/env python3
#-*- coding:utf-8 -*-

#this script is to introduce the use of __name__
#__name__ is to help us idenfy which kind is this script is running
#when it run as a single script __name__ = __main__
#when it run as a moudle in another script  __name__ = thisMoudleName

print("now __name__ is {}".format(__name__))

if __name__ == '__main__':
    print("now this script is running as a single script!")
else:
    print("now this script is running in another script")

#using __name__, we can control the code running process while importing 
