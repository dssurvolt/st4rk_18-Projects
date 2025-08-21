# 🎓 Epitech Intranet – Django Project

## 📌 Description
Ce projet est une implémentation d’un **mini intranet étudiant** développé avec **Django**.  
Il reprend certains concepts de l’intranet Epitech : gestion des étudiants, modules, notes, notifications et messagerie interne.  

Il s’agit d’un projet **full-stack back-end Django** destiné à :  
- Approfondir la pratique de Django (authentification, ORM, signaux, admin, templates).  
- Mettre en place une architecture claire et réutilisable.  
- Servir de démonstration dans un portfolio de développeur.  

---

## 🚀 Fonctionnalités principales
- 👤 **Gestion des utilisateurs (étudiants)**
  - Modèle `Student` (héritant de `AbstractUser`).  
  - Champs : promo, GitHub, email Epitech.  
  - Interface d’admin personnalisée.  

- 📚 **Modules et Notes**
  - Inscription des étudiants dans plusieurs modules.  
  - Notes gérées via le modèle `Grade`.  

- 🔔 **Notifications**
  - Reliées aux étudiants.  
  - Possibilité de marquer comme lues.  

- ✉️ **Messagerie interne**
  - Envoi de messages entre étudiants.  
  - Affichage des 5 derniers messages reçus.  

- 🧑‍💻 **Profils et rôles**
  - Modèle `UserProfile` lié à chaque utilisateur.  
  - Gestion des rôles (Étudiant, Admin).  
  - Possibilité d’ajouter un avatar.  

- 📊 **Dashboard étudiant**
  - Vue centralisée : modules, notes, notifications, messages récents.  

---

## ⚙️ Environnement & Dépendances

### 🔧 Prérequis
- **Python** ≥ 3.10 (testé sur Python 3.13)  
- **pip** ≥ 25.x  
- **virtualenv** (fortement recommandé)  
- **Django** ≥ 5.0  
- Base de données : **SQLite3**  

### 📦 Installation
```bash
# 1. Créer un environnement virtuel
python3 -m venv venv

# 2. Activer l’environnement
source venv/bin/activate  # Linux/Mac
venv\Scripts\activate     # Windows

# 3. Installer Django
pip install --upgrade pip
pip install django
pip install -r requirements.txt

▶️ Lancement du projet
    1. Appliquer les migrations
    python manage.py migrate
    
    2. Créer un superutilisateur
    python manage.py createsuperuser
    
    
    👉 pour se connecter à /admin.
    
    3. Lancer le serveur
    python manage.py runserver
    
    
    👉 dispo sur : http://127.0.0.1:8000
    
    📂 Structure du projet
    epitech_intranet/
    │
    ├── core/                     # App principale
    │   ├── models.py             # Modèles (Student, Module, Grade, etc.)
    │   ├── views.py              # Vues (login, dashboard, messaging, etc.)
    │   ├── urls.py               # Routage des endpoints
    │   ├── admin.py              # Configuration de l'admin Django
    │   ├── signals.py            # Création auto des UserProfiles
    │   └── templates/core/       # Templates HTML
    │
    ├── manage.py                 # Script principal Django
    ├── db.sqlite3                # Base locale (auto-générée)
    └── README.md                 # Documentation du projet
    
    🔐 Authentification & rôles
    
    🔑 Connexion : username + mot de passe.
    
    🚪 Déconnexion : /logout.
    
    📊 Dashboard : uniquement pour utilisateurs connectés.
    
    🧑‍🏫 Rôles : étudiant / admin via UserProfile.
    
    🧪 Tests en local
    
    Crée quelques étudiants via /admin.
    
    Connecte-toi sur /login.
    
    Envoie un message à un autre utilisateur depuis /send-message/.
    
    Consulte ton dashboard sur /dashboard/.
    
    🌐 Déploiement
    
    Heroku (avec gunicorn + Procfile)
    
    Docker (image Python + dépendances Django)
    
    Serveur dédié (Nginx + Gunicorn + PostgreSQL recommandé en prod)
    
    📌 Points techniques intéressants
    
    AbstractUser → modèle Student personnalisé.
    
    Signaux Django (post_save) pour auto-créer les UserProfile.
    
    Relations ORM : ManyToMany (Modules ↔ Étudiants), ForeignKey (Notes, Messages).
    
    Décorateur @login_required pour sécuriser les pages.
    
    Flash messages pour le feedback utilisateur.
    
    👨‍💻 Auteur
    
    Projet développé par Rakib Sobabe
    📧 rakib.sobabe@epitech.eu