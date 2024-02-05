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

    #TASK 3 
    def binary_pathfind(self, source, target, paths=[]):
        finalpathlist= []
        def binary_pathfind_recursive(source, target, path= '', paths = [], viewed_nodes = []):            
            viewed_nodes.append(source)
            path +=  str(source) + '->'
            for edge in list(self.adjency_list[source]):
                if(edge == target):
                        #print(path + str(target))
                        finalpathlist.append(path + str(target))
                        continue 
                if(edge not in viewed_nodes):                  
                    binary_pathfind_recursive(edge, target,path, paths,viewed_nodes)
                    viewed_nodes.remove(edge)
        binary_pathfind_recursive(source, target)
        return finalpathlist

#Task 1
g1 = graph()
g1.insert_edge_undirected((6,4))
g1.insert_edge_undirected((4,5))
g1.insert_edge_undirected((4,3))
g1.insert_edge_undirected((3,2))
g1.insert_edge_undirected((5,2))
g1.insert_edge_undirected((5,1))
g1.insert_edge_undirected((2,1))
print("--------pt1--------")
g1.print_graph()
print("Paths: ")
g1.binary_pathfind(6, 1)

#Task 2
g2 = graph()
g2.insert_edge_directed(('A','B'))
g2.insert_edge_directed(('B','C'))
g2.insert_edge_directed(('B','D'))
g2.insert_edge_directed(('B','E'))
g2.insert_edge_directed(('C','E'))
g2.insert_edge_directed(('D','E'))
g2.insert_edge_directed(('E','F'))
g2.insert_edge_directed(('G','D'))
print("--------pt2--------")
g2.print_graph()
print("Paths: ")
g2.binary_pathfind('A', 'F')

#Question2
def img_toajg(img):
    adjlist= dict()
    for row in range(len(img)):
        for col in range(len(img[0])):
            pix = img[row][col]
            adjlist[pix]= [] 
            if(row<len(img)-1):adjlist[pix].append(img[row+1][col])
            if(row>0):adjlist[pix].append(img[row-1][col])
            if(col<len(img[0])-1):adjlist[pix].append(img[row][col+1])
            if(col>0):adjlist[pix].append(img[row][col-1])  
    return adjlist
        


print("--------Q2--------")
img= [[150,	2,	5],
      [80,	145,45],    
      [74,	102,165]]

g3 = graph()
g3.init_by_list(img_toajg(img))
g3.print_graph()
print("Paths: ")
print(g3.binary_pathfind(150, 165))

print("----Bonus Question---")
img= [[150,	2,	5],
      [80,	145,45],    
      [74,	102,165]]

g4 = graph()
g4.init_by_list(img_toajg(img))
print("Paths: ")
pathlist= g3.binary_pathfind(150, 165)
mindist = 1000
minpath = ''
for path in pathlist:
    dist    = 0
    splitpoints= path.split('->')
    for i in range(0,len(splitpoints)-1):
        dist+=abs(int(splitpoints[i])-int(splitpoints[i+1]))
        if dist > mindist :break
    if(dist<mindist):
        mindist=dist
        minpath=path
print(minpath,"Distance: ",mindist)


### Home Task
print("Home Task")
mat=[[0,5,-1,6,-1],
[5,0,9,-1,7],
[0,9,0,-1,9],
[6,-1,-1,0,5],
[-1,7,9,5,0]]

graph= {'V1': {}, 'V2': {}, 'V3': {}, 'V4': {}, 'V5': {}}
import pprint 
for i in range(len(mat)):
    for j in range(len(mat[i])):
        
        graph[list(graph.keys())[i]][list(graph.keys())[j]]=mat[i][j]
        #print(mat[i][j])

pp = pprint.PrettyPrinter(indent=4)
pp.pprint(graph)       