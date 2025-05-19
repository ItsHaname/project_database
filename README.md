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
├── data/                   # Données et scripts SQL
│   ├── create_schema.sql
│   ├── hotel_db.sqlite
│   ├── insert_data.sql
│   └── queries.sql
│
├── env/                    # Environnement virtuel
│   ├── bin/
│   ├── etc/
│   ├── include/
│   ├── lib/
│   ├── lib64/
│   ├── pyvenv.cfg
│   └── share/
│
├── src/                    # Code source
│   ├── db_operations.py    # Fonctions de base de données
│   └── main.py             # Point d'entrée principal pour Streamlit
│
├── tests/                  # Tests unitaires
│   ├── __pycache__/        # Cache Python (généré automatiquement)
│   ├── test_db_operations.py
│   └── test_main.py        # Tests pour main.py
│
├── docs/                   # Documentation du projet (facultatif)
│   └── user_guide.md       # Exemple de documentation
│
├── README.md               # Documentation du projet
├── requirements.txt        # Dépendances principales
├── requirements-dev.txt    # Dépendances pour le développement et tests
└── setup.py                # Fichier de configuration pour installer comme package Python (facultatif)


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










