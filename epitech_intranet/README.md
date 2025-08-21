# 🎓 Epitech Intranet – Django Project

## 📌 Description

Ce projet est une implémentation d’un **mini intranet étudiant** développé avec **Django**.
Il reprend certains concepts de l’intranet Epitech : gestion des étudiants, modules, notes, notifications et messagerie interne.

Il s’agit d’un projet **full-stack back-end Django** destiné à :

* Approfondir la pratique de Django (authentification, ORM, signaux, admin, templates).
* Mettre en place une architecture claire et réutilisable.
* Servir de démonstration dans un portfolio de développeur.

---

## 🚀 Fonctionnalités principales

* **Gestion des utilisateurs (étudiants)**

  * Basée sur un modèle custom `Student` (héritant de `AbstractUser`).
  * Champs supplémentaires : promo, GitHub, email Epitech.
  * Interface d’admin personnalisée.

* **Modules et Notes**

  * Chaque étudiant peut être inscrit dans plusieurs modules.
  * Notes gérées via le modèle `Grade`.

* **Notifications**

  * Système de notifications relié aux étudiants.
  * Possibilité de marquer les notifications comme lues.

* **Messagerie interne**

  * Envoi de messages entre étudiants.
  * Affichage des 5 derniers messages reçus dans le dashboard.

* **Profils et rôles**

  * Modèle `UserProfile` lié à chaque utilisateur.
  * Gestion des rôles (Étudiant, Admin).
  * Possibilité d’ajouter un avatar.

* **Dashboard étudiant**

  * Vue centralisée avec modules, notes, notifications et messages récents.

---

## ⚙️ Environnement & Dépendances

### 🔧 Prérequis

* **Python** ≥ 3.10 (testé sur Python 3.13)
* **pip** ≥ 25.x
* **virtualenv** (fortement recommandé)
* **Django** ≥ 5.0
* Base de données par défaut : **SQLite3** (fichier `db.sqlite3`)

### 📦 Installation des dépendances

Depuis la racine du projet :

```bash
# 1. Créer un environnement virtuel
python3 -m venv venv

# 2. Activer l’environnement
source venv/bin/activate  # Linux/Mac
venv\Scripts\activate     # Windows

# 3. Installer Django et dépendances
pip install --upgrade pip
pip install django
```

*(optionnel)* : si un fichier `requirements.txt` est fourni :

```bash
pip install -r requirements.txt
```

---

## ▶️ Lancement du projet

### 1. Appliquer les migrations

```bash
python manage.py migrate
```

### 2. Créer un superutilisateur

```bash
python manage.py createsuperuser
```

👉 Cela permet de se connecter à `/admin`.

### 3. Lancer le serveur local

```bash
python manage.py runserver
```

Le site est disponible sur : [http://127.0.0.1:8000](http://127.0.0.1:8000).

---

## 📂 Structure du projet

```
epitech_intranet/
│
├── core/                     # App principale
│   ├── models.py             # Modèles (Student, Module, Grade, Message, etc.)
│   ├── views.py              # Vues (login, dashboard, messaging, etc.)
│   ├── urls.py               # Routage des endpoints
│   ├── admin.py              # Configuration de l'admin Django
│   ├── signals.py            # Création automatique des UserProfiles
│   └── templates/core/       # Templates HTML
│
├── manage.py                 # Script principal Django
├── db.sqlite3                # Base de données locale (auto-générée)
└── README.md                 # Documentation du projet
```

---

## 🔐 Authentification & rôles

* **Connexion** via username + mot de passe Django.
* **Déconnexion** via `/logout`.
* **Dashboard** accessible uniquement aux utilisateurs authentifiés.
* **Rôles** (étudiant/admin) gérés via le modèle `UserProfile`.

---

## 🧪 Tests en local

* Ajoute quelques étudiants dans `/admin` ou via `createsuperuser`.
* Connecte-toi sur `/login`.
* Envoie un message à un autre utilisateur depuis `/send-message/`.
* Vérifie ton dashboard `/dashboard/`.

---

## 🌐 Déploiement

Ce projet peut être déployé sur :

* **Heroku** (via `gunicorn` + `Procfile`)
* **Docker** (image Python + dépendances Django)
* **Serveur dédié** (Nginx + Gunicorn + PostgreSQL recommandé pour la prod)

---

## 📌 Points techniques intéressants

* Utilisation de `AbstractUser` pour personnaliser le modèle `Student`.
* Gestion des signaux Django (`post_save`) pour auto-créer les `UserProfile`.
* Relations entre modèles : `ManyToMany` (Modules ↔ Étudiants), `ForeignKey` (Notes, Messages).
* Décoration `@login_required` pour sécuriser l’accès au profil utilisateur.
* Intégration du système de **flash messages** pour feedback utilisateur.

---

## 👨‍💻 Auteur

Projet développé par **Rakib Sobabe**
📧 [rakib.sobabe@epitech.eu](mailto:rakib.sobabe@epitech.eu)

---