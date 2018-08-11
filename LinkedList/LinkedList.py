class Element(object):
    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedList(object):
    def __init__(self, head=None):
        self.head = head
    
    def append(self, newElement):
        current = self.head
        if self.head:
            while current.next :
                current = current.next
            current.next = newElement #current.next instead of newElement
        else:
            self.head = newElement
    
    def get_position(self, position):
        current = self.head        
        for i in range(1, position+1):
            if current != None:
                if i == position:
                    return current
                current = current.next
            else:
                return None
    def get_length(self):
        current = self.head
        counter = 1
        if self.head:                
            while current.next:
                counter += 1
                current = current.next
            return counter 
        return 0    

    def insert(self, newElement, position):
        current = self.head
        currentPosition = 1
 
        if position < 1:
            return None
        elif position == 1:
            newElement.next = self.head
            self.head = newElement    
        elif position > self.get_length():
            self.append(newElement)    
        else:
            while current.next and (currentPosition<position):
                if currentPosition == position - 1:
                    newElement.next = current.next
                    current.next = newElement
                current = current.next
                currentPosition += 1

    def delete(self, value):
        current = self.head
        previous = None
        while current.value != value and current.next:
            previous = current
            current = current.next    

        if current.value == value:
            if previous:
                previous.next = current.next
            else:
                self.head = current.next

# Test cases
# Set up some Elements
e1 = Element(1)
e2 = Element(2)
e3 = Element(3)
e4 = Element(4)

# Start setting up a LinkedList
ll = LinkedList(e1)
ll.append(e2)
ll.append(e3)

# Test get_position
# Should print 3
print ll.head.next.next.value
# Should also print 3
print ll.get_position(3).value

# Test insert
ll.insert(e4,3)
# Should print 4 now
print ll.get_position(3).value

# Test delete
ll.delete(1)
# Should print 2 now
print ll.get_position(1).value
# Should print 4 now
print ll.get_position(2).value
# Should print 3 now
print ll.get_position(3).value