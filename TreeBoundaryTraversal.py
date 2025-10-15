# Definition for a binary tree node
class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


class Solution:
    def boundary(self, root):
        if not root:
            return []

        res = [root.data]

        # Function to get left boundary (excluding leaves)
        def leftBoundary(node):
            while node:
                if node.left or node.right:
                    res.append(node.data)
                if node.left:
                    node = node.left
                else:
                    node = node.right

        # Function to get leaf nodes (in-order traversal)
        def leafNodes(node):
            if node is None:
                return
            leafNodes(node.left)
            if not node.left and not node.right:
                res.append(node.data)
            leafNodes(node.right)

        # Function to get right boundary (excluding leaves)
        def rightBoundary(node):
            temp = []
            while node:
                if node.left or node.right:
                    temp.append(node.data)
                if node.right:
                    node = node.right
                else:
                    node = node.left
            # Add in reverse order
            res.extend(reversed(temp))

        # Collect left boundary (excluding root and leaves)
        if root.left:
            leftBoundary(root.left)

        # Collect leaf nodes
        leafNodes(root.left)
        leafNodes(root.right)

        # Collect right boundary (excluding root and leaves)
        if root.right:
            rightBoundary(root.right)

        return res
