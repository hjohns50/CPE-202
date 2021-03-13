class Node:
    '''Node for use with doubly-linked list'''
    def __init__(self, item):
        self.item = item
        self.next = None
        self.prev = None

class OrderedList:
    '''A doubly-linked ordered list of items, from lowest (head of list) to highest (tail of list)'''

    def __init__(self):
        '''Use ONE dummy node as described in class
           ***No other attributes***
           DO NOT have an attribute to keep track of size'''
        self.head = Node(None)
    def is_empty(self):
        '''Returns True if OrderedList is empty
            MUST have O(1) performance'''
        return self.head.next is None or self.head.next is self.head

    def add(self, item):
        '''Adds an item to OrderedList, in the proper location based on ordering of items
           from lowest (at head of list) to highest (at tail of list) and returns True.
           If the item is already in the list, do not add it again and return False.
           MUST have O(n) average-case performance'''
        if not self.search(item):
            temp = self.head
            new = Node(item)
            if self.is_empty():
                self.head.next = new
                new.next = self.head
                new.prev = self.head
                self.head.prev = new
                return True
            else:
                while temp.next is not self.head:
                    temp = temp.next
                    if temp.item > item:
                        new.next = temp
                        new.prev = temp.prev
                        temp.prev = new
                        new.prev.next = new
                        return True
                    elif item > temp.item and temp.next == self.head:
                        new.next = self.head
                        new.prev = temp
                        temp.next = new
                        self.head.prev = new
                        return True
        return False

    def remove(self, item):
        '''Removes the first occurrence of an item from OrderedList. If item is removed (was in the list) 
          returns True.  If item was not removed (was not in the list) returns False
           MUST have O(n) average-case performance'''
        if not self.search(item):
            return False
        else:
            temp = self.head
            while temp.next is not None:
                temp = temp.next
                if temp.item == item:
                    temp.prev.next == temp.next
                    temp.next.prev == temp.prev
                    return True
                

    def index(self, item):
        '''Returns index of the first occurrence of an item in OrderedList (assuming head of list is index 0).
           If item is not in list, return None
           MUST have O(n) average-case performance'''
        i = 0
        if not self.search(item):
            return None
        temp = self.head
        while temp.next is not None:
            temp = temp.next
            if temp.item == item:
                return i
            i += 1

    def pop(self, index):
        '''Removes and returns item at index (assuming head of list is index 0).
           If index is negative or >= size of list, raises IndexError
           MUST have O(n) average-case performance'''
        i = 0
        if index < 0 or index >= self.size():
            raise IndexError
        temp = self.head.next
        while i != index:
            temp = temp.next
            i += 1
        pop = temp.item
        temp.next.prev = temp.prev
        temp.prev.next = temp.next
        return pop

    def search(self, item):
        '''Searches OrderedList for item, returns True if item is in list, False otherwise"
           To practice recursion, this method must call a RECURSIVE method that
           will search the list
           MUST have O(n) average-case performance'''
        temp = self.head
        return self.search_helper(item, temp)
    
    def search_helper(self, item, node):
        if node.item == item:
            return True
        if self.is_empty() or node.next is self.head:
            return False
        return self.search_helper(item, node.next)

    def python_list(self):
        '''Return a Python list representation of OrderedList, from head to tail
           For example, list with integers 1, 2, and 3 would return [1, 2, 3]
           MUST have O(n) performance'''
        temp = self.head
        lst = []
        i = 0
        while i < self.size():
            temp = temp.next
            lst.append(temp.item)
            i += 1
        return lst

    def python_list_reversed(self):
        '''Return a Python list representation of OrderedList, from tail to head, using recursion
           For example, list with integers 1, 2, and 3 would return [3, 2, 1]
           To practice recursion, this method must call a RECURSIVE method that
           will return a reversed list
           MUST have O(n) performance'''
        lst = []
        if self.is_empty():
            return lst
        temp = self.head.prev
        return self.reverse_helper(lst, temp)

    def reverse_helper(self, lst, temp):
        if temp.prev == self.head:
            lst.append(temp.item)
            return lst
        while temp.prev != self.head:
            lst.append(temp.item)
            return self.reverse_helper(lst, temp.prev)

    def size(self):
        '''Returns number of items in the OrderedList
           To practice recursion, this method must call a RECURSIVE method that
           will count and return the number of items in the list
           MUST have O(n) performance'''
        if self.is_empty():
            return 0
        temp = self.head
        return self.size_helper(temp.next)
    def size_helper(self, temp):
        if temp is self.head:
            return 0
        return 1 + self.size_helper(temp.next)
