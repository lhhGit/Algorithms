import random
#graph is represented as connectivity matrix
cols = 200
rows = 200
graph = [[0 for col in range(cols)] for row in range(rows)]
existing_Nodes = [i for i in range(cols)]

def loadMatrix():
    file = open("kargerMinCut.txt","r")
    lines = file.readlines()
    for line in lines:
        data = line.split("\t")
        #print data
        start = int(data[0])
        for i in range(1,len(data)-1):
            graph[start-1][int(data[i])-1] = 1

# pay attention: there are parallel edges in this graph,
# so randomly choose a graph need to take into consideration
# the values in the specified row of the connectivity matrix!
# Randomly choose a neighbor of the vertex is wrong! 
def getRandomAdj(graph,idx):
    neibrs = []
    total = 0
    for i in range(cols):
        if graph[idx][i] > 0:
            total += graph[idx][i]
            neibrs.append((i,total))
    
    rand = random.randint(0,total-1)
    for item in neibrs:
        if item[1] > rand:
            return (idx,item[0])
    return (idx,neibrs[-1])

def rowAnd(graph,idx1,idx2):
    for i in range(0,cols):
        graph[idx1][i] = graph[idx1][i] + graph[idx2][i]

def colAnd(graph,idx1,idx2):
    for i in range(0,rows):
        graph[i][idx1] = graph[i][idx1] + graph[i][idx2]

def clearNode(graph,idx):
    for i in range(0,rows):
        graph[i][idx] = 0
        graph[idx][i] = 0

def randEdge(graph):
    u = random.choice(existing_Nodes)
    return getRandomAdj(graph,u)

def getNumberOfAdj(graph,idx):
    total = 0
    for i in range(cols):
        if graph[idx][i] > 0:
            total += graph[idx][i]
        #print graph[idx]
    return total

def randContract(graph):
    for i in range(0,cols-2):
        edge = randEdge(graph)
        rowAnd(graph,edge[0],edge[1])
        colAnd(graph,edge[0],edge[1])
        clearNode(graph,edge[1])
        graph[edge[0]][edge[0]] = 0
        #print edge[1]
        existing_Nodes.remove(edge[1])
    return getNumberOfAdj(graph,existing_Nodes[0])

max = 10000
for i in range(0,10000):
    random.seed()
    loadMatrix()
    #print graph
    existing_Nodes = [j for j in range(cols)]
    temp = randContract(graph)
    if temp < max:
        max = temp
    print "attemp",i,temp,"max",max
print max
