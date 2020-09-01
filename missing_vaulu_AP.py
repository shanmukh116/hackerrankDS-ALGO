Find the missing element from  an ordered array A[ ], consisting of N elements representing an Arithmetic Progression (AP) .
 
"""
Input:
The first line of input contains an integer T denoting the number of test cases. Then T test cases follow. 
The first line of each test case contains an integer N, where N is the size of the array A[ ].
The second line of each test case contains N space separated integers of an Arithmetic Progression denoting elements of the array A[ ].
 

Note: The series should have a missing element in between a perfect A.P. with no missing element will not be considered.
 

Output:
Print out the missing element. 
 

Constraints:
1 <= T <= 100
2 <= N <= 10
-50 <= A[i] <=50
 

Examples :

Input:
3
3 
2 10 14 
4 
-28 -21 -7 0 
5 
9 12 15 21 24

Output : 
6
-14
18 """

solution:


n=int(input())
for i in range(n):
    a=int(input())
    b=list(map(int,input().split()))
    sum=0
    if(len(b)==2):
        d=(b[1]-b[0])/2
    elif(len(b)==3):
        if(b[1]-b[0]<b[2]-b[1]):
            d=b[1]-b[0]
        else:
            d=b[2]-b[1]
    elif((b[1]-b[0])==(b[len(b)-1]-b[len(b)-2])):
        d=b[1]-b[0]
    elif(b[2]-b[1]==b[1]-b[0]):
        d=b[1]-b[0]
    else:
        d=b[len(b)-1]-b[len(b)-2]
    k=(a+1)/2*(2*b[0]+(a*d)) 
    for i in range(len(b)):
        sum+=b[i]
    print(int(k-sum))    