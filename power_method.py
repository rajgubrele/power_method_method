# -*- coding: utf-8 -*-
"""power_method.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1m75b-WvF4Obq5-CTvYKB_yB-wied0XcZ
"""

######################## power_method.py
# Method description:-
# This is a module script file for power method 
# Power method is an iterative method to find largest (or dominant) eigenvalue and coressponding eigenvector
# In this method for a given problem matrix user takes a initial guess column vector and multiply with problem matrix
# A new column vector is the largest element of this column vector with magnitude is the dominant eigenvalue after 1st iteration and coressponding vector is eigenvector
###########
# Module function description:-
# This module contains the definition of function called 'power_method_new'  
# power_method_new(A,X, e,intprnt, pltn, max_iter)
# This function takes A,X,e,intprnt,pltn,max_iter as variable (or argument)                           
# A is the problem matrix, and it is a numpy array of order n                                                       
# X is the intial guess colmumn matrix, it is also a numpy array, of order equal to order of A                                         
# e is the tolerable error defined by user, this a real number means should be a float                                                      
# intprnt is a boolean variable should eneterd "True" if user wants to print intermediate iterations, otherwise "False" 
# pltn is a boolean variable should eneterd "True" if user wants to plot of largest eigenvalue vs number itretions graph otherwise "False" 
# max_iter is maximum number of iteration upto which user wants to iterate and this an integer  
############
# The outputs:-                                                                 
# The outputs of this function are number of iteration (k), dominant (or largest) eigenvalue (E), eigenvector (X) and tolerance (e) respectivley
# On condition of "True" intprnt and pltn it provides intermediate iteration and plot of largest eigenvaule vs number of iteration respectivley
#########################
# Example for use this module:- 
# from power_method import *
# A = np.array([[1,2,0,0,0],[2,1,2,0,0],[0,2,1,2,0],[0,0,2,1,2],[0,0,0,2,1]])
# X = np.array([1,2,3,2,1])
# e = 0.00001 
# intprnt = True
# pltn = True   
# max_iter = 10000 
# power_method_new(A,X, e,intprnt, pltn, max_iter)
#########################
import numpy as np                                              
import matplotlib.pyplot as plt                                                 
def power_method_new(A,X, e,intprnt, pltn, max_iter):                         # Defining the fuction which will be imported in input file                  
    t = True                                                                    
    X1= np.zeros(len(A))                                                       
    E1 = 1.0                                                                    
    k = 1                                                                       
    s=[0]  
    out = open("power_method.txt", "w")                                   # Creating a file called power_method.txt to record all print commands
    while t:                                                                    
        for i in range(len(A)):                                                 
            C = 0                                                               
            for j in range(len(A)):                                             
                C = C + A[i][j]*X[j]                                          # Matrix multiplication of problem matrix A and column matrix X
            X1[i] = C                                                         # Equating new multiplied coulumn matrix with X1 which is null column initially 
        for i in range(len(A)):                                                
             X[i] = X1[i]                                                     # Equating the initial guess X to new multiplied matrix X1 
        E = X[np.argmax(np.abs(X))]                                           # Defining E as the heighest number with sign from multiplied column matrix
        X = X/E                                                               # Dividing by E                              
        E = float(E)                                                            
        error = abs(E-E1)                                                     # Defining error as difference between two eigenvalue 
        E1 = E                                                                # Equating E1 to E so that in each next loop E1 should be the previous eigenvalue, tolerance can be calculated                                                                  
        t = error > e                                                         # Condition for itretion until the error is grater than tolerable error                   
        if intprnt == True:                                                   # Condition for intermediate print                    
            print('Result after Iteration {:d}'.format(k), file = out)        # Printing number of iteration   
            print('Dominant Eigen Value = {:.5f}'.format(E), file = out)      # Printing dominant (or largest) eigenvalue upto 5 decimal places
            print(' Eigen Vector: ', file = out)                                               
            print('X is: {}'.format(X), file = out)                           # Printing coressponding eigenvector upto 3 decimal places             
            np.set_printoptions(precision=3)                                        
            print('The tolerance is = {:.5f}'.format(error), file = out)       # Printing the tolerance upto 5 decimal places
            print('-------------------------------------------------------------------------', file = out)
        s.append(E)                                                           # Making a array of all eigenvalues
        if k>max_iter:                                                        # Condition for not convergent eigenvalue               
            print('Oops not convergent for the entered intial guess vector (X), permissable error (e) and allowed number of iteration (max_iter) please try another enteries from these three argument to get solution, since no solution therefore no graph :(', file = out)
            break                                                                                                                                
        k = k + 1                                                                                                                   
    s.remove(0)                                                               # Removing zero from array 's' of all eigenvalues              
    B = list(range(1, k))                                                       
    if pltn == True:                                                          # Condition for plot of eigenvalues vs number of itretion    
        plt.plot(B, s, 'r')                                                     
        plt.xlabel('Number of iteration')                                       
        plt.ylabel('Eigen value (or multiplicative factor)')                    
        plt.show()                                                              
    print('Result after final iteration = {:d}'.format(k), file = out)                         # Printing final number of iteration   
    print('Dominant eigenvalue {:.5f}'.format(E), file = out)                 # Printing final dominant (or largest) eigenvalue upto 5 decimal places              
    print('Coressponding Eigenvector =', file = out)                               
    print('X is: {}'.format(X), file = out)                                   # Printing final coressponding eigenvector upto 3 decimal places                       
    np.set_printoptions(precision=3)                                            
    print('The tolerance is = {:.5f}'.format(error), file = out)              # Printing the final tolerance upto 5 decimal places               
    print('-------------------- <> End of Itretion,congratulation you successfully executed the power method <> --------------------')
    out.close()
    return