import random

class tree(object):

    def __init__(self,data = None):

        self.node = data
        self.left_branch = None
        self.right_branch = None
        self.factor = random.randint(1,101)

    def add_element(self, data):

        if self.node != None:

            
            if self.node > data and self.left_branch == None:
                self.left_branch = tree(data)
                

            elif self.node > data and self.left_branch != None:
                self.left_branch.add_element(data)

            elif self.node < data and self.right_branch == None:
                self.right_branch = tree(data)
                

            elif self.node < data and self.right_branch != None:
                self.right_branch.add_element(x, data)

        elif self.node == None:
            self.node = data

        
        

    def rotate_left(self):

        if self.right_branch.node > self.node:
            temp = self.right_branch
            self.right_branch = temp.left_branch
            temp.left_branch = self

    def rotate_right(self):

        if self.left_branch.node > self.node:
            temp = self.left_branch
            self.left_branch = temp.right_branch
            temp.right_branch = self            

        

    def print_tree(self):

        if self.node != None:
            
            if self.left_branch != None:
                self.left_branch.print_tree()

            print(self.node)
            
            if self.right_branch != None:
                self.right_branch.print_tree()

            


    

def main():
    test = tree()
    test.add_element("b")
    test.add_element("a")
    test.add_element("c")


    test.print_tree()
    


main()
    



