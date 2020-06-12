"""
Binary search trees are a data structure that enforce an ordering over 
the data they store. That ordering in turn makes it a lot more efficient 
at searching for a particular piece of data in the tree. 

This part of the project comprises two days:
1. Implement the methods `insert`, `contains`, `get_max`, and `for_each`
   on the BSTNode class.
2. Implement the `in_order_print`, `bft_print`, and `dft_print` methods
   on the BSTNode class.
"""
class BSTNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    # Insert the given value into the tree
    def insert(self, value):
        #1 Check if there is no root
            # if there isn't, create the node and park it
        if self is None:
            self = BSTNode(value)
        #2 Otherwise, there is a root
            # compare the vlaue to the root's value to determine which direction to go in
            # if the value is less than the root's value, go left, 
            # if the vaue is greater or equal to the root's value, go right
        else:
            if value < self.value:
                if self.left is None:
                    self.left = BSTNode(value)
                else:
                    self.left.insert(value)
            else:
                if self.right is None:
                    self.right = BSTNode(value)
                else:
                    self.right.insert(value)


    # Return True if the tree contains the value
    # False if it does not
    def contains(self, target):
        output = False
        if self is None:
            output = False
        else:
            if self.value == target:
                output = True
            else:
                if target < self.value:
                    if self.left is None:
                        output = False
                    else:
                        output = self.left.contains(target)
                else:
                    if self.right is None:
                        output = False
                    else:
                        output = self.right.contains(target)
        return output

    # Return the maximum value found in the tree
    def get_max(self):
        current = self
        while(current.right):
            current = current.right
        return current.value

    # Call the function `fn` on the value of each node
    def for_each(self, fn):
        if self:
            fn(self.value)
        if self.left:
            self.left.for_each(fn)
        if self.right:
            self.right.for_each(fn)

    # Part 2 -----------------------

    # Print all the values in order from low to high
    # Hint:  Use a recursive, depth first traversal
    def in_order_print(self, node):
        if(self):
            if(self.left):
                self.left.in_order_print(node)
            print(self.value)
            if(self.right):
                self.right.in_order_print(node)

    # Print the value of every node, starting with the given node,
    # in an iterative breadth first traversal
    def bft_print(self, node):
        visitedNodes = []
        if(node):
            visitedNodes.append(node)
            print(node.value)
        current = node
        while(current):
            if(current.left):
                print(current.left.value)
                visitedNodes.append(current.left)
            if(current.right):
                print(current.right.value)
                visitedNodes.append(current.right)
            visitedNodes.pop(0)
            if(not visitedNodes):
                break
            current = visitedNodes[0]

    # Print the value of every node, starting with the given node,
    # in an iterative depth first traversal
    def dft_print(self, node):
        if(node):
            print(node.value)
            if(node.left):
                node.left.dft_print(node.left)
            if(node.right):
                node.right.dft_print(node.right)

    # Stretch Goals -------------------------
    # Note: Research may be required

    # Print Pre-order recursive DFT
    def pre_order_dft(self, node):
        pass

    # Print Post-order recursive DFT
    def post_order_dft(self, node):
        pass

# bst = BSTNode(1)
# bst.insert(8)
# bst.insert(5)
# bst.insert(7)
# bst.insert(6)
# bst.insert(3)
# bst.insert(4)
# bst.insert(2)

# bst.dft_print(bst)
