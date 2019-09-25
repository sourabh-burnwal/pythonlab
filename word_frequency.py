"""Python programs to count words in any file and sorting the frequency of words"""
# @author: sourabh-burnwal

#import queue to use PriorityQueue to sort the frequencies
import queue

fqueue= queue.PriorityQueue() #make a empty PriorityQueue
doc= open('<file>', 'r') #open the file in read mode
text_str= doc.read().split()
final_str=[]
cnt=[]
for x in text_str:
    if(x in final_str):
        i= final_str.index(x)
        cnt[i]+=1
    else:
        final_str.append(x)
        cnt.append(1)
for i in range(len(final_str)-1):
    fqueue.put((cnt[i],final_str[i])) #put the frequencies as tuples so as to form a sorted queue

for i in range(len(final_str)-1):
    print(fqueue.get())
