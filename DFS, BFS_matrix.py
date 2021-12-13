#노드의 값들이 0~n의 값을 가진다는 가정하에 구현하였다.
def DFSUtil(graph, v, visited):

    n = len(graph)
    visited[v] = True
    print(v, end = '')

    for i in range(n):
        if graph[v][i] == 1:
            if visited[i] == False:
                DFSUtil(graph, i, visited)

def DFS(graph, v):
    
    visited = [False] * (len(graph))
    DFSUtil(graph, v, visited)

def BFS(graph, s):

    visited = [False] * (len(graph))

    queue = []

    queue.append(s)
    visited[s] = True

    while queue:
        s = queue.pop(0)
        print(s, end = '')

        for i in range(len(graph)):
            if graph[s][i] == 1:
                if visited[i] == False:
                    queue.append(i)
                    visited[i] = True

def printG(graph):
    for i in range(len(graph)):
        for j in range(len(graph)):
            print(graph[i][j], end=' ')
        print("")

graphs = [[[0, 1, 1, 0, 0, 0, 0, 1], [1, 0, 0, 1, 0, 1, 0, 1], [1, 0, 0, 0, 0, 1, 1, 0], [0, 1, 0, 0, 1, 0, 0, 1], [0, 0, 0, 1, 0, 0, 0, 1], [0, 1, 1, 0, 0, 0, 0, 0], [0, 0, 1, 0, 0, 0, 0, 0], [1, 1, 0, 1, 1, 0, 0, 0]], [[0, 1, 0, 0, 0], [1, 0, 1, 1, 1], [0, 1, 0, 1, 1], [0, 1, 1, 0, 1], [0, 1, 1, 1, 0]], [[0, 1, 1, 0, 0, 0], [1, 0, 0, 1, 1, 0], [1, 0, 0, 0, 0, 1], [0, 1, 0, 0, 0, 0], [0, 1, 0, 0, 0, 0], [0, 0, 1, 0, 0, 0]]]
for i in range(len(graphs)):
    print("----------Graph----------")
    printG(graphs[i])
    print("----------DFS----------")
    DFS(graphs[i], 0)
    print("\n----------BFS----------")
    BFS(graphs[i], 0)
    print("\n----------End----------\n")