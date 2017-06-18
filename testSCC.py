from graph import Graph
from matplotlib import pyplot as plt

def testA():
    gr=Graph(1000)
    numeroSCC=[]
    for i in range(1,100):
        gr.ShuffleEdge(i)
        numeroSCC.append(gr.printSCCs())
    plt.plot(numeroSCC, label="#SCC all'aumentare della percentuale di archi, grafo dimensione fissa.")
    plt.legend()
    plt.show()


def testB():
    i=1
    numeroSCC=[]
    while i<1000:
        g=Graph(i)
        g.ShuffleEdge(100)
        numeroSCC.append(g.printSCCs())
        i=i+1
    plt.plot(numeroSCC, label="#SCC all'aumentare della dimensione del grafo con percentuale archi del 100%.")
    plt.legend()
    plt.show()

testA()
testB()