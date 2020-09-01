"""You will be given a list of integers,arr , and a single integer k. You must create an array of length k  from elements of arr such that its arr unfairness is minimized. Call that array subarr. Unfairness of an array is calculated as
     max(subarr)-min(subarr)
Where:
- max denotes the largest integer in subarr
- min denotes the smallest integer in subarr

As an example, consider the array [1,4,7,2] with a k of 2. Pick any two elements, test subarr=[4,7].
unfairness=max(4,7)-min(4,7)=3

Testing for all pairs, the solution  provides the minimum unfairness.

Note: Integers in  may not be unique.

Function Description

Complete the maxMin function in the editor below. It must return an integer that denotes the minimum possible value of unfairness.

maxMin has the following parameter(s):

k: an integer, the number of elements in the array to create
arr: an array of integers .
Input Format

The first line contains an integer , the number of elements in array .
The second line contains an integer .
Each of the next  lines contains an integer  where .

Output Format

An integer that denotes the minimum possible value of unfairness.
"""
solution:
  def maxMin(k, arr):
    arr.sort()
    m=2456789342
    for i in range(len(arr)-k+1):
        h=arr[i+k-1]-arr[i]
        if(h<m):
            m=h
    return m 