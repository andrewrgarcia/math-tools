# -*- coding: utf-8 -*-
"""
Created on Thu Jan 30 16:32:05 2020

@author: garci
"""
'''A x = b matrix solver script
Andrew Garcia'''

import argparse
import numpy as np

# construct the argument parse and parse the arguments
ap = argparse.ArgumentParser()


ap.add_argument("-a","--A_array", nargs ='+', type=float,
                help="A matrix in Ax = b")
ap.add_argument("-da","--A_dim", nargs ='+',type=int,
                help="dimensions of A (type:'-d 6 6' for 6 x 6)")
ap.add_argument("-b", "--b_array", nargs ='+',type =float,
                help="b vector (or matrix) in Ax = b")
ap.add_argument("-db","--b_dim", nargs ='+',type=int,default=None,
                help="dimensions of b if b not vector (type:'-db 6 6' for 6 x 6)")

args = vars(ap.parse_args())

a, b = args["A_array"],args["b_array"]
dim_a, dim_b = args["A_dim"],args["b_dim"]

a,b = np.array(a),np.array(b)
a = a.reshape(dim_a)
b = b.reshape(dim_b) if dim_b is not None else b

x = np.linalg.solve(a, b)
print('A x = b')
print('\nA\n{} \nb\n{}\n\nx\n{}'.format(a,b,x))
