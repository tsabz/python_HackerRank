import math
import os
import random
import re
import sys


# Theres an array of socks, we must find the number of pairs there are.

# n = 7 , length of the array, number of socks in a pile [1,2,1,2,1,3,2]
#must itterate through the array and find a the individual colors and their pairs
#create a hash table
# have two counters 
# add a counter , once the counter reaches two  add to the hash table
# if it equals two it is a pair add to pair counter print(pairs)
#
# 
#  n = len(ar)+1

def sockMerchant(n, ar):

    sock_drawer = []
    n = len(ar) 
    answer = 0
    for i in range(n):
        if ar[i] not in sock_drawer:
            sock_drawer.append(ar[i])            
        else:
            sock_drawer.remove(ar[i])
            answer = answer + 1
    print(answer)
       

sockMerchant(7,[1,2,1,2,1,3,2])        