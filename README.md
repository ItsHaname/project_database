# 🏨 Projet de Gestion d'Hôtels en SQL & Python

## 📚 Description

Ce projet est une application de gestion d’hôtels. Il est divisé en deux parties :

- **Partie 1** : Création et interrogation d'une base de données MySQL basée sur un modèle conceptuel de données (MCD).
- **Partie 2** : Développement d'une interface web avec **Python**, **SQLite** et **Streamlit** permettant d'interagir avec la base de données (ajout/consultation de clients, réservations, etc.).

---

## 🛠 Technologies Utilisées

- **MySQL Workbench** : pour la création et la gestion de la base de données relationnelle.
- **SQL** : pour écrire les requêtes d'interrogation et de manipulation de données.
- **SQLite** : une base de données légère utilisée pour l'application web.
- **Python** : langage de programmation pour le backend de l'application.
- **Streamlit** : bibliothèque Python pour créer rapidement une interface web.
- **GitHub** : pour le versionnage et le partage du code.

---

## 📁 Structure du Projet

```plaintext
project_database/
├── src/                     # Contient le code source Python
│   ├── main.py              # Application Streamlit principale (anciennement `app.py`)
│   ├── db_operations.py     # Fonctions de gestion de la base de données (anciennement `database.py`)
│   └── utils.py             # (Optionnel) Fonctions utilitaires, comme la gestion des erreurs ou des requêtes répétitives
│
├── data/                    # Contient la base de données et les scripts SQL
│   ├── hotel_db.sqlite      # Base de données SQLite
│   ├── create_schema.sql    # Script pour créer les tables de la base de données (anciennement `creation.sql`)
│   ├── insert_data.sql      # Script pour insérer des données de test dans la base de données (anciennement `insertion.sql`)
│   └── queries.sql          # Requêtes SQL fréquemment utilisées (anciennement `requetes.sql`)
│
├── env/                     # Dossier pour l'environnement virtuel
│   └── mon_env/
│
├── requirements.txt         # Liste des dépendances du projet
├── README.md                # Documentation du projet
└── .gitignore               # Fichier pour ignorer certains fichiers (comme l'environnement virtuel)


```
▶️ Comment exécuter le projet
Partie 1 : Base de données MySQL

    Ouvrir MySQL Workbench

    Exécuter le script creation_tables.sql pour créer les tables

    Remplir les données à l’aide du fichier annexe fourni

    Exécuter les requêtes depuis requetes.sql

Partie 2 : Application Web

    Installer les dépendances :

pip install -r requirements.txt

    Lancer l’application :

streamlit run app/app.py

📽 Démo Vidéo:

🔗 Lien vers la vidéo sur YouTube ou Google Drive
📌 Auteur

Ce projet a été réalisé dans le cadre d’un cours de base de données relationnelle.
Étudiante : Hanane AIT BAH










