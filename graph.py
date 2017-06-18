from collections import defaultdict
import random

class Graph:
    def __init__(self, vertici):
        self.V = vertici
        self.graph = defaultdict(list)

    def addEdge(self, u, v):
        self.graph[u].append(v)

    def DFS(self, v, visited):
        visited[v] = True
        print v,
        for i in self.graph[v]:
            if visited[i] == False:
                self.DFS(i, visited)

    def fillOrder(self, v, visited, stack):
        visited[v] = True
        for i in self.graph[v]:
            if visited[i] == False:
                self.fillOrder(i, visited, stack)
        stack = stack.append(v)

    def getTranspose(self):
        g = Graph(self.V)
        for i in self.graph:
            for j in self.graph[i]:
                g.addEdge(j, i)
        return g

    def printSCCs(self):
        counter=0
        stack = []
        visited = [False] * (self.V)
        for i in range(self.V):
            if visited[i] == False:
                self.fillOrder(i, visited, stack)
        gr = self.getTranspose()
        visited = [False] * (self.V)
        while stack:
            i = stack.pop()
            if visited[i] == False:
                gr.DFS(i, visited)
                print""
                counter=counter+1
        return counter

    def ShuffleEdge(self, percent):
        v=self.V
        edges=round((v*percent)/100)
        for i in range(0,edges):
            self.addEdge(random.randint(0,v-1),random.randint(0,v-1))



def provaClasse():
    # crea grafo di 100 vertici.
    grafo = Graph(100)
    # aggiunge il 40% di archi rispetto al numero di vertici.
    grafo.ShuffleEdge(40)
    # stampa le SCC e stampa ritornando il numero di esse.
    numeroSCC = grafo.printSCCs()
    print numeroSCC

    # stampa la dfs. Creata lista di White(False)
    lista = []
    for i in range(0, 100):
        lista.append(False)
    grafo.DFS(2, lista)
