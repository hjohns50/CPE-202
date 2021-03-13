
class LookupError(Exception):
    pass

class MyHashTable:

    def __init__(self, table_size = 11):
        self.table_size = table_size
        self.hash_table = [[] for i in range(table_size)]
        self.num_items = 0
    
    def insert(self, key, item):
        pair = (key, item)
        index = key % self.table_size
        lst = self.hash_table[index]
        for i in range(len(lst)):
            if lst[i][0] == key:
                lst[i] = pair
                print("yes")
                return
        self.hash_table[index].append(pair)
        self.num_items += 1
        if self.load_factor() > 1.5:
            self.rehash()
            return
        else:
            return

    def rehash(self):
        old_ht = self.hash_table 
        new_ts = self.table_size * 2 + 1
        self.hash_table = [[] for i in range(new_ts)]
        self.table_size = new_ts
        self.num_items = 0
        for i in old_ht:
            if i != None:
                for t in i:
                    self.insert(t[0], t[1])
        return 
        
    def get(self, key):
        index = key % self.table_size
        for i in self.hash_table[index]:
            if i[0] == key:
                return (i[0], i[1])
        raise LookupError("Item Not Found")

    def remove(self, key):
        index = key % self.table_size
        lst = self.hash_table[index]
        for i in lst:
            if i[0] == key:
                temp = i
                lst.remove(i)
                self.num_items -= 1
                return temp
        raise LookupError("Item Not Found")

    def size(self):
        return self.num_items

    def load_factor(self):
        return self.size() / self.table_size