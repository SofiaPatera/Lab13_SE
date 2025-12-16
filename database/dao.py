from database.DB_connect import DBConnect
from model.gene import Gene
from  model.interazione import Interazione
from model.classificazione import Classificazione
class DAO:

    @staticmethod
    def LeggiGene():
        conn = DBConnect.get_connection()
        result = []
        cursor = conn.cursor(dictionary=True)
        query = """ SELECT *
                    FROM gene  """
        cursor.execute(query)
        for row in cursor:
            result.append(Gene(**row)) #oggetti gene
        cursor.close()
        conn.close()
        return result

    @staticmethod
    def LeggiCromosomi():
        conn = DBConnect.get_connection()
        result = []
        cursor = conn.cursor(dictionary=True)
        query = """ SELECT DISTINCT cromosoma
                    FROM gene
                WHERE cromosoma >0"""
        cursor.execute(query)
        for row in cursor:
            result.append(row['cromosoma'])
        cursor.close()
        conn.close()
        return result

    @staticmethod
    def LeggiClassificazione():
        conn = DBConnect.get_connection()
        result = []
        cursor = conn.cursor(dictionary=True)
        query = """ SELECT * 
                    FROM classificazione 
                    """
        cursor.execute(query)
        for row in cursor:
            result.append(Classificazione(**row))
        cursor.close()
        conn.close()
        return result

    @staticmethod
    def LeggiInterazione():
        conn = DBConnect.get_connection()
        result = []
        cursor = conn.cursor(dictionary=True)
        query = """ SELECT g1.id AS gene1 , g1.id AS gene2, i.correlazione
                    FROM gene g1, gene g2, interazione i 
                    WHERE g1.cromosoma != g2.cromosoma #verifico che i cromosomi siano differenti
                    AND g1.cromosoma > 0 
                    AND g2.cromosoma > 0 
                    AND i.id_gene1 = g1.id AND i.id_gene2 = g2.id;  #verificare che esista
                    GROUP BY g1.id, g2.id
                """
        cursor.execute(query)
        for row in cursor:
            result.append((row['gene1'], row['gene2'], row['correlazione']))
        cursor.close()
        conn.close()
        return result

