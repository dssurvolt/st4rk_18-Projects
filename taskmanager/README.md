
# 📝 Task Manager - Spring Boot (Templates Thymeleaf)

## 📌 Description
Task Manager est une application **Fullstack** permettant de gérer des tâches (CRUD), avec authentification et gestion des utilisateurs.  
Le backend est construit avec **Spring Boot**, sécurisé avec **Spring Security**, et le frontend utilise des **templates Thymeleaf** (pas de React).  

Ce projet sert de base pour apprendre Spring Boot dans son intégralité tout en comprenant les bonnes pratiques d’architecture d’une application moderne avec des templates côté serveur.

---

taskmanager/
## ⚙️ Architecture du Projet

```
taskmanager/
├── src/main/java/com/example/taskmanager
│   ├── controller/     # Contrôleurs Spring MVC
│   ├── model/          # Entités (User, Task, ...)
│   ├── repository/     # Spring Data JPA repositories
│   ├── service/        # Logique métier
│   └── TaskManagerApplication.java
├── src/main/resources/
│   ├── application.properties
│   └── templates/      # Templates Thymeleaf (login, register, tasks)
└── README.md
```

---

## 🗄️ Base de Données

### Modèle Relationnel
- **User**
  - `id` (PK)
  - `username` (unique)
  - `password` (hashé, BCrypt)
  - `email`
  - `roles` (relation ManyToMany avec `Role`)

- **Role**
  - `id` (PK)
  - `name` (`ROLE_USER`, `ROLE_ADMIN`)

- **Task**
  - `id` (PK)
  - `title`
  - `description`
  - `status` (`TODO`, `IN_PROGRESS`, `DONE`)
  - `createdAt`
  - `updatedAt`
  - `user_id` (FK vers User)

---

## 📌 Use Cases

1. **Inscription**
   - Un utilisateur s’inscrit avec username, email, mot de passe.
   - Son mot de passe est hashé avant sauvegarde.

2. **Connexion**
   - L’utilisateur s’authentifie via son `username` & `password`.
   - Retour d’un **JWT** (JSON Web Token) valide.

3. **Gestion des tâches**
   - Créer une tâche
   - Lister ses tâches
   - Modifier une tâche
   - Supprimer une tâche

4. **Sécurité**
   - Un utilisateur **non authentifié** ne peut pas accéder aux endpoints `/api/tasks`.
   - Seuls les administrateurs (`ROLE_ADMIN`) peuvent gérer les utilisateurs.

---

## 🔐 Sécurité (Spring Security + JWT)

- **Spring Security** protège les routes.
- Authentification via **JWT** :
  - `POST /api/auth/login` → retourne un token JWT.
  - Les requêtes suivantes doivent inclure l’en-tête :  
    ```
    Authorization: Bearer <token>
    ```
- Les mots de passe sont hashés avec **BCryptPasswordEncoder**.
- Les rôles (`ROLE_USER`, `ROLE_ADMIN`) permettent de restreindre certaines actions.

---

## ▶️ Lancer le projet

### Prérequis
- **Java 17**
- **Maven 3+**
- **Node.js 18+**
- **npm** ou **yarn**
- **PostgreSQL** ou **MySQL**

### Lancement de l'application
```bash
mvn clean install
mvn spring-boot:run
```

* Application accessible sur : `http://localhost:8080`

Le frontend est directement intégré au backend via les templates **Thymeleaf**. Toutes les pages (login, register, gestion des tâches) sont accessibles depuis l'URL principale du backend. Il n'y a pas de projet React ni d'API séparée pour le frontend.

---

## 🧪 Tests

### Backend

Les tests sont écrits avec **JUnit** et **Spring Boot Test** :

```bash
mvn test
```

### Frontend

Tests avec **Jest** et **React Testing Library** :

```bash
npm test
```

---

## 📦 Dépendances principales

### Backend (Maven `pom.xml`)

* `spring-boot-starter-web`
* `spring-boot-starter-data-jpa`
* `spring-boot-starter-security`
* `thymeleaf` (templates côté serveur)
* `postgresql` ou `mysql-connector-j`

### Frontend

Le frontend utilise uniquement des templates **Thymeleaf** intégrés au projet Spring Boot. Il n'y a pas de dépendances JavaScript ni de fichier `package.json`.

---

## 🔄 Use Flows

### Exemple : Création d’une tâche

1. L’utilisateur se connecte et reçoit un **JWT**.
2. Le frontend envoie une requête :

   ```http
   POST /api/tasks
   Authorization: Bearer <JWT>
   Body: { "title": "Apprendre Spring", "description": "Avec un bon café" }
   ```
3. Le backend valide le token → associe la tâche à l’utilisateur.
4. Retourne la tâche créée avec son `id`.

---

## 📊 Diagrammes UML & Flows

### 1. Diagramme de Classe (Backend - Spring Boot)
```plantuml
@startuml
class User {
  - Long id
  - String username
  - String email
  - String password
  - Set<Role> roles
  + getId()
  + getUsername()
  + getEmail()
  + getPassword()
  + getRoles()
}

class Role {
  - Long id
  - String name
  + getId()
  + getName()
}

class Task {
  - Long id
  - String title
  - String description
  - String status
  - LocalDateTime createdAt
  - LocalDateTime updatedAt
  - User user
  + getId()
  + getTitle()
  + getDescription()
  + getStatus()
  + getUser()
}

User "1" -- "*" Task
User "*" -- "*" Role
@enduml

---

## 🚀 Extensions possibles

* Ajout d’un rôle **Manager** pour superviser plusieurs utilisateurs.
* Gestion de **projets** regroupant plusieurs tâches.
* Ajout d’un **système de notifications**.
* Implémentation de **WebSockets** pour des mises à jour temps réel.

---

## 👨‍💻 Auteur

Projet conçu par **Rakib Sobabe** dans le cadre de l’apprentissage de Spring Boot, avec pour objectif de maîtriser le backend sécurisé et l’intégration fullstack.

---
