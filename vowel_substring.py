#!/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'findSubstring' function below.
#
# The function is expected to return a STRING.
# The function accepts following parameters:
#  1. STRING s
#  2. INTEGER k
#

def findSubstring(s, k):
    j = k
    mx = 0
    count= 0
    max_sub = ""
    ln = len(s)
    i = 0
    for i in s[0:j]:
        if i in 'aeiou':
            count+=1
    if count!=0:
        mx = count
        max_sub = s[0:j]
    i = 0
    while(j<ln-1):
        if(s[i] in 'aeiou'):
            if count!=0:
                count-=1
        i+=1        
        if(s[j] in 'aeiou'):
            count+=1

        j+=1
        if count>mx:
            mx = count
            max_sub = s[i:j]
             
        
        
    if max_sub == "":
        return "Not found!"
    else:
        return max_sub
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    k = int(input().strip())

    result = findSubstring(s, k)

    fptr.write(result + '\n')

    fptr.close()
