from multiprocessing.spawn import is_forking

import flet as ft
from UI.view import View
from model.model import Model

from flet.core.dropdown import Dropdown

'''
    CONTROLLER:
    - Funziona da intermediario tra MODELLO e VIEW
    - Gestisce la logica del flusso dell'applicazione
'''

class Controller:
    def __init__(self, view: View, model: Model):
        self._model = model
        self._view = view

        # Variabili per memorizzare le selezioni correnti
        self.museo_selezionato = None
        self.epoca_selezionata = None

    # POPOLA DROPDOWN
    def popola_con_musei (self) :
        elenco_musei = self._model.get_musei()
        lista_nomi_musei = []

        lista_nomi_musei.append (ft.DropdownOption ("Seleziona Museo: "))

        for museo in elenco_musei :
            nome = museo.nome
            lista_nomi_musei.append (ft.DropdownOption (nome))
        return lista_nomi_musei

    def popola_con_epoche (self) :
        lista_epoche = self._model.get_epoche()
        elenco_epoche = []

        elenco_epoche.append (ft.DropdownOption ("Seleziona Epoche: "))

        for epoca in lista_epoche :
            elenco_epoche.append (ft.DropdownOption (epoca))
        return elenco_epoche

    # AZIONE: MOSTRA ARTEFATTI
    def mostra_artefatti_per_museo (self, museo_selezionato) :
        if not self.museo_selezionato :
            return None

        artefatti = self._model.get_artefatti_per_museo (museo_selezionato)
        return artefatti

    def mostra_artefatti_per_epoca (self, epoca_selezionata) :
        if not self.epoca_selezionata :
            return None

        artefatti = self._model.get_artefatti_per_epoca (epoca_selezionata)
        return artefatti

    def mostra_artefatti (self, museo_selezionato, epoca_selezionata) :
        if not self.museo_selezionato or not self.epoca_selezionata :
            return None

        artefatti = self._model.get_artefatti_filtrati (museo_selezionato, epoca_selezionata)
        return artefatti

    def mostra_tutti_artefatti (self) :
        artefatti = self._model.get_artefatti ()
        return artefatti
