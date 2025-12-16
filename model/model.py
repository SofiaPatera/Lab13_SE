import networkx as nx
from database.dao import DAO

class Model:
    def __init__(self):
        self.grafo = nx.Graph()
        self._listaGene = []
        self._cromosomi = []
        self._listaInterazione = []
        self.idMappa = {} #legare un gene al cromosoma

        self._soluzione_best = []

    def load_cromosomi(self):
        #carico cromosomi

    def load_geni(self):
        #mappa7diz che avrà come chiva id del genere e valore il cromosoma (id cromosoma)

    def geni_connessi(self):


        self._listaGene =  DAO.LeggiGene()
        self.grafo.add_nodes_from(self._listaGene) #aggiungo i nodi
        self._listaInterazione = DAO.LeggiInterazione()

    def creaGrafo(self):
        self.grafo.clear()
        self._nodes = []
        self._edges = []
        #creo nodi => prendo lista di cromosomi e aggiungo alla lista di nodi.
        #i nodi sono i cromosomi
        for c in self._cromosomi:
            pass

        #creaiamo i singoli archi del mio grafo
        #prendo la lista geni connessi =>
    def getArchiPeso_min_max(self):
        pesi = []
        if self.grafo.number_of_edges() == 0:
            return None
        for u,v, data in self.grafo.edges(data=True):
            peso = data['peso']
            pesi.append(peso)
        min_pesi = min(pesi)
        max_pesi = max(pesi)
        return min_pesi, max_pesi





