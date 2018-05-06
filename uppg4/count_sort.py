
import random

def count_sort(v):

    """ Sorts a list of positive integers in ascending order
        Timecomplexity: O(n+k) where k is the largest integer in the list"""
    
    biggest = v[0]


    for i in range (0, len(v)):     #finds the biggest number in the list
        if v[i] > biggest:
            biggest = v[i]
            

    elements = [0] * (biggest+1)    #A list where the entry at index i is the number of times i occurs in the list v
    

    for i in range(0,len(v)):      

        elements[v[i]] += 1


    sorted_list = [0]*len(v)        #Create the sorted list that will be returned
          
    counter = 0
    for i in range(0,len(elements)):
        for j in range(0,elements[i]):
            sorted_list[counter] = i
            counter += 1

    return sorted_list


y = random.sample(range(0,100), 50)
x = count_sort(y)


for i in range(1,len(x)):
    assert x[i-1] <= x[i]



