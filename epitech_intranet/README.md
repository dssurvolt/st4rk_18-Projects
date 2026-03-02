# 🎓 Epitech Intranet – Full Django Project

## 📌 Description

Ce projet est une implémentation moderne d’un **mini intranet étudiant** développé entièrement avec **Django**.
Il reproduit certains concepts de l’intranet Epitech : gestion des étudiants, modules, notes, notifications et messagerie interne.

Il s’agit d’un projet **full-stack back-end Django** destiné à :

* Approfondir la pratique de Django (modèles, vues, templates, sécurité).
* Créer une architecture claire et réutilisable.
* Servir de démonstration dans un portfolio de développeur.

---

## 🚀 Fonctionnalités principales

* **Authentification** : Login/logout sécurisé avec session Django.
* **Gestion des utilisateurs (étudiants)** : CRUD complet via admin.
* **Modules et Notes** : Association étudiants-modules, gestion des grades.
* **Notifications** : Système de notifications avec marquage lu/non lu.
* **Messagerie interne** : Envoi/réception de messages entre étudiants directement depuis dashboard.
* **Dashboard** : Interface moderne avec stats, modules, notes, notifications, messages.
* **Profils et rôles** : Gestion des rôles (Étudiant, Admin) avec avatars.
* **Design moderne** : Bootstrap 5 avec palette Epitech (rouge, bleu, vert).

---

## ⚙️ Environnement & Dépendances

### Variables d'environnement

Créer un fichier `.env` à la racine :

```
SECRET_KEY=votre-cle-secrete-très-longue-et-aléatoire
DEBUG=True
ALLOWED_HOSTS=localhost,127.0.0.1
DATABASE_URL=sqlite:///db.sqlite3  # ou PostgreSQL en prod
```

### 🔧 Prérequis

* **Python** ≥ 3.10
* **Django** ≥ 5.0

### 📦 Installation

```bash
pip install -r requirements.txt
python manage.py migrate
python manage.py createsuperuser
```

---

## ▶️ Lancement du projet

### Avec Docker (recommandé)

```bash
docker-compose up --build
```

Visite [http://localhost:8000](http://localhost:8000) pour l'app Django.

### Manuel

```bash
python manage.py runserver
```

Visite [http://127.0.0.1:8000](http://127.0.0.1:8000).

---

## 📂 Structure du projet

```
epitech_intranet/
├── core/                     # App Django principale
│   ├── models.py             # Modèles (Student, Module, etc.)
│   ├── views.py              # Vues (login, dashboard, messaging)
│   ├── urls.py               # Routage des endpoints
│   ├── admin.py              # Configuration de l'admin Django
│   ├── signals.py            # Création automatique des UserProfiles
│   └── templates/core/       # Templates HTML avec Bootstrap
├── config/                   # Config Django sécurisée
├── manage.py
├── db.sqlite3
└── README.md
```

---

## 🔐 Authentification & rôles

* **Connexion** via username + mot de passe Django.
* **Déconnexion** via `/logout`.
* **Dashboard** accessible uniquement aux utilisateurs authentifiés.
* **Rôles** (étudiant/admin) gérés via le modèle `UserProfile`.

---

## 🧪 Tests en local

1. Lance le serveur Django.
2. Crée un superuser via `/admin`.
3. Connecte-toi sur `/login`.
4. Envoie un message depuis le dashboard.
5. Vérifie les stats et modules.

---

## 🌟 Améliorations appliquées

* **Design moderne** : Bootstrap 5 avec palette attrayante Epitech.
* **Sécurité** : Variables d'environnement, CSRF, sessions.
* **DevOps** : Docker, migrations, admin.
* **Fonctionnalité** : Messagerie intégrée au dashboard.
* **Performance** : Requêtes optimisées, templates efficaces.

---

## 👨‍💻 Auteur

Projet développé par **Rakib Sobabe** avec refonte full Django par senior dev.
📧 [sobaberakib4@gmail.com](mailto:sobaberakib4@gmail.com)

---