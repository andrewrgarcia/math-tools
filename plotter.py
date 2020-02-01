# -*- coding: utf-8 -*-
"""
Created on Fri Jan 31 13:29:16 2020

@author: garci
"""
'''plotter.py - A comprehensive python plotter
Andrew Garcia, 2020  '''

import argparse

ap = argparse.ArgumentParser()

'manual data importer - input values of x and y columns one-by-one'
ap.add_argument("-x","--x values", default = 13, nargs ='+', type=float,
                help="x values with values spaced out (e.g. 4 31 13 23)")
ap.add_argument("-y","--y values", default = 13,nargs ='+', type=float,
                help="y values with values spaced out (e.g. 4 31 13 23)")

'database importer - load x,y data from excel file(s)'
ap.add_argument("-p", "--path", nargs = '+', type =str,
                help="paths to datasets to plot")
ap.add_argument("-s", "--sheet", default='Sheet1',
                help="name of sheet containing dataset")
ap.add_argument("-xd", "--xcolumn", default='A1',
                help="column with x data")
ap.add_argument("-yd ", "--ycolumn", default='B1',
                help="column with y data")

ap.add_argument("-lx","--x label", default = 'x', help="x label")
ap.add_argument("-ly","--y label", default = 'y', help="y label")
ap.add_argument("-t","--title", default = '', help="plot title")

args = vars(ap.parse_args())

'''lastRow credit: answered Sep 14 '16 at 11:39  -  Stefan
https://stackoverflow.com/questions/33418119/xlwings-function-to-find-the-last-row-with-data'''
def lastRow(idx, workbook, col=1):
    """ Find the last row in the worksheet that contains data.

    idx: Specifies the worksheet to select. Starts counting from zero.
    workbook: Specifies the workbook
    col: The column in which to look for the last cell containing data.
    """

    ws = workbook.sheets[idx]

    lwr_r_cell = ws.cells.last_cell      # lower right cell
    lwr_row = lwr_r_cell.row             # row of the lower right cell
    lwr_cell = ws.range((lwr_row, col))  # change to your specified column

    if lwr_cell.value is None:
        lwr_cell = lwr_cell.end('up')    # go up untill you hit a non-empty cell

    return lwr_cell.row


import matplotlib.pyplot as plt
def make():
    import xlwings as xw
    paths = args["path"]
    plt.style.use("ggplot")

    for path in paths:
        idx = args["sheet"]
        book=xw.Book(path)
        x = book.sheets[idx].range( args["xcolumn"] + ':' + args["xcolumn"][0]+str(lastRow(idx,book)) ).value
        y = book.sheets[idx].range( args["ycolumn"] + ':' + args["ycolumn"][0]+str(lastRow(idx,book)) ).value
        plt.plot(x,y)
#        plt.plot(x,y,label=path)
        book.close()

    plt.title(args["title"])
    plt.xlabel(args["x label"])
    plt.ylabel(args["y label"])
#    plt.legend()
    plt.show()

def manual():
    x, y = args["x values"], args["y values"]
    plt.style.use('ggplot')
    plt.plot(x,y,'o')
    plt.title(args["title"])
    plt.xlabel(args["x label"])
    plt.ylabel(args["y label"])
    plt.show()
    print(x,y)

make() if args["path"] is not 'C:\[path]\[file].xlsx' else manual()
