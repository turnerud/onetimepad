#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Sep 24 09:49:21 2024

@author: simon

"""


import random

p1 = "Send me $100"
p2 = "I will send you $100"

list_of_p1_chars = list(p1)
list_of_p2_chars = list(p2)
key = []
p1keylen = len(list_of_p1_chars) * 7
p2keylen = len(list_of_p2_chars) * 7
p1counter = 0 
p2counter = 0
finalkeylen = max(p1keylen, p2keylen)

cipherp1list = []
cipherp2list = []

key = [random.randint(0, 1) for _ in range(finalkeylen)]

    
while p1counter < p1keylen:
    for x in list_of_p1_chars:
        binary = format(ord(x), '07b')
        p1digitlist = [int(digit) for digit in binary]
        for y in p1digitlist:
            if p1counter < p1keylen:
                if y == key[p1counter]:
                    cipherp1list.append("0")
                else:
                    cipherp1list.append("1")
                p1counter += 1
                
while p2counter < p2keylen:
    for x in list_of_p2_chars:
        binary = format(ord(x), '07b')
        p2digitlist = [int(digit) for digit in binary]
        for y in p2digitlist:
            if p2counter < p2keylen:
                
                if y == key[p2counter]:
                    cipherp2list.append("0")
                    
                else:
                    cipherp2list.append("1")
                p2counter += 1
                
                
cipherp1 = ''.join([str(item) for item in cipherp1list])
cipherp2 = ''.join([str(item) for item in cipherp2list])


print("The ciphertext of p1 is: ", cipherp1)
print("The ciphertext of p2 is: ", cipherp2)



                
                
                
        
        



        
    


