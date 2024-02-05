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

class Node():
    def __init__(self,data):
        self.left = None
        self.right = None
        self.mid = None
        self.data = data
 
    def BFS(self):
        lst2= [self.data]
        visited = []
        F = Fifo() 
        F.push(self)
        while(F.notempty()):
            node = F.peek()
            F.popQ()
            visited.append(node)
            lst = [node.left,node.mid,node.right]
            for i in lst:
                if((i not in visited) and (i is not None)):
                    F.push(i)
                    visited.append(i)
                    lst2.append(i.data)
        return lst2
### graph1 ###
tree = Node(1)
tree.left=Node(2) 
tree.mid=Node(3) 
tree.right=Node(4) 
#Tree of 2
tree.left.left=Node(5)
tree.left.mid=Node(6)
tree.left.left.left=Node(9)
tree.left.left.mid=Node(10)
#Tree of 4
tree.right.right=Node(8)
tree.right.mid=Node(7)
tree.right.mid.mid=Node(11)
tree.right.mid.right=Node(12)
print(tree.BFS())

### graph2 ###

