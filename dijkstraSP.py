MAX = 1000000
VERTICECOUNT = 200
# graph representation: 
# [ (graphidx) [(adjacentVertex1,length1),(adjacentVertex2,length2),
#               ... ]
# ]
def loadGraph():
    data = open("dijkstraData.txt","r").read()
    rows = data.split("\n")
    graph = [[] for i in range(VERTICECOUNT)]
    for row in rows:
        eles = row.split("\t")
        vertex_idx = int(eles[0])-1
        for i in range(1,len(eles)-1):
            pair = eles[i].split(",")
            #print vertex_idx,pair
            graph[vertex_idx].append((int(pair[0])-1,int(pair[1])))
    return graph
                    
def dijkstra(graph,start):
    # the processed vertices so far
    X = [start]
    # the shortest path length for each vertex
    A = [MAX for i in range(VERTICECOUNT)]
    A[start] = 0
    # the shortest path for each vertex (optional)
    #B = [[] for i in range(VERTICECOUNT)]     
    while len(X) < VERTICECOUNT:
        #min dijkstra score and the corresponding vertex
        dijkstra_score = MAX
        min_vertex = -1
        for v in X:
            for edge in graph[v]:
                if edge[0] in X:
                    continue
                if A[v] + edge[1] < dijkstra_score:
                    min_vertex = edge[0]
                    dijkstra_score = A[v] + edge[1]
        #print "min",min_vertex
        X.append(min_vertex)
        A[min_vertex] = dijkstra_score
    return A

def main():
    graph = loadGraph()
    #print len(graph)
    result = dijkstra(graph,0)
    return result

shortestPaths = main()
print shortestPaths
test = [7,37,59,82,99,115,133,165,188,197]
resultp = [0 for i in range(len(test))]
for i in range(len(test)):
    resultp[i] = shortestPaths[test[i]-1]
print resultp
