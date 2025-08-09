# Pick one of the abstract data structures mentioned in this section that you have not yet implemented
# Build a custom Python class that demonstrates its functionality 
# Compare your solution to: https://github.com/david-legend/python-algorithms/tree/main/data-structures/src
class TreeNode:
    def __init__(self, value):
        self.left = None
        self.right = None
        self.value = value

    def insert(self, value):
        if value < self.value:
            if self.left is None:
                self.left = TreeNode(value)
            else:
                self.left.insert(value)
        else:
            if self.right is None:
                self.right = TreeNode(value)
            else:
                self.right.insert(value)

    def inorder_traversal(self):
        if self.left:
            self.left.inorder_traversal()
        print(self.value)
        if self.right:
            self.right.inorder_traversal()

    def preorder_traversal(self):
        print(self.value)
        if self.left:
            self.left.preorder_traversal()
        if self.right:
            self.right.preorder_traversal()  

    def postorder_traversal(self):
        if self.left:
            self.left.postorder_traversal()
        if self.right:
            self.right.postorder_traversal()                                          
        print(self.value)

    def find(self, value):
        if value < self.value:
            if self.left is None:
                return False
            else:
                return self.left.find(value)
        elif value > self.value:
            if self.right is None:
                return False
            else:
                return self.right.find(value)
        else:
            return True

    def remove(self, value):
        if value < self.value:
            if self.left:
                self.left = self.left.remove(value)
        elif value > self.value:
            if self.right:
                self.right = self.right.remove(value)
        else:
        # Node found
            if self.left is None:
                return self.right
            elif self.right is None:
                return self.left
            else:
            # Find min node in right subtree
                min_larger_node = self.right
                while min_larger_node.left:
                    min_larger_node = min_larger_node.left
                self.value = min_larger_node.value
                self.right = self.right.remove(min_larger_node.value)
        return self

       

tree = TreeNode(10)
tree.insert(5)
tree.insert(12)
tree.insert(3)
tree.insert(7)
tree.insert(15)
print("Inorder Traversal:")
tree.inorder_traversal()
print("\nPreorder Traversal:")
tree.preorder_traversal()
print("\nPostorder Traversal:")
tree.postorder_traversal()
print("\nFind 7 in the tree:", tree.find(7))
tree.remove(7)
print("\nInorder Traversal after removing 7:")
tree.inorder_traversal()