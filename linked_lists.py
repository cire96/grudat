class List_element(object):
    """ An element in a linked list with one field for the data stored and one for the link """

    def __init__(self, data, next_element):

        """ Creates two fields, one for the stored data and one for the reference to the next element
        """
        self.stored_data = data      #holds the stored value
        self.link = next_element     #holds the pointer to the next object


class Linked_list(object):

    """ A ordered list of information where each element contains the refernce to the next """

    def __init__(self):

        """ Creates three fields, one reference too the first element of the list, one referense too the last
        and one that holds the number of elements in the list """
        
        self.first_element = None   #holds the reference to the first element
        self.last_element = None    #holds the reference to the last element
        self.number_of_elements = 0 #the number of elements in the list

    def add_first(self, data):

        """ Ads a new element to the beginning of the list """
        if self.first_element == None:  #If the list is empty
            self.first_element = List_element(data,None) #Create the new element
            self.last_element = self.first_element      #The last and the first element are the same if there are no other elements
            
        else:       #If the list is not empty
            self.first_element = List_element(data, self.first_element)     #Create a new object with the that points to the current first object

        self.number_of_elements += 1 #Increases the number of elements in the list by one
        
    def add_last(self, data):

        """ Ad a new element to the end of the list """

        if self.last_element == None:   #If the list is empty
            self.last_element = List_element(data, None) #Create the new object
            self.first_element = self.last_element      #The last and first element are the same if there are no other elements
            
        else:
            temp = List_element(data, None) #Create a new element
            self.last_element.link = temp   #Make the current last element point to the new element
            self.last_element = temp        #Replace the former last element with the new

        self.number_of_elements += 1

    def get_index(self, i):

        """ Returns the stored data in the element with index i """
        
        if self.number_of_elements > 0: #Loops through the list until you get the refferenced 
            temp = self.first_element
            for j in range (1, i):
                temp = temp.link
            data = temp.stored_data
            return data
        else:
            return None             #If the list is empty return None

    def get_first(self):

        """ Returns the stored data in the first element """
        
        if self.first_element != None:
            data = self.first_element.stored_data
            return data
        else:
            return None

    def get_last(self):

        """ Returns the stored data in the last element """
        
        if self.last_element != None:
            data = self.last_element.stored_data
            return data
        else:
            return None

    def remove_first(self):

        """ Removes the first element from the list """

        if self.number_of_elements == 1:
            self.last_element = None

        if self.number_of_elements != 0:
            temp = self.first_element
            self.first_element = temp.link
            self.number_of_elements -= 1
        
        

    def clear(self):

        """ Removes the entire list """
        
        self.first_element = None        #Remove the reference to the first element
        self.last_element = None         #Remove the reference to the last element
        self.number_of_elements = 0

    def seize(self):

        """ Gives the length of the list """
        
        return self.number_of_elements
    
    def get_string(self):

        """ Returns all the data stored in the list """
        
        if self.number_of_elements > 0:
            
            r = [self.first_element.stored_data]
            temp = self.first_element
            for j in range (1, self.number_of_elements):
                temp = temp.link
                r.append(temp.stored_data)
            return r
        
        else:
            return None

    def healthy(self):

        """ Checks if the list meets three conditions
1) If the number of elements in the list are equal to its seize
2) If the list is empty both last_element and first element both have the value None
3) The last element in the list have a null value as reference to the next element """

        check1 = False  #Value for the first condition
        check2 = False  #Value for the second condition
        check3 = False  #Value for the last condition

        temp = self.first_element
        length = 0
        while temp:
            length +=1
            temp = temp.link

        if length == self.number_of_elements: #Checks the first condition
            check1 = True

            
        if self.number_of_elements == 0 and self.first_element == None and self.last_element == None:   #Checks the second condition
            check2 = True
        elif self.number_of_elements != 0 and self.first_element != None and self.last_element != None:     #if the list is not empty you can't check the second condition
            check2 = True
            

        if self.number_of_elements > 0:     #Checks the third condition
            if self.last_element.link == None:
                check3 = True
        if self.number_of_elements == 0:
            if self.last_element == None and self.first_element == None:

                check3 = True

        if check1 and check2 and check3:
            return True
        else:
            return False
        


def main():

    """ Create a empty list """

    test = Linked_list()
    
    assert test.seize() == 0
    assert test.get_first() == None
    assert test.get_last() == None
    assert test.get_string() == None
    assert test.healthy() == True

    """ Add an element to the beginning of the list """
    
    test.add_first("Hello")
    
    assert test.seize() == 1
    assert test.get_first() == "Hello"
    assert test.get_last() == "Hello"
    assert test.get_string() == ['Hello']
    assert test.healthy() == True

    """ Add an element to the end of the list """
    
    test.add_last("World")

    assert test.seize() == 2
    assert test.get_first() == "Hello"
    assert test.get_last() == "World"
    assert test.get_string() == ['Hello', 'World']
    assert test.healthy() == True

    """ Add a new element to the beginning of the list """

    test.add_first(4)
    
    assert test.seize() == 3
    assert test.get_first() == 4
    assert test.get_index(1) == 4
    assert test.get_index(2) == "Hello"
    assert test.get_index(3) == "World"
    assert test.get_last() == "World"
    assert test.get_string() == [4, "Hello", "World"]
    assert test.healthy() == True

    """ Remove the first from the list """

    test.remove_first()

    assert test.seize() == 2
    assert test.get_first() == "Hello"
    assert test.get_last() == "World"
    assert test.get_string() == ['Hello', 'World']

    """ Clear the entire lit """
    
    test.clear()
    
    assert test.seize() == 0
    assert test.get_first() == None
    assert test.get_last() == None
    assert test.get_string() == None
    assert test.healthy() == True

    """ Add two list element on top of each other """
    
    test.add_first(5)
    test.add_first(3)

    assert test.seize() == 2
    assert test.get_first() == 3
    assert test.get_last() == 5
    assert test.healthy() == True

    """ Remove the two first elements two too se if it is the same as clearing the list """

    test.remove_first()
    test.remove_first()

    assert test.seize() == 0
    assert test.get_first() == None
    assert test.get_last() == None
    assert test.healthy() == True


main()
