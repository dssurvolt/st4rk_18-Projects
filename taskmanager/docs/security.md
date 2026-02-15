# Sécurité et Authentification

L'application implémente une couche de sécurité robuste basée sur **Spring Security**.

## Configuration (`SecurityConfig`)

La configuration définit les règles d'accès suivantes :
- **Accès Public** : `/`, `/register`, `/login`, `/css/**`, `/js/**`, et la console H2 (`/h2-console/**`).
- **Accès Restreint** : Toutes les autres requêtes nécessitent une authentification.

## Authentification

L'authentification est gérée par `JpaUserDetailsService`, qui charge les informations de l'utilisateur depuis la table `users`.

### Processus de Connexion
1. L'utilisateur soumet ses identifiants via `/login`.
2. Spring Security compare le mot de passe fourni avec le mot de passe haché en base (via `BCryptPasswordEncoder`).
3. En cas de succès, l'utilisateur est redirigé vers `/tasks`.

## Gestion des Rôles

Actuellement, le système utilise une chaîne de caractères simple pour les rôles (par défaut "USER"). 
*Évolution prévue* : Passage à une gestion de rôles plus fine (ACHETEUR, VENDEUR, NOTAIRE, ADMIN) pour répondre aux besoins de la plateforme iLôt.

## Protection CSRF

La protection CSRF est activée par défaut, sauf pour la console H2 afin de faciliter le développement.

## Frame Options

Les options de frame sont désactivées pour permettre l'affichage de la console H2 dans une iframe.
