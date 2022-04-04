# Math tools by Andrew
Handy math tools to have.

## msolver.py

Solves the iconic **A x = b** matrix equation from a terminal Python function call.

#### The script has changed! See the quick examples below to learn 
In your command line/ terminal, type any of the following `python msolver.py` commands :

```ruby
#matrix "A" and vector "b" both specified in separate Excel files named **A.xlsx** and **b.xlsx**, respectively both in the local folder [i.e. in the same folder as msolver.py]:
python msolver.py -pA A.xlsx -pb b.xlsx

#matrix "A" specified in an Excel file named **A.xlsx** in the local folder and a "b" vector defined in the terminal as b = [6 6 6 3 3 3]:
python msolver.py -pA A.xlsx -b 6 6 6 3 3 3

#LINUX: matrix "A" specified in an Excel file named **A2.xlsx** in the Desktop directory and a "b" vector specified in an Excel file **b.xlsx** in the local folder:
python msolver.py -pA $HOME/Desktop/A2.xlsx -pb b.xlsx

'''matrix "A" and vector "b" both specified IN the terminal (not recommended for large matrices) 
A = | 1  4 3 |
 	| 2  3 1 |
 	| 2 10 2 |
b = | 12 |	
	| 43 |
	| 65 |
	''':
python msolver.py -A 1 4 3 2 3 1 2 10 2 -dA 3 3 -b 12 43 65

```

#### Old video

<a href="https://youtu.be/J4ynp58c0AA"><img src="figures/yt_logo.png" alt="drawing" width="400"/></a>
