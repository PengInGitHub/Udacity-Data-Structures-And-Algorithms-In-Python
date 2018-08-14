#https://www.youtube.com/watch?v=YlgPi75hIBc
class Node:
    def __init__(self, value):
        self.value = value
        self.leftChild = None
        self.rightChild = None

    def insert(self, data):
        print "insert called, data: ", data
        if self.value == data:
            print "self.value == data:: ", self.value, data
            return False # value already exists, return False
       
        elif self.value > data:
            print "self.value > data:: ", self.value, data
            if self.leftChild: # if there is a left child
                print "there is a left child, self.leftChild.insert(data): ", data, "self.value: ",self.value
                self.leftChild.insert(data)
            else:
                print "there is no left child,, self.leftChild = Node(data): ", data, "self.value: ",self.value
                self.leftChild = Node(data)
                return True
        else:
            print "self.value < data:: ", self.value, data
            if self.rightChild:
                print "there is a right child, self.rightChild.insert(data): ", data, "self.value: ",self.value
                self.rightChild.insert(data)
            else:
                print "there is no right child,, self.rightChild = Node(data): ", data, "self.value: ",self.value
                self.rightChild = Node(data)
                return True

    def find(self, data):
        if self.value == data:
            return True
        elif self.value > data:
            if self.leftChild:
                return self.leftChild.find(data)
            else:
                return False
        else:
            if self.rightChild:
                return self.rightChild.find(data)
            else:
                return False
    
    def preorder(self):
        if self:
            print str(self.value)
            if self.leftChild:
                self.leftChild.preorder()
            if self.rightChild:
                self.rightChild.preorder()

    def postorder(self):
        if self:
            if self.leftChild:
                self.leftChild.postorder()
            if self.rightChild:
                self.rightChild.postorder()
            print str(self.value)
 
    def inorder(self):
        if self:
            if self.leftChild:
                self.leftChild.inorder()
            print str(self.value)
            if self.rightChild:
                self.rightChild.inorder()

class Tree:
    def __init__(self):
        self.root = None
    
    def insert(self, data):
        if self.root:
            self.root.insert(data)
        else:
            self.root = Node(data)
            return True # return to user if the node (data) is added
    
    def find(self, data):
        if self.root:
            self.root.find(data)
        else:
            return False

    #traversal func
    #all the traversal func use the root node to call a RECURSIVE traversal func
    def preorder(self):
        print "PrePrder"
        self.root.preorder()

    def postorder(self):
        print "PostOrder"
        self.root.postorder()
        
    def inorder(self):
        print "InOrder"
        self.root.inorder()   

#instantiate
bst = Tree()
bst.insert(10)
bst.insert(7)
bst.insert(17)
bst.insert(20)
bst.insert(21)
bst.insert(5)
bst.insert(30)

print bst.find(20)
print bst.find(19)

bst.preorder()
bst.postorder()
bst.inorder()