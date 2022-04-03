# -*- coding: utf-8 -*-
"""
Created on Thu Jan 30 16:32:05 2020

@author: garci
"""
'''A x = b matrix solver script
Andrew Garcia
Last Update: 02/21/2020'''

import argparse
import numpy as np

# construct the argument parse and parse the arguments
ap = argparse.ArgumentParser()

ap.add_argument("-g","--excel_grid", default = False, type = bool,
                help="'a' matrix declaration: one line terminal input [False] (small matrices) \
                or extract from Excel file  [True](large matrices) [default: False]")
ap.add_argument("-gb","--excel_grid_b", default = False, type = bool,
                help="'b' vector/matrix declaration: one line terminal input [False] \
                (vectors only) or extract from Excel file  [True](large matrices) \
                [default: False]")

ap.add_argument("-p","--path", default= r'Book.xlsx', type =str,
                help="path to excel file containing A matrix")
ap.add_argument("-pb","--path_b", default= r'Book2.xlsx', type =str,
                help="path to excel file containing b matrix")

ap.add_argument("-s","--sheet", default= r'Sheet1', type =str,
                help="Sheet name of excel file containing A matrix (default: Sheet1)")
ap.add_argument("-sb","--sheet_b", default= r'Sheet1', type =str,
                help="Sheet name of excel file containing b vector or matrix (default: Sheet1)")

ap.add_argument("-a","--A_array", nargs ='+', type=float,
                help="A matrix in Ax = b")
ap.add_argument("-da","--A_dim", nargs ='+',type=int,
                help="dimensions of A (type:'-d 6 6' for 6 x 6 matrix)")


ap.add_argument("-b", "--b_array", nargs ='+',type =float,
                help="b vector (or matrix) in Ax = b")
ap.add_argument("-db","--b_dim", nargs ='+',type=int,default=None,
                help="dimensions of b if b is a matrix (type:'-db 6 6' for 6 x 6 matrix)")

args = vars(ap.parse_args())


# import xlwings as xw
import string
import pandas as pd


def excel_matrix(book, sheet):
    # b00k=xw.Book(book) 
    # df=pandas.read_excel(book,sheet)
    # m,n= df.shape
    # m=m+1
    # lastcol=list(string.ascii_lowercase)[n-1]
    # mat = b00k.sheets[sheet].range('a1:'+lastcol+str(m)).value
    # mat = np.array(mat).reshape(m,n)
    # b00k.close() 
    # return mat
    df = pd.read_excel(book, sheet,header=None).to_numpy()
    return df
    

if args["excel_grid_b"] is False:
    b = args["b_array"]
    dim_b = args["b_dim"]
    b = np.array(b)
    b = b.reshape(dim_b) if dim_b is not None else b
else: 
    b = excel_matrix(args["path_b"], args["sheet_b"])

if args["excel_grid"] is False:
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
