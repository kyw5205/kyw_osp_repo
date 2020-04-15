#!/usr/bin/python3

num = input (' How many numbers will you enter? ')
sum = 0
nums = list()
i = 0

while i<int(num):
    nums.insert(i,input("input number "))
    sum = sum + int(nums[i])
    i = i+1 
avr = sum / int(num)

print ( "average is ",avr)
