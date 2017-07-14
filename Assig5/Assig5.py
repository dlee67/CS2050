class Vertex:

    def __init__(self, key):

        self.id = key

        self.connectedTo = {}

    def addNeighbor(self, nbr, weight = 0):

        self.connectedTo[nbr] = weight

    def __str__(self):

        return str(self.id) + ' connectedTo: ' + str([x.id for x in self.connectedTo])

    def getConnections(self):

        return self.connectedTo.keys()

    def getId(self):

        return self.id

    def getWeight(self, nbr):

        return self.connectedTo[nbr]

class Graph:

    def __init__(self):

        self.vertList = {}

        self.numVertices = 0

    def addVertex(self, key):

        self.numVertices = self.numVertices + 1

        newVertex = Vertex(key)

        self.vertList[key] = newVertex

        return newVertex

    def getVertex(self, n):

#Shouldn't the line below have for instead of if?

        if n in self.vertList:

            return self.vertList[n]

        else:

            return None

    def __contains__(self, n):

        return n in self.vertList

    def addEdge(self, f, t, cost = 0):

        if f not in self.vertList:

            nv = self.addVertex(f)

        if t not in self.vertList:

            nv = self.addVertex(t)

        self.vertList[f].addNeighbor(self.vertList[t], cost)

    def getVertices(self):

        return self.vertList.keys()

    def __iter__(self):

        return iter(self.vertList.values())


graph = Graph()

for i in range(6):

    graph.addVertex(i)

graph.vertList

graph.addEdge(0, 1, 5)

graph.addEdge(0, 5, 2)

graph.addEdge(1,2,4)

graph.addEdge(2,3,9)

graph.addEdge(3,4,7)

graph.addEdge(3,5,3)

graph.addEdge(4,0,1)

graph.addEdge(5,4,8)

graph.addEdge(5,2,1)

for vertex in graph:

    for w in vertex.getConnections():

        print("(%s, %s)" % (vertex.getId(), w.getId()))









