#!/usr/bin/python3

from bin_to_others import *
from do_set import pr_un_in

while True:

    mode = input ("Select menu : 1) conversion 2) union/intersection 3) exit ?  ")

    if mode == '1':
        bin_num = input("input binary number : ")

        dec_num = bin_to_dec(bin_num)

        print("=> OCT > " + makeo(dec_num))
        print("=> DEC > " + str(dec_num))
        print("=> HEX > " + makeh(dec_num))


    if mode =='2':
        a_str = input("1st list : ")
        ma_str =  a_str.replace(","," ").replace("["," ").replace("]"," ")
        first_str = ma_str.split()
        first_set = set(first_str)

        b_str = input("2nd list : ")
        mb_str =  b_str.replace(","," ").replace("["," ").replace("]"," ")
        second_str = mb_str.split()
        second_set = set(second_str)

        pr_un_in(first_set, second_set)

    if mode =='3':
        print("exit the program")
        break;
