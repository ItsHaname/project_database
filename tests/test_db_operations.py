# tests/test_db_operations.py

import unittest
from src.db_operations import connexion_db  # Remplacer 'connect_db' par 'connexion_db'

class TestDBOperations(unittest.TestCase):
    def test_connection(self):
        # Essayer de se connecter à la base de données
        conn = connexion_db()  # Appel de la fonction correcte
        self.assertIsNotNone(conn)  # Vérifie que la connexion est réussie et non nulle
        conn.close()  # N'oublie pas de fermer la connexion après le test

if __name__ == "__main__":
    unittest.main()

