#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Oct 22 15:40:31 2019

@author: sourabh-burnwal

python program to find addition and product of two sparse matrices as coo matrices:
"""

import numpy as np

#function to make coo matrix
def make_matrix(mat):
    adjMat= []
    row= np.shape(mat)[0] #number of rows
    col= np.shape(mat)[1] #number of columns
    for i in range(col):
        for j in range(row):
            if mat[i][j]!=0 :
                adjMat.append([i,j,mat[i][j]]) #appending non-zero entries
    adjMat2= np.reshape(adjMat,(len(adjMat),3)) #converting into numpy array format
    print(adjMat2)
    return adjMat

#function to check whether it's a sparse matrix
def check_mat(mat):
    zero=0
    m= len(mat)
    n= len(mat[0])
    for i in range(m):
        for j in range(n):
            if mat[i][j]==0:
                zero=zero+1

    if zero>(m*n)/2: #condition for being a sparse matrix
        print("--> it's a sparse matrix")
    else:
        print("--> it's not a sparse matrix")

#function to find sum of two coo matrices
def add_mat(mat1,mat2):
    sum_mat=[]
    for i in range(len(mat1)):
        temp=0
        for j in range(len(mat2)):
            #case1: adding values in same row and column
            if mat1[i][0]==mat2[j][0] and mat1[i][1]==mat2[j][1]:
                sum_mat.append([mat1[i][0],mat1[i][1],mat1[i][2]+mat2[j][2]])
                sum_mat.remove(mat2[j]) #removing the extra row appended when i==0
                temp=1
            elif i==0:
                sum_mat.append(mat2[j]) #case2_1: appending rows of mat2
        if temp==0:
            sum_mat.append(mat1[i]) #case2_2: appending rows of mat1 if case1 didn't get run
    sum_mat = sorted(sum_mat)
    sum_mat2= np.reshape(sum_mat,(len(sum_mat),3)) #converting into numpy array format
    print(sum_mat2)

#function to obtain transpose of a coo matrix
def transpose(mat):
    trans_mat=[]
    for i in range(len(mat)):
        trans_mat.append([mat[i][1],mat[i][0],mat[i][2]]) #appending the transposed entries
    trans_mat= sorted(trans_mat)
    trans_mat2= np.reshape(trans_mat,(len(mat),3)) #converting into numpy array format
    return trans_mat2

#function to multiply two coo matrices
def multiply(mat1,mat2):
    prod_mat= []
    mat2_t= transpose(mat2) #transposing second matrix
    for i in range(len(mat1)):
        for j in range(len(mat2_t)):
            if mat1[i][1]==mat2_t[j][1]: #checking if second entry of both matrices are same
                prod= mat1[i][2]*mat2_t[j][2] #finding product of their entries
                #appending row of first matrix as row and row of second matrix as column
                prod_mat.append([mat1[i][0],mat2_t[j][0],prod])
    prod_mat= sorted(prod_mat)
    prod_mat2= np.reshape(prod_mat,(len(prod_mat),3)) #converting into numpy array format
    print(prod_mat2)

#driver program
mat1= np.array([[0,0,0,1],[0,1,0,1],[0,1,0,0],[0,0,2,0]])
mat2= np.array([[0,20,0,0],[0,0,15,0],[0,24,0,0],[0,0,0,30]])
print("mat1:")
mat_1= make_matrix(mat1)
check_mat(mat1)
print("mat2:")
mat_2= make_matrix(mat2)
check_mat(mat2)
print("sum:")
add_mat(mat_1,mat_2)
print("product:")
multiply(mat_1,mat_2)
