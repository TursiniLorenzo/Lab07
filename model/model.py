from database.museo_DAO import MuseoDAO
from database.artefatto_DAO import ArtefattoDAO

'''
    MODELLO: 
    - Rappresenta la struttura dati
    - Si occupa di gestire lo stato dell'applicazione
    - Si occupa di interrogare il DAO (chiama i metodi di MuseoDAO e ArtefattoDAO)
'''

class Model:
    def __init__(self):
        self._museo_dao = MuseoDAO()
        self._artefatto_dao = ArtefattoDAO()

    # --- ARTEFATTI ---
    def get_artefatti_filtrati(self, museo:str, epoca:str):
        """Restituisce la lista di tutti gli artefatti filtrati per museo e/o epoca (filtri opzionali)."""
        # TODO
        lista_artefatti_filtrati = self._artefatto_dao.leggi_artefatti_filtrati (museo, epoca)
        return lista_artefatti_filtrati

    def get_epoche(self):
        """Restituisce la lista di tutte le epoche."""
        # TODO
        lista_epoche = self._artefatto_dao.leggi_epoche ()
        return lista_epoche

    # --- MUSEI ---
    def get_musei(self):
        """ Restituisce la lista di tutti i musei."""
        # TODO
        lista_musei = MuseoDAO.leggi_musei ()
        return lista_musei






