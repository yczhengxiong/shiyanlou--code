#!/usr/bin/env python3
#-*- coding:utf-8 -*-

#this is a personal tax calculator script.

import sys
input_infos_list = sys.argv[1:]
# this part is to process the income data and make a except
try:
	payment_infos_dict = {}
	for input_info in input_infos_list:
		i = input_info.split(":")
#		print(i)
		payment_infos_dict[i[0]] = int(i[1])
except ValueError:
	print("Parameter Error")

#this part is to calculate tax and store the result in another dict
incomes_info_dict = {}
for key,value in payment_infos_dict.items():
	payment_able = value - 5000 - value * 0.165
	if 0<payment_able <= 3000:
		income = value - value* 0.165 - (payment_able*0.03 - 0)
	elif 3000<payment_able<=12000:
		income = value - value* 0.165 - (payment_able*0.10 - 210)
	elif 12000<payment_able<=25000:
		income = value - value* 0.165 - (payment_able*0.20 - 1410)
	elif 25000<payment_able<=35000:
		income = value - value* 0.165 - (payment_able*0.25 - 2660)
	elif 35000<payment_able<=55000:
		income = value - value* 0.165 - (payment_able*0.30 - 4410)
	elif 55000<payment_able<=80000:
		income = value - value* 0.165 - (payment_able*0.35 - 7160)
	elif 80000<payment_able:
		income = value - value* 0.165 - (payment_able*0.45 - 15160)
	else:
		income = value - value * 0.165
	incomes_info_dict[key] = income

#this part is to print out the income information
for key,value in incomes_info_dict.items():
	print("{}:{:.2f}".format(key,value))