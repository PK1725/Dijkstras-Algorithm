import UI

class Dijkstra:


    table = {}
    tempDict = {}

    def run(self, generator, start, stop):

        for i in range(0, generator.hjørner.antalhjørner):
            self.table[f"{generator.hjørner.positioner[i*5+3]}"] = [0, f"{generator.hjørner.positioner[i*5+3]}", 0]

        for i in range(0, len(generator.hjørner.connections)//2):
            generator.hjørner.connections[i*2] = generator.hjørner.connections[i*2].lower()

        distances = {}
        Q = []
        lastVertex = {}
        distances[start] = 0
        lastVertex[start] = start
        for vertex in self.table:
            Q.append(vertex)
            if vertex != start:
                distances[vertex] = 999999999

        while Q != []:
            vertex = Q[0]
            for val in Q:
                if distances[vertex] > distances[val]:
                    vertex = val


            Q.remove(vertex)
            for nei in self.findNeighbors(vertex=vertex,generator=generator):

                vertex1Length = distances[vertex]
                vertex2Length = distances[generator.hjørner.connections[nei[2]].upper()]

                dLength = next((x for x in generator.hjørner.kanter if
                                x.connection == [generator.hjørner.connections[nei[3]].lower(),
                                                 generator.hjørner.connections[nei[4]]]), None).length
                potLength = vertex1Length + dLength
                if potLength < vertex2Length:
                    distances[generator.hjørner.connections[nei[2]].upper()] = potLength
                    lastVertex[generator.hjørner.connections[nei[2]].upper()] = vertex
        verticesToDest = []
        curVertex = stop
        endVertex = start

        while curVertex != endVertex:
            verticesToDest.append(curVertex)
            curVertex = lastVertex[curVertex]
        verticesToDest.append(endVertex)
        for kant in generator.hjørner.kanter:
            kant.color=(0,0,0)

        for vertex in verticesToDest:
            i = verticesToDest.index(vertex)
            if vertex != start:
                next((x for x in generator.hjørner.kanter if
                      x.connection == [verticesToDest[i+1].lower(),
                                       vertex] or x.connection == [vertex.lower(),
                                                                      verticesToDest[i + 1]]), None).color = (255,0,0)


    def findNeighbors(self,vertex,generator):
        neighbors = []
        for i in range(0, len(generator.hjørner.connections)):
            generator.hjørner.connections[i] = generator.hjørner.connections[i].upper()
        for j in range(0, len(generator.hjørner.connections)):

            if j == 0 and generator.hjørner.connections[j] == vertex:
                neighbors.append([generator.hjørner.connections[j+1],j,j+1, j,j+1])

            elif j%2 == 0 and generator.hjørner.connections[j] == vertex:
                neighbors.append([generator.hjørner.connections[j+1],j,j+1,j,j+1])

            elif j % 2 != 0 and generator.hjørner.connections[j] == vertex:
                neighbors.append([generator.hjørner.connections[j - 1],j,j-1,j-1,j])
        return(neighbors)
    def clear(self):
            self.table = {}

