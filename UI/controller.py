import flet as ft
from UI.view import View
from model.model import Model

class Controller:
    def __init__(self, view: View, model: Model):
        self._view = view
        self._model = model

    def handle_graph(self, e):
        """ Handler per gestire creazione del grafo """""
        # TODO
        self._view.lista_visualizzazione_1.controls.clear()
        self._view.lista_visualizzazione_1.controls.append(ft.Text(f"Grafo calcolato: {self._model.grafo.number_of_nodes()} nodi, "
                                                                   f"{self._model.grafo.number_of_edges()} archi"))
        self._view.page.update()

    def handle_conta_edges(self, e):
        """ Handler per gestire il conteggio degli archi """""
        try:
            soglia = float(self._view.txt_name.value)
        except:
            self._view.show_alert("inserisci una soglia valida: ")
            return
        min_p, max_p = self._model.getArchiPeso_min_max()



    def handle_ricerca(self, e):
        """ Handler per gestire il problema ricorsivo di ricerca del cammino """""
        # TODO