#!/usr/bin/python3


def bin_to_dec(bi_num):
    dec_num = 0
    bi_num_str = str(bi_num)
    for i, digit in enumerate(bi_num_str):
        dec_num += int(digit) * pow(2,len(bi_num_str) -1 -i)
    return dec_num

def makeb(a):
	return format(a, 'b')

def makeo(a):
	return format(a, 'o')

def makeh(a):
	return format(a, 'x')

