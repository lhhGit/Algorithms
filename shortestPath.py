import sys
def combineList(list1,list2):
    for i in range(1,len(list2)):
        list1.append(list2[i])

def calcPath(start,end):
    if start == end:
        return [[end]]
    neighbors = graph[start]
    paths = []
    for neibr in neighbors:
        neibrpaths = calcPath(neibr,end)
        for path in neibrpaths:
            paths.append([start] + path)
    return paths

def calcShortestPath(start,end):
    if start == end:
        #print end
        return [0,[end]]
    shortestpaths = [100000]
    neighbors = graph[start]
    neibr_dist = 0
    for neibr in neighbors:
        neibrshtpath = calcShortestPath(neibr,end)
        if len(shortestpaths)==0 or neibrshtpath[0] + graph[start][neibr] < shortestpaths[0]:
            shortestpaths = neibrshtpath
            neibr_dist = graph[start][neibr]
            shortestpaths[0] += neibr_dist
        elif neibrshtpath[0] + graph[start][neibr]== shortestpaths[0]:
            combineList(shortestpaths,neibrshtpath)
        else:
            continue

    for i in range(1,len(shortestpaths)):
        list = shortestpaths[i]
        list.append(start)
        j = len(list)-1;
        while j>=1:
            list[j] = list[j-1]
            j=j-1
        list[0]=start
    #print start,end,shortestpaths
    return shortestpaths

#the first entry is the node, the second entry is the length
graph = {}
teams = []
data = sys.stdin.readline().split()
nodes = int(data[0])
lines = int(data[1])
start = int(data[2])
end = int(data[3])
for i in range(0,nodes):
    graph[i] = {}
path_data = sys.stdin.readline().split()
for item in path_data:
    teams.append(int(item))
while lines>0:
    edge = sys.stdin.readline().split()
    graph[int(edge[0])][int(edge[1])] = int(edge[2])
    lines-=1
paths = calcShortestPath(start,end)
allpaths = calcPath(start,end)
#print allpaths
passed_nodes = []
sum = 0
for i in range(0,len(allpaths)):
    for j in allpaths[i]:
        if j not in passed_nodes:
               passed_nodes.append(j)
               sum += teams[j]
print len(paths)-1,sum
