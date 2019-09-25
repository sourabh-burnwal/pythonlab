#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Sep 24 14:47:33 2019

@author: sourabh-burnwal
"""

import numpy as np

class Graph():
    def __init__(self,order):
        self.graph= np.zeros((order,order),dtype=int) #initializing a zero matrix
        self.order= order
        
    def addedge(self,v1,v2,weight):
        self.graph[v1][v2]= weight 
        self.graph[v2][v1]= weight  #matrix will be symmetric as edges don't have direction
        
    def findmin(self,visited,dist):
        arr=[]
        arr= [dist[i] for i in range(self.order) if dist[i]!=0 and i not in visited] #collecting all non-zero values
        minimum= min(arr)
        min_index= dist.index(minimum)
        return min_index
    
    def dijsktra(self,src):
        visited=['src']  #source will be visited first
        dist= self.graph[src,:].tolist() #will be working on source row so as to find minimum distances
        print("the adjacency matrix for the graph is:\n{}".format(self.graph))
        print("\niterations:")
        while(len(visited)!=self.order):
            min_index= self.findmin(visited,dist) #find node with minimum distance from the source
            visited.append(min_index) #mark that node visited 
    
            for ind in range(1,self.order):
                if self.graph[min_index][ind]>0 and ind not in visited: #for every adjacent node, find if it's not visited 
                    if dist[ind]==0: #here, zero actually is the infinite distance, so it'll be changed
                        dist[ind]= dist[min_index]+self.graph[min_index][ind]

                    elif dist[ind]> dist[min_index]+self.graph[min_index][ind]: #for every adjacent node of that node, find it's minimum
                        dist[ind]= dist[min_index]+self.graph[min_index][ind]
            print()       
            print("path is: {}".format(visited))
            print("minimum distances: {}".format(dist))
        
      
graph= Graph(6)
graph.addedge(0,1,10)
graph.addedge(1,3,5)
graph.addedge(2,4,6)
graph.addedge(1,2,7)
graph.addedge(0,2,9)
graph.addedge(1,4,4)
graph.addedge(2,5,7)
graph.addedge(1,5,11)
graph.addedge(3,4,12)

graph.dijsktra(0)