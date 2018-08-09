"""Write a HashTable class that stores strings
in a hash table, where keys are calculated
using the first two letters of the string."""

class HashTable(object):
    def __init__(self):
        self.table = [None]*10000

    def store_dict(self, string):
        """Input a string that's stored in 
        the table."""
        self.table.append({self.calculate_hash_value(string):string})

    def store(self, string):
        """Input a string that's stored in 
        the table."""
        hashValue = self.calculate_hash_value(string)
        if hashValue != -1:
            if  self.table[hashValue]  != None:
                self.table[hashValue].append(string)
            else:
                self.table[hashValue] = [string]
    def lookup(self, string):
        hashValue = self.calculate_hash_value(string)
        if hashValue != -1:
            if  self.table[hashValue]  != None:
                if string in self.table[hashValue]:
                    return hashValue
        return -1
        
    def lookup_dict(self, string):
        """Return the hash value if the
        string is already in the table.
        Return -1 otherwise."""
        for d in self.table:
          if d:
            for k in d.keys():
              if d[k] == string:
                return k
        return -1

    def calculate_hash_value(self, string):
        """Helper function to calulate a
        hash value from a string."""
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
