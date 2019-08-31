"""Python program to find a continuous subset of a list whose sum is maximum"""
# @author: sourabh-burnwal

#import random to generate random numbers in the list
import random

alist=[]
for i in range(0,10):
    x= random.randint(-60,60)
    alist.append(x)
print("list: ", end=" ")
print(alist)
totalsum=[]
subsets=[]
for i in range(0,len(alist)):
    for j in range(i+1,len(alist)+1):
        totalsum.append(sum(alist[i:j])) #append sum of every subset in totalsum list
        subsets.append(alist[i:j]) #append every subset of original list as sublist in subsets list
maxvalue= max(totalsum)
print("the maximum sum is: ",maxvalue)
print("the maximal subset is: ",subsets[totalsum.index(maxvalue)])
