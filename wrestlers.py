# CS 325 Fall 2020 HW 5
# Brittany Sundberg

import sys

with open(sys.argv[1], 'r') as infile:
    n = int(infile.readline().strip())
    V = []
    for m in range(0, n):
        V.append(infile.readline().strip())
    r = int(infile.readline().strip())
    E = []
    for t in range(0, r):
        line = infile.readline().strip()
        rivals = line.split()
        tuple = (rivals[0], rivals[1])
        E.append(tuple)

print("number of wrestlers = ", n)
print("wrestlers are ", V)
print("number of rivalries are ", r)
print("rivalries are ", E)


# Build Adjacency List as a dictionary
Adj = {}
for x in range(0, len(V)):
    Adj[V[x]] = []
    for y in range(0, len(E)):
        if E[y][0] == V[x]:
            Adj[V[x]].append(E[y][1])
        if E[y][1] == V[x]:
            Adj[V[x]].append(E[y][0])

print("Adjacency List is ", Adj)

#Traverse through the Graph with modified BFS
def check_rivalries(V, Adj):
    """traverse through the graph, starting at each vertex individually (in case it's not connected), and see if the rivalries
    are such that each opponent can have a single label - either babyface or heel"""
    babyfaces = []
    heels = []
    for v in V:
        processing = []
        visited = []
        Q = [v]
        processing.append(v)
        if v not in babyfaces and v not in heels:
            babyfaces.append(v)
        #print("current wrestler starting point = ", v)
        while len(Q) > 0:
            u = Q.pop(0)
            #print(u)
            for z in Adj[u]:
                #print(u, " is connected to ", z)
                if z not in visited and z not in processing:
                    processing.append(z)
                    Q.append(z)
                if u in babyfaces:
                    heels.append(z)
                if u in heels:
                    babyfaces.append(z)
            processing.remove(u)
            #print(processing)
            visited.append(u)
            #print("we have visited ", visited)
            #print("babyfaces: ", babyfaces)
            #print("heels: ", heels)
            if u in babyfaces and u in heels:
                print("Impossible")
                return
    babyfaces = list(dict.fromkeys(babyfaces))    #removes duplicates
    heels = list(dict.fromkeys(heels))              #removes duplicates
    print("Yes, it's possible.")
    print("Babyfaces: ", babyfaces)
    print("Heels: ", heels)
    return

check_rivalries(V, Adj)

