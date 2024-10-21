sequence = [0]
L = int(input("Length of sequence: ")) # this should be your only input
if L > 0:
    sequence.append(1)
for i in range(2,L):
    newNum = sequence[i-1] - (i)
    if newNum <= 0:
        newNum = sequence[i-1] + (i)
    elif (newNum in sequence) == True:
        newNum = sequence[i-1] + (i)

    sequence.append(newNum)

    
# Your code for the Recaman Sequence
# You should stire the sequence in an appropriate data structure named 'sequence'

# You may wish to use further output for testing purposes while you develop your code
# Please remove any extra output before submitting to Gradescope
    

# your only output for submission should be the final sequence
#[ print(item) for item in sequence ]    # this method is reasonably independent of the choice of data structure
print(sequence)