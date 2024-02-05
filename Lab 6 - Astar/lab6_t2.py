class PriorityQueue:
    def __init__(self):
        self.queue = {}

    def push(self, item, priority):
        if priority in self.queue:
            self.queue[priority].append(item)
        else:
            self.queue[priority] = [item]

    def pop(self):
        if not self.isEmpty():
            highest_priority = min(self.queue.keys())
            item = self.queue[highest_priority].pop(0)
            if not self.queue[highest_priority]:
                del self.queue[highest_priority]
            return item

    def isEmpty(self):
        return not bool(self.queue)


def AStar(graph, heuristic, startNode, goal):
    open_set = PriorityQueue()  
    open_set.push(startNode, 0)
    came_from = {}
    cost_so_far = {startNode: 0}

    while not open_set.isEmpty():
        current = open_set.pop()

        if current == goal:
            current = goal
            path = []

            while current != startNode:
                path.append(current)
                current = came_from[current]

            path.append(startNode)
            path.reverse()

            return path, cost_so_far[goal]

        for neighbor, cost_to_reach_neighbor in graph[current].items():
            new_cost = cost_so_far[current] + cost_to_reach_neighbor

            if neighbor not in cost_so_far or new_cost < cost_so_far[neighbor]:
                cost_so_far[neighbor] = new_cost
                priority = new_cost + heuristic[neighbor]
                open_set.push(neighbor, priority)
                came_from[neighbor] = current

    return None, 0  # No path found


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


def get_weighted(adjlist): 
    new_adjlist= {}
    for k in adjlist.keys():
        new_adjlist[k]={}
        for i in adjlist[k]: 
            new_adjlist[k][i]= abs(k-i)
    return new_adjlist

def get_huristics(img):
    heuristic = {}
    for row in range(len(img)):
        for col in range(len(img[0])):
            heuristic[img[row][col]] =   row + col
    return heuristic

img= [[150,	2   ,5],
      [80,	145 ,45],    
      [74,	102 ,165]]

graph= img_toajg(img)
heuristic=get_huristics(img)
weighted_graph=get_weighted(img_toajg(img))

path,goal= AStar(weighted_graph,heuristic,150,165)
print(path)
print(goal)