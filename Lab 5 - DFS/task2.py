class Fifo:
    def __init__(self):
        self.Queue = list()

    def push(self,data):
        self.Queue.append(data)

    def popQ(self):
        if(len(self.Queue)>0):
            self.Queue.pop(0)

    def peek(self):
        return self.Queue[0]

    def printQ(self):
        print(self.Queue)

    def notempty(self):
        return bool(len(self.Queue))

class Lifo:
    def __init__(self):
        self.stk = list()

    def push(self,data):
        self.stk.append(data)

    def pop(self):
        if(len(self.stk)>0):
            self.stk.pop(-1)

    def peek(self):
        return self.stk[-1]

    def printS(self):
        print(self.stk)

    def notempty(self):
        return bool(len(self.stk))


class Node():
    def __init__(self,data):
        self.left = None
        self.right = None
        self.data = data

    def DFS(self):
        lst2= []
        visited = []
        F = Lifo() 
        F.push(self)
        while(F.notempty()):
            node = F.peek()
            F.pop()
            lst2.append(node.data)
            visited.append(node)
            lst = [node.right,node.left]
            for i in lst:
                if((i not in visited) and (i is not None)):
                    F.push(i)
                    visited.append(i)
        return lst2

    def BFS(self):
        lst2= [self.data]
        visited = []
        F = Fifo() 
        F.push(self)
        while(F.notempty()):
            node = F.peek()
            F.popQ()
            visited.append(node)
            lst = [node.left,node.right]
            for i in lst:
                if((i not in visited) and (i is not None)):
                    F.push(i)
                    visited.append(i)
                    lst2.append(i.data)
        return lst2

    def inorder(self,node):
        if (node is None): return
        self.inorder(node.left)
        print(node.data,end=', ')
        self.inorder(node.right)


    def preorder(self,node):
        if (node is None): return
        print(node.data,end=', ')
        self.inorder(node.left)
        self.inorder(node.right)

    def postorder(self,node):
        if (node is None): return
        self.inorder(node.left)
        self.inorder(node.right)
        print(node.data,end=', ')


print("-------------G1------------")
### graph1 ###
tree = Node(1)
tree.left=Node(2) 
tree.right=Node(3) 
#Tree of 2
tree.left.left=Node(4)
tree.left.left.left=Node(6)
#Tree of 4
tree.left.right=Node(5)
tree.left.right.left=Node(7)
tree.left.right.right=Node(8)

print('BFS',tree.BFS())
#print('DFS',tree.DFS())
print('inorder [',end='')
tree.inorder(tree)
print(']')
print('pre-order [',end='')
tree.preorder(tree)
print(']')
print('post-order [',end='')
tree.postorder(tree)
print(']')


### graph2 ###
print("-------------G2------------")
tree1 = Node(50)
tree1.left=Node(17) 
#right graph
tree1.right=Node(76)
tree1.right.left=Node(54)
tree1.right.left.right=Node(72)
tree1.right.left.right.left=Node(67)
#left graph
tree1.left.left= Node(9)
tree1.left.right= Node(23)
tree1.left.right.left= Node(19)
tree1.left.left.right= Node(14)
tree1.left.left.right.left= Node(12)

print('BFS',tree1.BFS())
#print('DFS',tree1.DFS())
print('inorder [',end='')
tree1.inorder(tree1)
print(']')
print('pre-order [',end='')
tree1.preorder(tree1)
print(']')
print('post-order [',end='')
tree1.postorder(tree1)
print(']')