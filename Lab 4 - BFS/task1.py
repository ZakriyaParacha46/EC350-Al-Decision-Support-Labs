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

    ### LAB4 Function ###
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
print("---Graph---")
G= graph()
G.insert_edge_directed(("Tottenham Court Road","Oxford Circus"))
G.insert_edge_directed(("Tottenham Court Road","Goodge Street"))
G.insert_edge_directed(("Tottenham Court Road","Holborn"))
G.insert_edge_directed(("Oxford Circus","Warren Street"))
G.insert_edge_directed(("Oxford Circus","Regent's Park"))
G.insert_edge_directed(("Goodge Street","Warren Street"))
G.insert_edge_directed(("Holborn","Russell Square"))
G.insert_edge_directed(("Warren Street","Euston"))
G.insert_edge_directed(("Warren Street","King's Cross St. Pancras"))
G.insert_edge_directed(("Regent's Park","Baker Street"))
G.insert_edge_directed(("Russell Square","King's Cross St. Pancras"))
G.insert_edge_directed(("Euston","King's Cross St. Pancras"))
G.insert_edge_directed(("Baker Street","Great Portland Street"))
G.insert_edge_directed(("Great Portland Street","Euston Square"))
G.insert_edge_directed(("Euston Square","King's Cross St. Pancras"))


G.print_graph()
print(G.BFS_search("Tottenham Court Road","King's Cross St. Pancras"))
