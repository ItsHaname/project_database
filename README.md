<div align="center">

<table style="width: 100%; border: none;">
  <tr>
    <td align="center" width="50%">
      <img src="https://raw.githubusercontent.com/ItsHaname/Project_CPP_FSSM/main/assets/fssm.png" alt="Logo FSSM" height="180">
      <br/>
      <strong>Faculté des Sciences Semlalia</strong><br/>
      Université Cadi Ayyad
    </td>
    <td align="center" width="50%">
      <img src="https://raw.githubusercontent.com/ItsHaname/Project_CPP_FSSM/main/assets/uni.png" alt="Logo Université" height="160">
      <br/>
      <strong>Université Cadi Ayyad</strong><br/>
      Marrakech, Maroc
    </td>
  </tr>
</table>

<img src="https://readme-typing-svg.herokuapp.com?font=Fira+Code&size=28&pause=1000&color=2AF70C&center=true&vCenter=true&width=800&lines=%F0%9F%9A%80+Projet+de+Base+de+Donn%C3%A9es+:+Gestion+d%E2%80%99H%C3%B4tel" alt="Typing SVG" />
</div>

---

## 🧑‍🎓 Auteur

- **Nom :** Hanane AIT BAH  
- **Encadré à la FSSM - UCA**

---

# 🏨 Système de Gestion d’Hôtel — Base de Données (SQLite + Python)

Ce projet implémente une base de données relationnelle pour la gestion d’un hôtel, avec des fonctionnalités permettant la gestion des **clients**, **réservations**, **chambres**, **prestations**, **évaluations**, et **hôtels**.

L’objectif est de fournir un outil de gestion complet via **SQLite** et **Python** avec des scripts SQL d’initialisation, insertion et interrogation.

---

## ⚙️ Fonctionnalités

- 👤 Gestion des clients (ajout, affichage, modification)
- 🛏️ Gestion des chambres par type et disponibilité
- 📝 Réservations : ajout, affichage par date/client
- 🧼 Gestion des prestations hôtelières
- 🌍 Gestion de plusieurs hôtels (multi-sites)
- ⭐ Évaluations des séjours par les clients

---

## 🧩 Technologies utilisées

| Technologie | Utilisation |
|------------|-------------|
| `SQLite`   | Base de données relationnelle |
| `Python 3.x` | Scripts de gestion et requêtes |
| `SQL` | Création de schéma, insertion, requêtes |
| `Virtualenv` | Environnement virtuel Python |
| `pytest` | Tests unitaires |

---

## 📁 Structure du projet

```bash
project_database/
│
├── data/
│   ├── create_schema.sql     # Création des tables
│   ├── insert_data.sql       # Données d'exemple
│   ├── hotel_db.sqlite       # Fichier SQLite de la base
│   └── queries.sql           # Requêtes SQL personnalisées
│
├── src/
│   ├── db_operations.py      # Fonctions Python de gestion de la DB
│   └── main.py               # Script principal pour tests
│
├── tests/
│   └── test_db_operations.py # Tests unitaires avec pytest
│
├── requirements.txt          # Dépendances de production
├── requirements-dev.txt      # Dépendances pour développement/test
├── setup.py                  # Setup projet (optionnel)
└── README.md                 # Ce fichier
```
 🚀 Installation étape par étape
   1. Cloner le projet     
   ```
git clone https://github.com/ItsHaname/project_database.git
cd project_database
```
  2. Créer un environnement virtuel
````
pip install virtualenv
virtualenv env
source env/bin/activate  # Linux / Mac
env\Scripts\activate     # Windows


````
 3. Installer les dépendances
```
pip install -r requirements.txt
```
🏗️ Initialiser la base de données


1. Créer le schéma de la base

sqlite3 data/hotel_db.sqlite < data/create_schema.sql

2. Ajouter les données d’exemple

sqlite3 data/hotel_db.sqlite < data/insert_data.sql

    ❗ Si vous avez des erreurs UNIQUE constraint failed, videz la base ou supprimez hotel_db.sqlite avant de recommencer.

💻 Lancer le programme

Exécuter le fichier principal Python :

python src/main.py

Ce fichier contient des appels de test aux fonctions définies dans db_operations.py.
✅ Exécuter les tests

Installez pytest si nécessaire :

pip install pytest

Puis lancez les tests :

pytest tests/test_db_operations.py

🧠 Exemples de fonctionnalités Python (extrait)

from db_operations import *

# Ajouter un client
ajouter_client("John Doe", "10 rue Alpha", "Casablanca", "20000", "john@email.com", "0600000000")

# Obtenir toutes les chambres disponibles entre deux dates
chambres = obtenir_chambres_disponibles("2025-06-01", "2025-06-10")
for ch in chambres:
    print(ch)

🤝 Contribution

Les contributions sont bienvenues !
Pour contribuer :

    Fork du projet

    Créer une branche :

git checkout -b feature/nouvelle-fonction

Faire vos modifications + tests

Pousser vos changements :

    git push origin feature/nouvelle-fonction

    Créer une Pull Request sur GitHub

📜 Licence

Projet open-source sous licence MIT.
🧾 Remerciements

    Professeurs de la FSSM - Université Cadi Ayyad

    Support technique de la communauté open source

    Python & SQLite pour leur puissance et simplicité


 <div align="center">
  <img src="https://readme-typing-svg.herokuapp.com?font=Fira+Code&size=22&pause=1000&color=F7C700&center=true&vCenter=true&width=800&lines=Merci+d%E2%80%99avoir+consult%C3%A9+ce+projet+%F0%9F%92%BC;N'oubliez+pas+de+laisser+une+%E2%AD%90+si+vous+l'avez+aim%C3%A9+!;Suivez-moi+pour+d'autres+projets+!+%F0%9F%91%BB" alt="Typing SVG" />
</div>
