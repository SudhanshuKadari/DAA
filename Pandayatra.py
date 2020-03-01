import sys
check = 1
class Graph(): 
  
    def __init__(self, vertices): 
        self.V = vertices 
        self.graph = [[0 for column in range(vertices)]  
                    for row in range(vertices)] 
  
    def printSolution(self, dist): 
        for node in range(self.V): 
            if node == check:
                return (dist[node])
  
    # A utility function to find the vertex with  
    # minimum distance value, from the set of vertices  
    # not yet included in shortest path tree 
    def minDistance(self, dist, sptSet): 
  
        # Initilaize minimum distance for next node 
        min = sys.maxsize 
  
        # Search not nearest vertex not in the  
        # shortest path tree 
        try:
            for v in range(self.V): 
                if dist[v] < min and sptSet[v] == False: 
                    min = dist[v] 
                    min_index = v 
  
            return min_index 
        except:
            None
            
  
    # Funtion that implements Dijkstra's single source  
    # shortest path algorithm for a graph represented  
    # using adjacency matrix representation 
    def dijkstra(self, src): 
  		
        dist = [sys.maxsize] * self.V 
        dist[src] = 0
        sptSet = [False] * self.V 
  
        for cout in range(self.V): 
  
            try:
                u = self.minDistance(dist, sptSet)
                sptSet[u] = True
        
            except:
                None
  
            # Put the minimum distance vertex in the  
            # shotest path tree 
            
  
            # Update dist value of the adjacent vertices  
            # of the picked vertex only if the current  
            # distance is greater than new distance and 
            # the vertex in not in the shotest path tree 
            for v in range(self.V): 
                try:
                    if self.graph[u][v] > 0 and sptSet[v] == False and dist[v] > dist[u] + self.graph[u][v]: 
                        dist[v] = dist[u] + self.graph[u][v] 
                except:
                    None

  
        return self.printSolution(dist) 

   
    
d = {}
lst = []
graph =[]

inp = int(input()) 

for i in range(0,inp):
    for j in range(0,inp):
        lst.append(0)
    graph.append(list(lst))
    lst.clear()

count = 0
weight = 0
for i in range(0,inp):
    a,b,c = input().split(' ')  
    if a not in d:
        d[a] = count
        count +=1
        
    if b not in d:
        d[b] = count
        count +=1
    if count == 2:
        weight = int(c)
        continue
 
    graph[d[a]][d[b]] = int(c)
    graph[d[b]][d[a]] = int(c)
  	

g = Graph(inp)
g.graph = graph
#[[0, 4, 0, 44], [4, 0, 3, 0], [0, 3, 0, 0], [44, 0, 0, 0]]
#[[0, 0, 3, 0], [0, 0, 4, 44], [3, 4, 0, 0], [0, 44, 0, 0]]
#[[0, 4, 44, 0], [4, 0, 0, 3], [44, 0, 0, 0], [0, 3, 0, 0]]

print(g.dijkstra(0)+weight)
        

