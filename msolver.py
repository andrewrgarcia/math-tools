# -*- coding: utf-8 -*-
"""
Created on Thu Jan 30 16:32:05 2020

@author: garci
"""
'''A x = b matrix solver script
Andrew Garcia
Last Update: 04/03/2022'''

import argparse
import numpy as np

ap = argparse.ArgumentParser()

ap.add_argument("-pA","--path", default= '', type =str,
                help="path to excel file containing A matrix e.g. A.xlsx")
ap.add_argument("-pb","--path_b", default= '', type =str,
                help="path to excel file containing b matrix e.g. b.xlsx")

ap.add_argument("-sA","--sheet", default= r'Sheet1', type =str,
                help="Sheet name of excel file containing A matrix (default: Sheet1)")
ap.add_argument("-sb","--sheet_b", default= r'Sheet1', type =str,
                help="Sheet name of excel file containing b vector or matrix (default: Sheet1)")

ap.add_argument("-A","--A_array", nargs ='+', type=float,
                help="A matrix in Ax = b")
ap.add_argument("-dA","--A_dim", nargs ='+',type=int,
                help="dimensions of A (type:'-d 6 6' for 6 x 6 matrix)")

ap.add_argument("-b", "--b_array", nargs ='+',type =float,
                help="b vector (or matrix) in Ax = b")
ap.add_argument("-db","--b_dim", nargs ='+',type=int,default=None,
                help="dimensions of b if b is a matrix (type:'-db 6 6' for 6 x 6 matrix)")

args = vars(ap.parse_args())


import string
import pandas as pd


def excel_matrix(book, sheet):
    df = pd.read_excel(book, sheet,header=None).to_numpy()
    return df
    

if len(args["path_b"]) == 0:
    b = args["b_array"]
    dim_b = args["b_dim"]
    b = np.array(b)
    b = b.reshape(dim_b) if dim_b is not None else b
else: 
    b = excel_matrix(args["path_b"], args["sheet_b"])


if len(args["path"]) == 0:

    a= args["A_array"]
    dim_a = args["A_dim"]
    
    a= np.array(a)
    a = a.reshape(dim_a)

else:
    a = excel_matrix(args["path"], args["sheet"])
    
x = np.linalg.solve(a, b)
print('')
print('A x = b')
print('\nA\n{} \nb\n{}\n\nx\n{}'.format(a,b,x))
