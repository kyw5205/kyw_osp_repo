#!/usr/bin/python3

def fibonacci(n):
    a,b = 1, 0
    for i in range(n):
        a, b = b, a + b
    return b


num = int(input("number of fibonacci "))
for i in range(1,num+1):
    print( fibonacci(i), end=' ' )
print(' ')
print ("%d th fibonacci number is %d" %(num,fibonacci(num)))


