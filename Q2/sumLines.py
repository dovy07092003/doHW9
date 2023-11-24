# Name: sumLines.py
# This program will read numbers from a text file and returns
# sum, number of integers, and average 
# Based on the tme.py file 

import sys

# Start for loop
def checkline():
    global l
    global word_count
    w = l.split() # Split the string into a list of words
    word_count += len(w) # return # of elements in a list
# End of def

word_count = 0
f = open(sys.argv[1]) # Open a file, f is a pointer
flines = f.readlines() # Return # of lines in the file
line_count = len(flines)
for l in flines:
    checkline()
print("Number of lines ", line_count)
print("Number of elements ", word_count)

# Start for loop
total = 0
for line in flines: # Let line run in the range of # lines
    for ele in line.split(): # For each element in the line(split the string into a list of numbers"
        if len(ele) != 0: # If the number of the strin isn't 0 = not a blank string
            total += int(ele) # Change from string to integer type
# End for loop

ave = total/word_count;
print("The sum of all elements are", total)
print(total, word_count, ave) 
