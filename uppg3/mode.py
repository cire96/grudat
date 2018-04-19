def mode(a):

    """ Returns the most common integer that occurs in a list of numbers, if two values are equally common the lowest is returned
        Timecomplexity: O(n).
        In the first loop the most common operators are to check if an element is in the hashtable and add keys or alter values of existing keys, all those are O(1) in time and they are performed n times in total.
        In the second loop the most common operator is to check all the keys. An O(1) timecomplex operator performed n times"""


    check = {}  #A dictionary (hashtable) to store the values and there number of occurences in
    
    for i in range (0,len(a)):

        if a[i] not in check:   #If the integer has not appeared before in the list, add it as a key to the hashtable and set its value to one
            check[a[i]] = 1
            
        elif a[i] in check:     #If the integer already has appeared in the list, upp its value by one.
            check[a[i]] += 1

    #Now check wich key has the highest value
    
    common = 0
    number = 0

    for i in range (0,len(a)):

        if check[a[i]] > number:    
            number = check[a[i]]
            common = a[i]

        elif check[a[i]] == number and a[i] < common:
            common = a[i]

    return common



a = [1, 2, 3, 2, 0, 4, 5, 1, 1]
b = [4, 5, 2, 4, 1, 4, 5, 6, 7, 7, 7]
c = [1, 2, 0, 0, 0, 0, 2, 5, 1, 4]

assert mode(a) == 1
#In b both 4 and 7 are equally common so I make sure that 7 is not returned
assert mode(b) == 4
assert mode(b) != 7
assert mode(c) == 0
