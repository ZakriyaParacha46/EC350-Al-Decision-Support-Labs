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


#######Lab3 Code#########
class graph:
    def __init__(self):
        self.adjency_list = dict()
    
    def init_by_list(self, adjdict):
        self.adjency_list= adjdict

    def insert_edge_directed(self,edge):
        #Inputs a tuple (A,B)
        if(edge[0] in self.adjency_list):
            self.adjency_list[edge[0]].append(edge[1])
        else:
            self.adjency_list[edge[0]]= [edge[1]]

    def insert_edge_undirected(self,edge):
        self.insert_edge_directed((edge[0],edge[1]))
        self.insert_edge_directed((edge[1],edge[0]))


    def print_edge(self):
        for key,val in self.adjency_list.items():
                for v in val:
                    print(key, '->' , v)

    def print_graph(self):
        flat_list = []
        for sublist in list(self.adjency_list.values()):
            for item in sublist:
                flat_list.append(item)

        for key,val in self.adjency_list.items():
            print(f'{key}:({flat_list.count(key)}:{len(val)}) -> {val}')

    ##LAB 5 Code
    def DFS(self,startingpt):
        F= Lifo()
        out=[]
        visited = [startingpt]
        F.push(startingpt)
        while (F.notempty()):
            #F.printS()
            node= F.peek()
            F.pop()
            out.append(node)
            for i in self.adjency_list[node]:
                if(i not in visited):
                    F.push(i)
                    visited.append(i)
            
        return out

    def BFS(self,startingpt):
        F= Fifo()
        out=[startingpt]
        visited = [startingpt]
        F.push(startingpt)
        while (F.notempty()):
            node= F.peek()
            F.popQ()
            for i in self.adjency_list[node]:
                if(i not in visited):
                    F.push(i)
                    visited.append(i)
                    out.append(i)
            
        return out


    ### Assignment Function ###
    def BFS_search(self, startingpt, ending):
        F = Fifo()
        parent = {}  # To store the parent node for each node in the path
        out = []
        visited = [startingpt]
        F.push(startingpt)
    
        while F.notempty():
            node = F.peek()
            F.popQ()
    
            if node == ending:
                # Reconstruct the path from the parent dictionary
                path = [ending]
                while path[-1] != startingpt:
                    path.append(parent[path[-1]])
                path.reverse()
                return path
    
            for neighbor in sorted(self.adjency_list[node]):
                if neighbor not in visited:
                    F.push(neighbor)
                    visited.append(neighbor)
                    parent[neighbor] = node
    
        return None  # If no path is found


#######Lab3 Code#########
#Graph 1
print("---G1---")
G= graph()
G.insert_edge_undirected(('E','B'))
G.insert_edge_undirected(('E','A'))
G.insert_edge_undirected(('A','B'))
G.insert_edge_undirected(('D','A'))
G.insert_edge_undirected(('D','B'))
G.insert_edge_undirected(('D','C'))
G.print_graph()
print('BFS',G.BFS('E'))
print('DFS',G.DFS('E'))


#Graph 2
print("---G2---")
G1= graph()
G1.insert_edge_undirected(('1','5'))
G1.insert_edge_undirected(('1','2'))
G1.insert_edge_undirected(('4','5'))
G1.insert_edge_undirected(('5','2'))
G1.insert_edge_undirected(('3','4'))
G1.insert_edge_undirected(('3','2'))
G1.insert_edge_undirected(('4','6'))
G1.print_graph()
print('BFS',G1.BFS('6'))
print('DFS', G1.DFS('6'))