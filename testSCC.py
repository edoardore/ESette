from graph import Graph
from matplotlib import pyplot as plt

def test():
    gr=Graph(1000)
    numeroSCC=[]
    for i in range(1,100):
        gr.ShuffleEdge(i)
        numeroSCC.append(gr.printSCCs())
    print numeroSCC
    plt.plot(numeroSCC, label="#SCC all'aumentare della percentuale di archi, grafo dimensione fissa.")
    plt.legend()
    plt.show()


test()