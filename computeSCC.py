# graph representation for first pass:
# graph = [(node1)[Ismarked,finishingTime,leader,[outgoing_neibr1,outgoing_neibr2,...]]
#           node2:...]
import sys
import threading
t = 0
s = None
Num = 875714
mapping = []
#todoList for iterative depth first search
todoList = []
def loadGraph(filename):
    graph = [[0,0,0,[]] for i in range(Num)]
    data = open(filename,"r").read()
    rows = data.split("\n")
    for row in rows:
        segs = row.split()
        start = int(segs[0]) - 1
        end = int(segs[1]) - 1
        graph[start][3].append(end)
    return graph

def reverseGraph(graph):
    temp = [[0,0,0,[]] for i in range(Num)]
    for i in range(0,Num):
        for neibr in graph[i][3]:
            temp[neibr][3].append(i)
    return temp

def iterativeDFS(graph,node):
    # todoList: a stack
    todoList = [node]
    # call stack
    callstack = []
    while len(todoList) > 0:
        current = todoList.pop()
        # something wrong
        callstack.append(current)
        #mark as explored
        #print current
        graph[current][0] = 1
        #set leader
        graph[current][2] = s
        #has unexplored childs?
        flag = False
        for neibr in graph[current][3]:
            if graph[neibr][0] == 0:
                todoList.append(neibr)
                flag = True
        while(not flag):
            global t
            t = t+1
            n = callstack.pop()
            graph[n][1] = t
            global mapping
            #print (n,t)
            mapping.append((n,t))
            flag = False
            if len(callstack)<=0:
                break
            for neibr in graph[callstack[-1]][3]:
                if graph[neibr][0] == 0:
                    flag = True
                    break
    
def DFS(graph,node):
    #mark as explored
    graph[node][0] = 1
    #set leader
    graph[node][2] = s
    for neibr in graph[node][3]:
        if graph[neibr][0] == 0:
            DFS(graph,neibr)
    global t
    t=t+1
    #set finishing time
    graph[node][1] = t
    global mapping
    mapping.append((node,t))

def DFSloop(graph,perm,pass_id):
    for i in perm:
        if isinstance(i,tuple):
            t = i[0]
        else:
            t = i
        #print i,t
        if graph[t][0] == 0:
            global s
            s = t
            DFS(graph,t)
    if pass_id == 1:
        # return the permutation used for second pass
        #print mapping
        #temp = Sort(mapping)
        #print temp
        #reverse the map
        for i in range(0,len(mapping)/2):
            # swap the i-th item and (len-1-i)th item
            temp = mapping[i]
            mapping[i] = mapping[len(mapping)-1-i]
            mapping[len(mapping)-1-i] = temp
        print mapping
        return mapping
    else:
        #print graph
        # count list of SCC
        SCClist = {}
        for item in graph:
            key = item[2]
            if key not in SCClist:
                SCClist[key] = 1
            else:
                SCClist[key] += 1
        return SCClist
            
def main():
    #open("SCCdata.txt","w").write("success")
    print "start"
    graph = loadGraph("SCC.txt")
    #print graph
    reversedG = reverseGraph(graph)
    init_perm = [Num-i-1 for i in range(Num)]
    sec_perm = DFSloop(reversedG,init_perm,1)
    global t
    t = 0
    SCClist = DFSloop(graph,sec_perm,2)
    #open("SCCdata.txt","w").write(str(SCClist))
    #print graph
    #print SCClist
    print "end"
    m = []
    for i in SCClist:
        t = SCClist[i]
        if t > 170:
            m.append(t)
    print m

def testIterativeDFS():
    graph = loadGraph("testIterativeDFS.txt")
    iterativeDFS(graph,0)
    
threading.stack_size(67108864) # 64MB stack
sys.setrecursionlimit(2 ** 20)  # approx 1 million recursions
thread = threading.Thread(target = main) # instantiate thread object
thread.start() # run program at target
main()
