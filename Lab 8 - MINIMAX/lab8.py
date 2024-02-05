import time

class Node: 
    def __init__(self,val):
        self.left = None        
        self.right = None         
        self.data = val 

def print_tree(root, level=0, prefix="Root: "):
    if root is not None:
        print(" " * (level * 2) + prefix + str(root.data))
        if root.left is not None or root.right is not None:
            print_tree(root.left, level + 1, "L- ")
            print_tree(root.right, level + 1, "R- ")

def minimax(node, depth,maximizing_player=True):
    if depth == 0 or node is None:
        return node.data
    # Recursive function
    if maximizing_player:
        max_val = float('-inf')
        if node.left is not None:
            max_val = max(max_val, minimax(node.left, depth - 1, False))
        if node.right is not None:
            max_val = max(max_val, minimax(node.right, depth - 1, False))
        return max_val
    else:
        min_val = float('inf')
        if node.left is not None:
            min_val = min(min_val, minimax(node.left, depth - 1, True))
        if node.right is not None:
            min_val = min(min_val, minimax(node.right, depth - 1, True))
        return min_val

def alphabeta(node, depth, alpha, beta,maximizing_player=True):
    if depth == 0 or node is None:
        return node.data

    if maximizing_player:
        v = float('-inf')
        for child in [node.left, node.right]:
            if child is not None:
                v = max(v, alphabeta(child, depth - 1, alpha, beta, False))
                alpha = max(alpha, v)
                if beta <= alpha:
                    #beta pruned
                    break  
        return v

    else:
        v = float('inf')
        for child in [node.left, node.right]:
            if child is not None:
                v = min(v, alphabeta(child, depth - 1, alpha, beta, True))
                beta = min(beta, v)
                if beta <= alpha:
                    #Alpha pruned
                    break  
        return v

## Initialize the tree           
n=Node(None)
n.left=Node(None)
n.left.left=Node(None)
n.left.left.left=Node(3)
n.left.left.right=Node(5)
n.left.right=Node(None)
n.left.right.left=Node(6)
n.left.right.right=Node(9)
n.right=Node(None)
n.right.left=Node(None)
n.right.left.left=Node(1)
n.right.left.right=Node(2)
n.right.right=Node(None)
n.right.right.left=Node(0)
n.right.right.right=Node(-1)

#print tree
print_tree(n)
current= time.time()
for i in range(100): result1 = minimax(n, 3)
elapsed1= time.time()-current

current= time.time()
for i in range(100): result2 = alphabeta(n,3,float('-inf'), float('inf'))
elapsed2= time.time()-current

print(f"The optimal value for the root node is (minimax): {result1} with t= {elapsed1}")
print(f"The optimal value for the root node is (Alpha-Beta): {result2} with t= {elapsed2}")