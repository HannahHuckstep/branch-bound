# Hannah Huckstep
# Lab test 2
# Dec 1st 2014 8pm


# need an upper bound function

# need a lower bound function

##You should consider at least two different options
##for the lower bound and two for the upper bound.
##I will leave the details up to you, but at least one
##of the lower bound methods should include the row and
##column reduction method we looked at in class. Some
##upper bound suggestions : random selection, greedy
##heuristics, exhaustive search when the problem is small 

# define a min heap 

# need a CSF function(cost so far) 

# ?? need a GSF function(greedy so far?)

# ?? need a FC function(feasible cost)

import random

def main():
    file = open('data1.txt', 'r')
    testcase = file.readlines()

    num_array = txt_into_array(testcase)

    int_array = ArrayFormat(num_array)
    print int_array

    upper_b_r = upper_bound_rand(num_array)
    print "Rand Upper Bound:", upper_b_r

    upper_b_e = upper_bound_exhaustive(num_array)
    print "Exhaustive Upper Bound:", upper_b_e

def txt_into_array(testcase):
 
    # takes the data and makes it into a 2D array 
    dataset = []

    for i in range(1,len(testcase)):
        current = testcase[i].split('\t')
        dataset.append(current)

    # removing '\n', " ", and ""
    n = len(dataset) 
        
    for i in range(0,n):
        if ("\n") in dataset[i]:
            dataset[i].remove('\n')
        if ("") in dataset[i]:
            dataset[i].remove("")
        if (" ") in dataset[i]:
            dataset[i].remove(" ")

    # turning into numbers
    for i in range(0,n):
        for j in range (0,len(dataset[i])):
            dataset[i][j] = int(dataset[i][j])
    return dataset



def ArrayFormat(array):

    # printing array in an easy to read format
    for i in range (0,len(array)):
        print array[i]

def upper_bound_rand(num_array):

    # pickes a random index number from each row
    # adds the index's value to upper, and then sums it.
    upper= []
    for i in range(0, len(num_array)):
        n = random.randint(1, len(num_array)-1)
        upper.append(num_array[i][n])
        upper_b = sum(upper)Gi
    return upper_b

#def upper_bound_greedy(num_array):
    

def upper_bound_exhaustive(num_array):
    upper = []
    if len(num_array) <= 35:
        for i in range(0, len(num_array)):
            for j in range(0, len(num_array)):
                biggest = max(num_array[i])
            upper.append(biggest)
            upper_b = sum(upper)
        return upper_b
                
    

main()
