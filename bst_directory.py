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
        return self._search_recursive(self.root, name)

    def _search_recursive(self, root, name):
        if root is None: #no item found
            return False
        
        if root.name == name: #item found
            return True
        if name < root.name:
            return self._search_recursive(root.left, name)
        else:
            return self._search_recursive(root.right, name)
        pass

    #return all names in alphabetical order
    def inorder(self):
        return self._inorder_recursive(self.root)

    def _inorder_recursive(self, root):
        if root is None:
            return []

        left_side = self._inorder_recursive(root.left) #move left in tree
        current = [root.name] #get the name
        right_side = self._inorder_recursive(root.right) #move right

        # Get output and return it
        return left_side + current + right_side