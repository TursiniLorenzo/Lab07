from database.DB_connect import ConnessioneDB
from model.artefattoDTO import Artefatto

import mysql.connector

"""
    ARTEFATTO DAO
    Gestisce le operazioni di accesso al database relative agli artefatti (Effettua le Query).
"""

class ArtefattoDAO:
    def __init__(self):
        pass

    # TODO
    @staticmethod
    def leggi_epoche () :
        cnx = None
        cursor = None

        try :
            cnx = ConnessioneDB.get_connection ()
            if cnx is None :
                print ("Connessione fallita.")
                return None

            cursor = cnx.cursor ()
            query = "SELECT DISTINCT (epoca) FROM artefatto"
            cursor.execute (query)

            righe = cursor.fetchall ()

            epoche = []
            for riga in righe :
                epoche.append (riga [0])
            return epoche

        except mysql.connector.Error as error :
            print (f"Errore {error}.")
            return None
        finally :
            if cursor :
                cursor.close ()
            if cnx :
                cnx.close ()

    def leggi_artefatti_filtrati (self, nome_museo, epoca) :
        cnx = None
        cursor = None

        try :
            cnx = ConnessioneDB.get_connection ()
            if cnx is None :
                print ("Connessione fallita.")
                return None

            cursor = cnx.cursor ()
            query = ("SELECT a.* FROM artefatto a "
                     "JOIN museo m ON a.id = m.id "
                     "AND m.nome = %s AND a.epoca = %s")

            cursor.execute (query, (nome_museo, epoca))

            righe = cursor.fetchall ()

            artefatti = []
            if righe :
                for riga in righe :
                    artefatto = Artefatto (*riga)
                    artefatti.append (artefatto)
                return artefatti

        except mysql.connector.Error as error :
            print (f"Errore {error}.")
            return None

        finally :
            if cursor :
                cursor.close ()
            if cnx :
                cnx.close ()