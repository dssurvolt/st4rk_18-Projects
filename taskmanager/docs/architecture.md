# Architecture du Projet TaskManager (Socle iLôt)

Ce document décrit l'architecture technique actuelle du projet, qui sert de base pour le développement de la plateforme de sécurisation foncière **iLôt**.

## Stack Technique

- **Langage** : Java 17 (LTS)
- **Framework** : Spring Boot 3.5.6
- **Gestion de dépendances** : Maven
- **Persistance** : Spring Data JPA
- **Base de données** : H2 (Base de données en mémoire pour le développement)
- **Sécurité** : Spring Security 6.x (Authentification par formulaire, BCrypt pour le hachage des mots de passe)
- **Moteur de template** : Thymeleaf
- **Utilitaires** : Lombok (pour la réduction du code boilerplate)

## Structure du Projet

Le projet suit une architecture en couches standard pour une application Spring Boot :

- `com.example.taskmanager.model` : Contient les entités JPA (ex: `AppUser`, `Task`).
- `com.example.taskmanager.repository` : Interfaces Spring Data JPA pour l'accès aux données.
- `com.example.taskmanager.service` : Couche métier contenant la logique de l'application.
- `com.example.taskmanager.controller` : Contrôleurs Spring MVC gérant les requêtes HTTP et le rendu des vues.
- `com.example.taskmanager.config` : Classes de configuration (Sécurité, etc.).

## Flux de Données

1. L'utilisateur interagit avec l'interface Thymeleaf.
2. Le `Controller` reçoit la requête, valide les données (via `jakarta.validation`).
3. Le `Controller` fait appel au `Service` correspondant.
4. Le `Service` utilise le `Repository` pour persister ou récupérer des données.
5. Le `Controller` renvoie une vue ou redirige l'utilisateur.

## Sécurité

L'application utilise une authentification basée sur une base de données via `JpaUserDetailsService`. Les accès sont restreints par défaut, sauf pour les pages publiques (`/`, `/register`, `/login`, ressources statiques).
