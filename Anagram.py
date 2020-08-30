import math
import os
import random
import re
import sys

# Complete the anagram function below.
def anagram(s):
    if(len(s)%2!=0):
        return -1
    else: 
        k=s[0:len(s)//2]
        j=s[(len(s)//2)::]
        k=list(k)
        j=list(j)
        for char in k:
            if char in j:
                j.remove(char)
        return (len(j)) 

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input())

    for q_itr in range(q):
        s = input()

        result = anagram(s)

        fptr.write(str(result) + '\n')

    fptr.close()
