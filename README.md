<div align="center" style="margin: 40px 0;">

<table style="border: none; width: 100%; max-width: 1000px; margin: 0 auto;">
  <tr>
    <td style="text-align: center; padding: 30px; border-right: 1px solid #eee; width: 50%;">
      <img 
        src="https://raw.githubusercontent.com/ItsHaname/Project_CPP_FSSM/main/assets/fssm.png" 
        alt="Logo FSSM"
        style="height: 200px; width: auto; object-fit: contain; display: block; margin: 0 auto;"
      />
      <div style="margin-top: 20px; font-family: 'Segoe UI', sans-serif; font-size: 15px; color: #444; line-height: 1.5;">
        <strong style="font-size: 16px;">Faculté des Sciences Semlalia</strong><br/>
        Université Cadi Ayyad
      </div>
    </td>
    
 <td style="text-align: center; padding: 30px; width: 50%;">
      <img 
        src="https://raw.githubusercontent.com/ItsHaname/Project_CPP_FSSM/main/assets/uni.png" 
        alt="Logo Université"
        style="height: 180px; width: auto; object-fit: contain; display: block; margin: 0 auto;"
      />
      <div style="margin-top: 20px; font-family: 'Segoe UI', sans-serif; font-size: 15px; color: #444; line-height: 1.5;">
        <strong style="font-size: 16px;">Université Cadi Ayyad</strong><br/>
        Marrakech, Maroc
      </div>
    </td>
  </tr>
</table>
</div>
<p align="center">
  <img src="https://readme-typing-svg.herokuapp.com?font=Fira+Code&size=32&pause=1000&color=FFFFFF&center=true&vCenter=true&width=800&lines=%F0%9F%9A%80+Rapport+de+Projet+de+Fin+de+Module" alt="Typing SVG" />
</p>

## Université Cadi Ayyad - Faculté des Sciences Semlalia

#### **Auteurs** :  
### - Hanane AIT BAH  
----
# Project Database - Hotel Management System

## Description

Ce projet est une base de données pour un système de gestion d'hôtel. Il permet de gérer les informations des clients, des réservations, des chambres, des hôtels, des prestations et des évaluations. L'objectif est de permettre aux utilisateurs de réserver des chambres, de consulter les détails des réservations et d'effectuer diverses actions liées à la gestion d'un hôtel.

Le projet utilise une base de données SQLite et un ensemble de scripts Python pour effectuer des opérations sur la base de données.

## Fonctionnalités

- **Gestion des Clients** : Ajout, consultation et modification des informations des clients.
- **Réservations** : Création, modification et consultation des réservations des clients.
- **Chambres** : Gestion des chambres, y compris la disponibilité et les types de chambres.
- **Hôtels** : Informations sur les hôtels, y compris leur localisation et les prestations proposées.
- **Évaluations** : Permet aux clients de laisser des évaluations sur leur séjour.
- **Prestations** : Ajout et gestion des prestations offertes par les hôtels.

## Prérequis

Avant de commencer à utiliser ce projet, vous devez avoir installé les éléments suivants :

- **Python 3.x** : Le projet utilise Python pour l'interaction avec la base de données.
- **SQLite** : Le projet utilise SQLite pour la gestion de la base de données.
- **Virtualenv** (optionnel mais recommandé) : Un environnement virtuel pour gérer les dépendances Python.

### Installation des dépendances

1. **Cloner le repository** :

```bash
git clone https://github.com/ItsHaname/project_database.git
cd project_database
```
Créer et activer un environnement virtuel :

Si tu n'as pas virtualenv installé, installe-le d'abord :

pip install virtualenv

Ensuite, crée et active l'environnement virtuel :

    virtualenv env
    source env/bin/activate  # Sur Linux/Mac
    env\Scripts\activate     # Sur Windows

    Installer les dépendances :

pip install -r requirements.txt

Structure du projet

Voici la structure des fichiers du projet :

project_database/
│
├── data/                  # Contient les fichiers de la base de données et les scripts SQL
│   ├── create_schema.sql  # Script pour créer la structure de la base de données
│   ├── hotel_db.sqlite    # Fichier de la base de données SQLite
│   ├── insert_data.sql    # Script pour insérer des données dans la base de données
│   └── queries.sql        # Script pour effectuer des requêtes SQL personnalisées
│
├── env/                   # Environnement virtuel
│
├── src/                   # Code source du projet
│   ├── db_operations.py   # Contient les fonctions pour interagir avec la base de données
│   └── main.py            # Fichier principal pour exécuter l'application
│
├── tests/                 # Tests du projet
│   └── test_db_operations.py  # Tests unitaires des opérations de base de données
│
├── requirements.txt       # Liste des dépendances du projet
├── requirements-dev.txt   # Liste des dépendances pour le développement
└── README.md              # Ce fichier de documentation

Utilisation
## 1. Créer la base de données

Après avoir installé le projet, tu peux créer la base de données en exécutant le script create_schema.sql pour créer la structure de la base de données.

sqlite3 data/hotel_db.sqlite < data/create_schema.sql

##  2. Insérer des données dans la base

Tu peux insérer des données d'exemple dans la base de données en exécutant le script insert_data.sql :

sqlite3 data/hotel_db.sqlite < data/insert_data.sql

##  3. Utilisation du script Python

Pour interagir avec la base de données, tu peux utiliser le fichier main.py qui permet de tester les différentes fonctionnalités.

Voici un exemple d'utilisation des fonctions du projet en Python :

python src/main.py

Tu peux aussi personnaliser ce fichier pour ajouter des fonctionnalités ou des tests supplémentaires.
##  4. Tests unitaires

Le dossier tests/ contient les tests unitaires pour vérifier les différentes fonctions du projet. Pour exécuter les tests, tu peux utiliser pytest (assure-toi d'avoir installé pytest avec pip install pytest).

pytest tests/test_db_operations.py

Fonctionnement du code

Le code Python interagit avec la base de données SQLite à travers les fonctions définies dans db_operations.py. Ces fonctions permettent de :

    Créer et gérer des clients

    Ajouter et consulter des réservations

    Gérer les chambres et leur disponibilité

    Gérer les prestations et les évaluations des hôtels

Contribution

Les contributions sont les bienvenues ! Si tu souhaites contribuer à ce projet, voici les étapes à suivre :

    Fork ce repository.

    Crée une branche pour ta fonctionnalité (git checkout -b feature/nom-fonctionnalité).

    Fais tes modifications et teste-les.

    Soumets un Pull Request.






    
