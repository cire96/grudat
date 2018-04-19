import random

class tree(object):

    def __init__(self,data = None, left_branch = None, right_branch = None, prio = 0):
        """ Stores a string, two refrences too other instances of this object, a priority integer and the seize of the tree: O(1) """

        self.node = data
        self.left_branch = left_branch
        self.right_branch = right_branch
        if prio == 0:
            self.priority = random.randint(1,101)
        else:
            self.priority = prio
            
        self.seize = 0
        

    def add_element(self, data):

        """ Adds an element to the tree structure so that all values in the right branch are "higher" then th previous one and all values in the left branch are smaller then the previous one: O(log(n)) """

        if self.node == data: #If the value already exists nothing happens, there are no doubles in the tree
            return self

        if self.node != None: #The node is only empty the first time you add a value 

            #Checks where the value should be places, in the left or right branch and wether that branch is empty
            
            if self.node > data and self.left_branch == None: 
                self.left_branch = tree(data) # if the branch is empty, create a new tree
                

            elif self.node > data and self.left_branch != None:
                self.left_branch = self.left_branch.add_element(data) # if the branch is not empty, call the add function on thtree in that branch

            elif self.node < data and self.right_branch == None:
                self.right_branch = tree(data)
                

            elif self.node < data and self.right_branch != None:
                self.right_branch = self.right_branch.add_element(data)


        elif self.node == None:
            self.node = data


        #After a new value has been added, these functions balances the nodes in the tree according to the priority number of each node
        self.rotate_left()  
        self.rotate_right()

        self.seize +=1  #Increase the seize of the tree by one

        return self
        
        

    def rotate_left(self):
        """ If the node in the right branch has a higher priority then this node, this function places the right node higher upp in the tree: O(log(n)) """
        if self.right_branch != None: #The right branch might be empty and then there is no point in checking
            
            if self.right_branch.priority < self.priority: 

                temp = tree(self.node, self.left_branch, self.right_branch.left_branch, self.priority) #create a new tree, same as the old one but change the right branch so that it the same as the left branch of the right branch
                
                self.node = self.right_branch.node   #Change the node so that it becomes the node in the right branch except with the new node as the left branch
                self.priority = self.right_branch.priority
                self.left_branch = temp
                self.right_branch = self.right_branch.right_branch
                

    def rotate_right(self):

        """ If the node in the left branch has a higher priority then this node, this function places it higher upp in the tree: O(log(n)) """

        if self.left_branch != None: # The left branch might be empty and then there is no point in checking
            if self.left_branch.priority < self.priority:

                temp = tree(self.node, self.left_branch.right_branch, self.right_branch, self.priority) # create a new tree, same as the old one but change the left branch so that it is tha same as the right branch of the left branch

                self.node = self.left_branch.node # Change the node so that it becomes the node in the left branch except with the new node as the left branch
                self.priority = self.left_branch.priority
                self.right_branch = temp
                self.left_branch = self.left_branch.left_branch

        

    def print_tree(self):

        """ Prints all of the nodes in the tree in order: O(n) """

        if self.node != None: #If the tree is empty nothing should happen
            
            if self.left_branch != None: #First print the left branch
                self.left_branch.print_tree()

            print(self.node) #If the left branch is empty, print the node
            
            if self.right_branch != None: #Then, print the right branch
                self.right_branch.print_tree()

    def length(self):

        """ Returns the seize of the tree: O(1) """
        
        return self.seize


            


    

def main():
    test = tree()

    assert test.node == None
    assert test.seize == 0
    
    test.add_element("m")

    assert test.node != None
    assert test.left_branch == None
    assert test.right_branch == None
    assert test.seize == 1
    
    test.add_element("a")
    test.add_element("b")
    test.add_element("gg")
    test.add_element("l")
    test.add_element("h")
    test.add_element("g")
    test.add_element("t")
    test.add_element("j")
    test.add_element("v")
    test.add_element("c")
    test.add_element("x")
    test.add_element("pz")
    test.add_element("ps")
    test.add_element("pa")
    test.add_element("pr")
    test.add_element("ph")
    

    assert test.node > test.left_branch.node
    assert test.node < test.right_branch.node
    assert test.priority <= test.left_branch.priority
    assert test.priority <= test.right_branch.priority
    assert test.length() == 17
    
    test.print_tree()
    


main()
    



