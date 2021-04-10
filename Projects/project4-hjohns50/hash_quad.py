class Node:

    def __init__(self, val, data):
        self.val = val
        if type(data) == list:
            self.data = data
        else:
            self.data = [data]

    def __repr__(self):
        return "[%s, %s]" % (self.val, self.data)
        
class HashTable:

    def __init__(self, table_size):         # can add additional attributes
        self.table_size = table_size        # initial table size
        self.hash_table = [None]*table_size # hash table
        self.num_items = 0                  # empty hash table
    #str, any -> nothing
    #inserts key-value pair into hash table using quadratic probing
    def insert(self, key, value=None):
        ''' Inserts an entry into the hash table (using Horner hash function to determine index, 
        and quadratic probing to resolve collisions).
        The key is a string (a word) to be entered, and value is any object (e.g. Python List).
        If the key is not already in the table, the key is inserted along with the associated value
        If the key is is in the table, the new value replaces the existing value.
        If load factor is greater than 0.5 after an insertion, hash table size should be increased (doubled + 1).'''
        if type(key) != str: #catches non-string items
            raise TypeError("Invalid Token")
        elif type(key) == str:
            node = Node(key, value) #creates a node to insert to hold the key-value pair
            horn = self.horner_hash(key) #uses key to find index
            col = 0 #collision counter
            insert = False
            index = (horn + col**2)
            while insert is False:
                if index >= self.table_size - 1:
                    index -= self.table_size
                if self.hash_table[index] is None: #makes sure spot is empty for insertion
                    self.hash_table[index] = node 
                    self.num_items += 1
                    if self.get_load_factor() > .5: #checks load factor for rehashing
                        self.rehash()
                    insert = True
                elif self.hash_table[index] != None: #either changes the value aspect or adds 1 to col
                    if self.hash_table[index].val == key:
                        self.hash_table[index].data.append(value)
                        insert = True
                    else:
                        col +=1 
                        index = (horn + col**2) % self.table_size
        
    #none -> none
    #grows the hash table and re-inserts items
    def rehash(self):
        new_ts = (self.table_size * 2) + 1
        new_ht = [None] * new_ts
        old_ht = self.hash_table
        self.num_items = 0 #resets hash table to new parameters
        self.hash_table = new_ht
        self.table_size = new_ts
        for i in old_ht:
            if i != None:
                self.insert(i.val, i.data)
    #str -> int
    #uses horners functon to create a index
    def horner_hash(self, key):
        ''' Compute and return an integer from 0 to the (size of the hash table) - 1
        Compute the hash value by using Horner’s rule, as described in project specification.'''
        i = 0 
        horn = 0
        n = min(8, len(key))
        while i < n:#sums up the ASCII Values and multiplies them 
            horn += ord(key[i]) * (31**(n-1-i))
            i += 1
        hashed = horn % self.table_size #mods by table size
        return hashed

    #str -> boolean
    #takes a key and checks to see if it's in the hash table
    def in_table(self, key):
        ''' Returns True if key is in an entry of the hash table, False otherwise.'''
        horn = self.horner_hash(key) #finds the horner value
        col = 0 #collision counter
        found = False
        while found is False:
            index = (horn + col**2) % self.table_size
            if self.hash_table[index] == None:
                return False #if it's not then returns false
            elif self.hash_table[index].val == key:
                found = True
                return True #returns true if in table
            else:
                col += 1 #updates collision counter
    
    #str -> int
    #returns index of speciefied item
    def get_index(self, key):
        ''' Returns the index of the hash table entry containing the provided key. 
        If there is not an entry with the provided key, returns None.'''
        horn = self.horner_hash(key) #gets horn value 
        col = 0 #collision counter
        found = False
        while found is False:
            index = (horn + col**2) % self.table_size
            if self.hash_table[index] == None:
                return None #if not found returns none
            elif self.hash_table[index].val == key:
                found = True
                return index #returns index
            else:
                col += 1 #updates col
    #None -> List
    #returns a list of all keys in the hashtable
    def get_all_keys(self):
        ''' Returns a Python list of all keys in the hash table.'''
        key_lst = [] #list of keys
        for i in self.hash_table:
            if i != None:
                key_lst.append(i.val) #appends only items with value to key_lst
        return key_lst

    #str -> node element
    #takes a key and returns corresponding value
    def get_value(self, key):
        ''' Returns the value associated with the key. 
        If key is not in hash table, returns None.'''
        horn = self.horner_hash(key) #gets horner value
        col = 0 #collsion counter
        found = False
        while found is False:
            index = (horn + col**2) % self.table_size
            if self.hash_table[index] == None:
                return None #returns none if not found
            elif self.hash_table[index].val == key:
                found = True 
                return self.hash_table[index].data #returns data from node with corresponding data
            else:
                col += 1 #updates col

    def get_num_items(self):
        ''' Returns the number of entries in the table.'''
        return self.num_items

    def get_table_size(self):
        ''' Returns the size of the hash table.'''
        return self.table_size

    def get_load_factor(self):
        ''' Returns the load factor of the hash table (entries / table_size).'''
        return self.num_items / self.table_size
