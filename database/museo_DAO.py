from database.DB_connect import ConnessioneDB
from model.museoDTO import Museo

import mysql.connector

"""
    Museo DAO
    Gestisce le operazioni di accesso al database relative ai musei (Effettua le Query).
"""

class MuseoDAO:
    def __init__(self):
        pass

    @staticmethod
    def leggi_musei () :
        cnx = None
        cursor = None

        try :
            cnx = ConnessioneDB.get_connection()
            if cnx is None :
                print ("Connessione fallita.")
                return None
            else :
                cursor = cnx.cursor ()
                query = f"SELECT * FROM museo"
                cursor.execute (query)

                righe = cursor.fetchall ()
                musei = []
                if righe :
                    for riga in righe :
                        museo = Museo (*riga)
                        musei.append (museo)
                return musei

        except mysql.connector.Error as error :
            print (f"Errore {error}.")

        finally :
            if cursor :
                cursor.close ()
            if cnx :
                cnx.close ()
