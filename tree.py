import random

class tree(object):

    def __init__(self,data = None, left_branch = None, right_branch = None):

        self.node = data
        self.left_branch = left_branch
        self.right_branch = right_branch
        self.priority = random.randint(1,10001)
        self.seize = 0

    def add_element(self, data):

        if self.node == data:
            return self

        if self.node != None:

            
            if self.node > data and self.left_branch == None:
                self.left_branch = tree(data)
                

            elif self.node > data and self.left_branch != None:
                self.left_branch = self.left_branch.add_element(data)

            elif self.node < data and self.right_branch == None:
                self.right_branch = tree(data)
                

            elif self.node < data and self.right_branch != None:
                self.right_branch = self.right_branch.add_element(data)


        elif self.node == None:
            self.node = data

        self.rotate_left()
        self.rotate_right()
        self.seize += 1

        return self
        
        

    def rotate_left(self):

        if self.right_branch != None:
            if self.right_branch.priority > self.priority:

                temp = tree(self.node, self.left_branch, self.right_branch.left_branch)
                self.node = self.right_branch.node
                self.left_branch = temp
                self.right_branch = self.right_branch.right_branch
                

    def rotate_right(self):

        if self.left_branch != None:
            if self.left_branch.priority > self.priority:

                temp = tree(self.node, self.left_branch.right_branch, self.right_branch)
                self.node = self.left_branch.node
                self.right_branch = temp
                self.left_branch = self.left_branch.left_branch

        

    def print_tree(self):

        if self.node != None:
            
            if self.left_branch != None:
                self.left_branch.print_tree()

            print(self.node)
            
            if self.right_branch != None:
                self.right_branch.print_tree()

            


    

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
    test.add_element("6346346.")
    test.add_element("l")
    test.add_element("h")
    test.add_element("g")
    test.add_element("p")

    assert test.node > test.left_branch.node
    assert test.node < test.right_branch.node
    assert test.priority > test.left_branch.priority
    assert test.priority > test.right_branch.priority
    assert test.seize == 8
    
    test.print_tree()
    


main()
    



