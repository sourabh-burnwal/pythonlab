"""Python program to show the working of loop invariants in Selection sort to prove it's correctness."""
# @author: sourabh-burnwal

#import random to generate entries in list
import random

#inner loop invariant function
def innerinv(alist, i, j, smallest):
    for k in range(i + 1,j - 1):
        ifalist[smallest] < alist[k]: #inner loop invariant expression
            print("inner loop invariant verified")
        else:
            print("inner loop invariant not verified")

#outer loop invariant function
def outerinv(alist, i):
    for k in range(i, len(alist) - 1):
        if alist[i - 1] <= alist[k]: #outer loop invariant expression
            print("outer loop invariant verified")
        else:
            print("outer loop invariant not verified")

#function to do selection sort
def selectionsort(alist):
    for i in range(len(alist)):
        smallest = i
        for j in range(i + 1, len(alist)):
            if(alist[smallest] > alist[j]):
                smallest = j
                #check if inner loop invariant verified
                innerinv(alist, i, j, smallest)
        alist[i], alist[smallest] = alist[smallest], alist[i]
        if(i > 0):
            #check if outer loop invariant verified
            outerinv(alist, i)

#driver function
alist = []
for i in range(0, 8):
    x = random.randint(1, 20)
    alist.append(x)
print("unsorted list is: ", end = " ")
print(alist)
selectionsort(alist)
print("sorted list is: ", end = " ")
print(alist)
