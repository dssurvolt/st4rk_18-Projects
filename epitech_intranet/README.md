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
