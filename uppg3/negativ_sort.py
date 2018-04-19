import random

def zero_sort(a):

    """ Sorts the list a so that all negative elements in the list are to the left
        Timecomplexity: O(n)"""
    
    j = 0     #refers to the index of the last moved negative element in the list
    for i in range(0, len(a)):

        """
        Invariant: [ x<0 :j: y >= 0  ], all elements to the left of index j, and including j is sorted so that all negative numbers are to the left and all positive numbers are to the right
        Initiation: Before the first iteration j is outside of the list and therefore there are no elements to sort and so by default they are sorted
        Iteration: The invariant is true both before and after the the loop
        Termination:
        """

        if a[i] < 0:   #if the element at index i is negative

            #change place with the element at index j
            
            temp = a[j]     
            a[j] = a[i]
            a[i] = temp
            j += 1 

        
def main():

    v = [0, 1,-1, 4, -3, 0, -2, 8, -5,-4, 7]
    zero_sort(v)

    x = [3, -2, 1]
    zero_sort(x)

    y = random.sample(range(-100,100), 30)
    print(y)
    zero_sort(y)
    print(y)

    assert x == [-2, 3, 1]
    assert v == [-1, -3, -2, -5, -4, 0, 0, 8, 4, 1, 7]
    



main()
