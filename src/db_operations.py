import sqlite3

# Connexion à la base de données
def connexion_db():
    try:
        conn = sqlite3.connect("data/hotel_db.sqlite")
        print("Connexion réussie à la base de données.")
        return conn
    except sqlite3.Error as e:
        print(f"Erreur lors de la connexion à la base de données: {e}")
        return None

# Obtenir la liste des clients
def obtenir_clients():
    try:
        conn = connexion_db()
        if conn is None:
            return []

        cursor = conn.cursor()
        cursor.execute("SELECT * FROM Client")
        clients = cursor.fetchall()
        return clients
    except sqlite3.Error as e:
        print(f"Erreur SQLite lors de la récupération des clients: {e}")
        return []
    finally:
        if conn:
            conn.close()

# Obtenir les réservations avec détails du client et de l'hôtel
def obtenir_reservations():
    query = """
    SELECT R.id_Reservation, C.Nom_complet, C.Email, R.Date_arrivee, R.Date_depart, H.Ville, H.Pays
    FROM Reservation R
    JOIN Client C ON R.id_Client = C.id_Client
    JOIN Concerner Co ON R.id_Reservation = Co.id_Reservation
    JOIN Type_Chambre T ON Co.id_Type = T.id_Type
    JOIN Chambre Ch ON T.id_Type = Ch.id_Type
    JOIN Hotel H ON Ch.id_Hotel = H.id_Hotel;
    """
    try:
        conn = connexion_db()
        if conn is None:
            return []

        cursor = conn.cursor()
        cursor.execute(query)
        reservations = cursor.fetchall()
        return reservations
    except sqlite3.Error as e:
        print(f"Erreur SQLite lors de la récupération des réservations: {e}")
        return []
    finally:
        if conn:
            conn.close()

# Obtenir les chambres disponibles entre deux dates
def obtenir_chambres_disponibles(date_debut, date_fin):
    query = """
    SELECT Ch.id_Chambre, Ch.Numero, Ch.Etage, Ch.Fumeurs, H.Ville, T.Type, T.Tarif
    FROM Chambre Ch
    JOIN Hotel H ON Ch.id_Hotel = H.id_Hotel
    JOIN Type_Chambre T ON Ch.id_Type = T.id_Type
    WHERE Ch.id_Chambre NOT IN (
        SELECT DISTINCT Ch.id_Chambre
        FROM Chambre Ch
        JOIN Type_Chambre T ON Ch.id_Type = T.id_Type
        JOIN Concerner Co ON T.id_Type = Co.id_Type
        JOIN Reservation R ON Co.id_Reservation = R.id_Reservation
        WHERE NOT (R.Date_depart < ? OR R.Date_arrivee > ?)
    );
    """
    try:
        conn = connexion_db()
        if conn is None:
            return []

        cursor = conn.cursor()
        cursor.execute(query, (date_debut, date_fin))
        chambres = cursor.fetchall()
        return chambres
    except sqlite3.Error as e:
        print(f"Erreur SQLite lors de la récupération des chambres disponibles: {e}")
        return []
    finally:
        if conn:
            conn.close()

# Ajouter un nouveau client
def ajouter_client(nom, adresse, ville, code_postal, email, telephone):
    query = """
    INSERT INTO Client (Nom_complet, Adresse, Ville, Code_postal, Email, Telephone)
    VALUES (?, ?, ?, ?, ?, ?)
    """
    try:
        conn = connexion_db()
        if conn is None:
            return

        cursor = conn.cursor()
        cursor.execute(query, (nom, adresse, ville, code_postal, email, telephone))
        conn.commit()
        print(f"Client {nom} ajouté avec succès.")
    except sqlite3.Error as e:
        print(f"Erreur SQLite lors de l'ajout du client: {e}")
    finally:
        if conn:
            conn.close()

# Ajouter une réservation avec une chambre
def ajouter_reservation(id_client, date_arrivee, date_depart, id_chambre):
    try:
        conn = connexion_db()
        if conn is None:
            return

        cursor = conn.cursor()

        # 1. Insérer la réservation
        cursor.execute("""
            INSERT INTO Reservation (id_Client, Date_arrivee, Date_depart)
            VALUES (?, ?, ?)
        """, (id_client, date_arrivee, date_depart))
        reservation_id = cursor.lastrowid

        # 2. Trouver le type de chambre lié à cette chambre
        cursor.execute("SELECT id_Type FROM Chambre WHERE id_Chambre = ?", (id_chambre,))
        result = cursor.fetchone()
        if result:
            id_type = result[0]

            # 3. Ajouter dans la table Concerner
            cursor.execute("""
                INSERT INTO Concerner (id_Reservation, id_Type)
                VALUES (?, ?)
            """, (reservation_id, id_type))

            conn.commit()
            print(f"Réservation pour le client {id_client} ajoutée avec succès.")
        else:
            print("Type de chambre non trouvé pour la chambre sélectionnée.")
    except sqlite3.Error as e:
        print(f"Erreur SQLite lors de l'ajout de la réservation: {e}")
    finally:
        if conn:
            conn.close()

# Obtenir les villes d'hôtels (optionnel pour filtrage)
def obtenir_villes_hotels():
    query = "SELECT DISTINCT Ville FROM Hotel"
    try:
        conn = connexion_db()
        if conn is None:
            return []

        cursor = conn.cursor()
        cursor.execute(query)
        villes = [row[0] for row in cursor.fetchall()]
        return villes
    except sqlite3.Error as e:
        print(f"Erreur SQLite lors de la récupération des villes des hôtels: {e}")
        return []
    finally:
        if conn:
            conn.close()

# Obtenir les types de chambres
def obtenir_types_chambres():
    query = "SELECT id_Type, Type, Tarif FROM Type_Chambre"
    try:
        conn = connexion_db()
        if conn is None:
            return []

        cursor = conn.cursor()
        cursor.execute(query)
        types_chambres = cursor.fetchall()
        return types_chambres
    except sqlite3.Error as e:
        print(f"Erreur SQLite lors de la récupération des types de chambres: {e}")
        return []
    finally:
        if conn:
            conn.close()

