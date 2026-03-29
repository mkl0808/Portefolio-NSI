from PileFile import PileFile
import networkx as nx
import matplotlib.pyplot as plt

class graphe:

    def __init__(self, mat_adj):
        self.__graphe = mat_adj

    def dijkstra(self, sommet_depart, sommet_arrivee):
        observe = PileFile()
        visite = []
        chemin = []
        dejavu = []
        distance = {sommet_depart: 0}
        cycle_detecte = False

        observe.enfiler(sommet_depart)

        while not observe.estVide():
            sommet = observe.defiler()

            if sommet in visite:
                cycle_detecte = True

            for voisin in self.__graphe[sommet]:
                observe.enfiler(voisin)

                nouvelle_distance = distance[sommet] + self.__graphe[sommet][voisin]

                if voisin not in distance or nouvelle_distance < distance[voisin]:
                    distance[voisin] = nouvelle_distance
                    dejavu.append(voisin)
                    visite.append(sommet)

        chemin.append(sommet_arrivee)
        for i in range(len(dejavu) - 1, -1, -1):
            if chemin[-1] == dejavu[i]:
                chemin.append(visite[i])
        if sommet_depart not in chemin:
            chemin.append(sommet_depart)
        chemin.reverse()

        return chemin, distance[sommet_arrivee], cycle_detecte

    def dessiner(self):
        G = nx.DiGraph()
        weighted_edges = []
        for node_p, nodes_s in self.__graphe.items():
            for node_s, weight in nodes_s.items():
                weighted_edges.append((node_p, node_s, weight))
        G.add_weighted_edges_from(weighted_edges)
        pos = nx.spring_layout(G, seed=2)
        nx.draw_networkx(G, pos)
        labels = nx.get_edge_attributes(G, 'weight')
        nx.draw_networkx_edge_labels(G, pos, edge_labels=labels)
        plt.show()


if __name__ == "__main__":
    adj = {'A':{'B':15,'C':4},'B':{'E':5},'C':{'E':11,'D':2},'D':{'E':3},'E':{}}
    adj1 = {'Z':{'B':185,'T':296},'B':{'R':205,'T':245},'R':{'C':179,'T':200},'C':{'L':164,'P':332},'T':{'P':242},'P':{'V':203,'M':168},'V':{'L':102,'M':213},'M':{},'L':{}}
    g = graphe(adj1)
    chemin, distance, cycle = g.dijkstra('Z', 'L')
    print("Chemin le plus court :", chemin)
    print("Distance totale :", distance)
    print("Cycle détecté :", cycle)
    g.dessiner()

