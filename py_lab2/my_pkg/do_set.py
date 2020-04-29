#!/usr/bin/python3


def pr_un_in(a,b):
    unlist =list(a|b)
    inlist = list(a&b)
    u = sorted(unlist)
    i = sorted(inlist)
    print("=> union ", u)
    print("=> intersection ", i)

    
