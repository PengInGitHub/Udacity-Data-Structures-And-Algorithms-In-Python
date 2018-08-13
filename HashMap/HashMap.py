"""Write a HashTable class that stores strings
in a hash table, where keys are calculated
using the first two letters of the string."""

class HashTable(object):
    def __init__(self):
        self.table = [None]*10000

    def store(self, string):
        """Input a string that's stored in 
        the table."""
        hv = self.calculate_hash_value(string)
        if hv != -1:
            if self.table[hv] != None:
                #append
                self.table[hv].append(string)
            else:
                #add new list
                self.table[hv] = [string]
        
        
    def lookup(self, string):
        """Return the hash value if the
        string is already in the table.
        Return -1 otherwise."""
        hv = self.calculate_hash_value(string)
        if hv != -1:
            if self.table[hv] != None: # already exists
                return hv

        return -1


    def calculate_hash_value(self, string):
        if len(string) >= 2:
            return ord(string[0])*100 + ord(string[1])
        return -1
    
# Setup
hash_table = HashTable()

# Test calculate_hash_value
# Should be 8568
print hash_table.calculate_hash_value('UDACITY')

# Test lookup edge case
# Should be -1
print hash_table.lookup('UDACITY')

# Test store
hash_table.store('UDACITY')
# Should be 8568
print hash_table.lookup('UDACITY')

# Test store edge case
hash_table.store('UDACIOUS')
# Should be 8568
print hash_table.lookup('UDACIOUS')
