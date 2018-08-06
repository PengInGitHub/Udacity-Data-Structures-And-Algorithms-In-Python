class Element(object):
    def __init__(self, value): #use __init__ to initialize an Element
        self.value = value #each element associated with a value
        self.next = None #each element has a variable points to the next element

class LinkedList(object):
    def __init__(self, head=None):
        self.head=head #first element in the lsit
    def append(self, new_element):
        current = self.head #if the LinkedList already has head
        if self.head:
            while current.next: #iterate over the next element
                current = current.next
            current.next = new_element
        else:
            self.head = new_element
                
            
        
