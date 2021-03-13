from queue_array import Queue

class TreeNode:
    def __init__(self, key, data, left=None, right=None):
        self.key = key
        self.data = data
        self.left = left
        self.right = right

class BinarySearchTree:

    def __init__(self): # Returns empty BST
        self.root = None

    def is_empty(self): # returns True if tree is empty, else False
        return self.root is None
    
    def search(self, key): # returns True if key is in a node of the tree, else False
        return self.search_helper(self.root, key)
    
    def search_helper(self, node, key):
        if node is None:
            return False
        elif node.key == key:
            return True
        elif key < node.key:
            return self.search_helper(node.left, key)
        elif key > node.key:
            return self.search_helper(node.right, key)
        else:
            return False
        
            

    def insert(self, key, data=None): # inserts new node w/ key and data
        # If an item with the given key is already in the BST, 
        # the data in the tree will be replaced with the new data
        node = TreeNode(key, data)  
        if self.root is None:
            self.root = node
            return
        else:
            self.insert_helper(self.root, node)
            
    def insert_helper(self, root, node):
        if node.key > root.key:
            if root.right is None:
                root.right = node
                return
            else:
                self.insert_helper(root.right, node)
        elif node.key < root.key:
            if root.left is None:
                root.left = node
                return
            else:
                self.insert_helper(root.left, node)
        elif node.key == root.key:
            root.data = node.data
            return
             
    
    def find_min(self): # returns a tuple with min key and data in the BST
        # returns None if the tree is empty
        if self.root is None:
            return None
        return self.min_key_helper(self.root)
    
    def min_key_helper(self, root):
        if root.left is None:
            return (root.key, root.data)
        else:
            return self.min_key_helper(root.left)
        

    def find_max(self): # returns a tuple with max key and data in the BST
        # returns None if the tree is empty
        if self.root is None:
            return None
        return self.max_key_helper(self.root)
    
    def max_key_helper(self, root):
        if root.right is None:
            return (root.key, root.data)
        else:
            return self.max_key_helper(root.right)


    def tree_height(self): # return the height of the tree
        # returns None if tree is empty
        if self.root is None:
            return None
        return (self.height_helper(self.root))

    def height_helper(self, root):
        if root is None:
            return 0
        if root.left is None and root.right is None:
            return 0
        return 1 + max(self.height_helper(root.left), self.height_helper(root.right))

    def inorder_list(self):
        lst = []
        if self.root is None:
            return lst
        return self.order_list_helper(self.root, lst)
        
    
    def order_list_helper(self, node, lst):
        if node is not None:
            self.order_list_helper(node.left, lst)
            lst.append(node.key)
            self.order_list_helper(node.right, lst)
        return lst
    def preorder_list(self):  # return Python list of BST keys representing pre-order traversal of BST
        lst = []
        if self.root is None:
            return lst
        return self.preorder_list_helper(self.root, lst)
    
    def preorder_list_helper(self, node, lst):
        if node is not None:
            lst.append(node.key)
            self.preorder_list_helper(node.left, lst)
            self.preorder_list_helper(node.right, lst)
        return lst
        
    def level_order_list(self):  # return Python list of BST keys representing level-order traversal of BST
        # You MUST use your queue_array data structure from lab 3 to implement this method
        q = Queue(25000) # Don't change this!
        lst = []
        q.enqueue(self.root)
        while not q.is_empty():
            temp = q.dequeue()
            if temp is not None:
                lst.append(temp.key)
                q.enqueue(temp.left)
                q.enqueue(temp.right)
        return lst

