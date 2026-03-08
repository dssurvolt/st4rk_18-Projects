# 🎓 Epitech Intranet – Full Django Project

## 📌 Description

Ce projet est une implémentation moderne d'un **mini intranet étudiant** développé entièrement avec **Django**.
Il reproduit certains concepts de l'intranet Epitech : gestion des étudiants, modules, notes, notifications et messagerie interne.

Il s'agit d'un projet **full-stack back-end Django** destiné à :

* Approfondir la pratique de Django (modèles, vues, templates, sécurité).
* Créer une architecture claire et réutilisable.
* Servir de démonstration dans un portfolio de développeur.

---

## 🚀 Fonctionnalités principales

* **Authentification** : Login/logout sécurisé avec session Django.
* **Authentification à deux facteurs (2FA)** : Via TOTP avec QR code pour sécurisation supplémentaire.
* **Gestion des utilisateurs (étudiants)** : CRUD complet via admin.
* **Modules et Notes** : Association étudiants-modules, gestion des grades.
* **Notifications** : Système de notifications avec marquage lu/non lu.
* **Messagerie interne** : Envoi/réception de messages entre étudiants directement depuis dashboard.
* **Recherche full-text** : Recherche dans les messages avec Haystack et Whoosh.
* **Dashboard** : Interface moderne avec stats, modules, notes, notifications, messages.
* **Profils et rôles** : Gestion des rôles (Étudiant, Admin) avec avatars (redimensionnés automatiquement).
* **Pagination** : Pagination Django pour les listes de messages et notifications.
* **Rate limiting** : Limitation des tentatives de connexion et envoi de messages.
* **Notifications email** : Envoi d'emails lors de réception de messages.
* **Cache Redis** : Mise en cache des requêtes fréquentes pour améliorer les performances.
* **Index DB** : Index sur champs fréquemment filtrés pour optimiser les requêtes.
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
REDIS_URL=redis://127.0.0.1:6379/1
CELERY_BROKER_URL=redis://127.0.0.1:6379/0
CELERY_RESULT_BACKEND=redis://127.0.0.1:6379/0
EMAIL_BACKEND=django.core.mail.backends.console.EmailBackend
EMAIL_HOST=smtp.gmail.com
EMAIL_PORT=587
EMAIL_USE_TLS=True
EMAIL_HOST_USER=votre-email@gmail.com
EMAIL_HOST_PASSWORD=votre-mot-de-passe
DEFAULT_FROM_EMAIL=noreply@epitech.eu
```

### 🔧 Prérequis

* **Python** ≥ 3.10
* **Django** ≥ 5.0
* **Redis** (pour cache et Celery)
* **Docker** (optionnel)

### 📦 Installation

```bash
pip install -r requirements.txt
python manage.py migrate
python manage.py rebuild_index  # Pour la recherche
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
# Terminal 1: Redis
redis-server

# Terminal 2: Django
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
│   ├── search_indexes.py     # Index de recherche Haystack
│   ├── templates/core/       # Templates HTML avec Bootstrap
│   └── tests.py              # Tests complets
├── config/                   # Config Django sécurisée
├── .github/workflows/        # CI/CD GitHub Actions
├── whoosh_index/             # Index de recherche Whoosh
├── manage.py
├── db.sqlite3
└── README.md
```

---

## 🔐 Authentification & sécurité

* **Connexion** via username + mot de passe Django.
* **2FA** : Authentification à deux facteurs avec TOTP (Google Authenticator, etc.).
* **Rate limiting** : 5 tentatives de connexion/minute, 10 messages/minute par utilisateur.
* **Déconnexion** via `/logout`.
* **Dashboard** accessible uniquement aux utilisateurs authentifiés.
* **Rôles** (étudiant/admin) gérés via le modèle `UserProfile`.
* **CSRF protection** activée sur tous les formulaires.

---

## 🧪 Tests & CI/CD

### Tests

```bash
python manage.py test
```

Couvre tous les modèles, vues, et fonctionnalités (2FA, email, recherche, etc.).

### CI/CD

Intégré avec **GitHub Actions** :
- Tests automatiques sur push/PR
- Linting avec Flake8 et Black
- Vérification des migrations
- Tests avec Redis

---

## 🌟 Améliorations appliquées

### Performance
* **Cache Redis** pour les requêtes fréquentes (liste étudiants, etc.).
* **Optimisation DB** : `select_related`/`prefetch_related` dans les vues.
* **Index DB** sur `sent_at`, `is_read`, `created_at`.
* **Pagination Django** pour les listes longues.

### Sécurité
* **2FA** avec django-otp et QR codes.
* **Rate limiting** avec django-ratelimit.
* **Variables d'environnement** pour secrets.
* **Validation fichiers** pour les avatars.

### Fonctionnalités
* **Recherche full-text** avec django-haystack.
* **Notifications email** avec send_mail.
* **Upload avatars** avec redimensionnement automatique (300x300px).
* **Messagerie paginée** avec interface moderne.

### DevOps
* **Docker Compose** avec Redis intégré.
* **CI/CD GitHub Actions** pour tests automatiques.
* **Tests complets** (unitaires + fonctionnels).

---

## 👨‍💻 Auteur

Projet développé par **Rakib Sobabe** avec refonte full Django par senior dev.
📧 [sobaberakib4@gmail.com](mailto:sobaberakib4@gmail.com)

---