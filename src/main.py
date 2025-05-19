import streamlit as st
from datetime import date
from db_operations import (
    obtenir_clients,
    obtenir_reservations,
    obtenir_chambres_disponibles,
    ajouter_client,
    ajouter_reservation
)

# Configuration de la page
st.set_page_config(page_title="Gestion Hôtelière", layout="centered")

# Style CSS personnalisé
st.markdown("""
    <style>
        body {
            background-color: #f9f9f9;
        }
        .main {
            max-width: 900px;
            margin: auto;
            padding: 2rem;
            background-color: #ffffff;
            border-radius: 8px;
            box-shadow: 0 0 10px rgba(0,0,0,0.05);
        }
        h1, h2, h3 {
            color: #2c3e50;
        }
        .stButton > button {
            background-color: #2c3e50;
            color: white;
        }
    </style>
""", unsafe_allow_html=True)

st.markdown('<div class="main">', unsafe_allow_html=True)
st.title("Système de Gestion Hôtelière")

# Menu latéral
menu = st.sidebar.selectbox(
    "Menu principal",
    [
        "Réservations",
        "Clients",
        "Chambres disponibles",
        "Ajouter un client ou une réservation"
    ]
)

# Section : Réservations
if menu == "Réservations":
    st.header("Liste des Réservations")
    reservations = obtenir_reservations()
    if reservations:
        st.table([{
            "ID": r[0],
            "Client": r[1],
            "Arrivée": r[2],
            "Départ": r[3],
            "Chambre": r[4]
        } for r in reservations])
    else:
        st.info("Aucune réservation enregistrée.")

# Section : Clients
elif menu == "Clients":
    st.header("Liste des Clients")
    clients = obtenir_clients()
    if clients:
        st.table([{
            "ID": c[0],
            "Nom": c[6],
            "Email": c[4],
            "Téléphone": c[5],
            "Ville": c[2]
        } for c in clients])
    else:
        st.info("Aucun client enregistré.")

# Section : Chambres disponibles
elif menu == "Chambres disponibles":
    st.header("Vérifier la disponibilité des chambres")
    col1, col2 = st.columns(2)
    with col1:
        debut = st.date_input("Date d'arrivée", date.today())
    with col2:
        fin = st.date_input("Date de départ", date.today())

    if st.button("Vérifier"):
        if debut >= fin:
            st.error("La date de départ doit être postérieure à la date d'arrivée.")
        else:
            chambres = obtenir_chambres_disponibles(str(debut), str(fin))
            if chambres:
                st.success(f"{len(chambres)} chambre(s) disponible(s) trouvée(s).")
                st.table([{
                    "ID": c[0],
                    "Numéro": c[1],
                    "Étage": c[2],
                    "Type": c[5],
                    "Prix": f"{c[6]} €"
                } for c in chambres])
            else:
                st.warning("Aucune chambre disponible pour cette période.")

# Section : Ajouter un client ou une réservation
elif menu == "Ajouter un client ou une réservation":
    st.header("Ajouter un nouveau client")
    with st.form("form_client"):
        nom = st.text_input("Nom complet *")
        email = st.text_input("Adresse email *")
        telephone = st.text_input("Téléphone")
        ville = st.text_input("Ville")
        adresse = st.text_input("Adresse")

        if st.form_submit_button("Enregistrer le client"):
            if nom and email:
                ajouter_client(nom, adresse, ville, "", email, telephone)
                st.success("Client enregistré avec succès.")
            else:
                st.error("Veuillez remplir au minimum les champs obligatoires.")

    st.markdown("---")
    st.header("Ajouter une nouvelle réservation")
    clients_dispo = obtenir_clients()
    if not clients_dispo:
        st.warning("Veuillez d'abord enregistrer un client.")
    else:
        with st.form("form_reservation"):
            client_id = st.selectbox(
                "Client",
                options=[c[0] for c in clients_dispo],
                format_func=lambda x: next(c[6] for c in clients_dispo if c[0] == x)
            )
            col1, col2 = st.columns(2)
            with col1:
                date_arrivee = st.date_input("Date d'arrivée", date.today())
            with col2:
                date_depart = st.date_input("Date de départ", date.today())

            if st.form_submit_button("Valider la réservation"):
                if date_arrivee >= date_depart:
                    st.error("Date de départ invalide.")
                else:
                    chambres = obtenir_chambres_disponibles(str(date_arrivee), str(date_depart))
                    if not chambres:
                        st.error("Aucune chambre disponible.")
                    else:
                        chambre_id = chambres[0][0]  # Choix simplifié
                        ajouter_reservation(client_id, str(date_arrivee), str(date_depart), chambre_id)
                        st.success("Réservation enregistrée avec succès.")
st.markdown('</div>', unsafe_allow_html=True)

