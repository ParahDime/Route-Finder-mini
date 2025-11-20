#Binary search tree

#Node for using in binary search tree
class Node:
    def __init__(self, name):
        self.name = name
        self.left = None
        self.right = None


#Binary search tree

class BST:
    #initialise binary tree and root
    def __init__(self):
        self.root = None
    
    #trigger function to insert into BST
    def insert(self, name):
        self.root = self._insert_recursive(self.root, name)
    
    #recursive function for insertion
    def _insert_recursive(self, root, name):
        if root is None: #empty place found on tree
            return Node(name)
        #move down the tree to find the correct spot
        if name < root.name:
            root.left = self._insert_recursive(root.left, name)
        else:
            root.right = self._insert_recursive(root.right, name)

        return root

    #search the binary search tree, return true/false
    def search(self, name):
        self.root = self._search_recursive(self.root, name)

    def _search_recursive(self, root, name):
        pass
    #if is found return true

    #else search

    #return
    #return all names in alphabetical order
    def inorder(self):
        pass