# Guide de Lancement du Projet

Ce document explique comment lancer et accéder à l'application **TaskManager / iLôt**.

## Prérequis

- **Java 17** ou supérieur installé.
- Un terminal à la racine du projet.

## Lancement de l'application

Utilisez le wrapper Maven fourni (`mvnw`) pour lancer l'application. Cela garantit que vous utilisez la bonne version de Maven sans avoir à l'installer manuellement.

### Commande de lancement :
```bash
./mvnw spring-boot:run
```

L'application sera compilée et démarrée. Une fois que vous voyez un message indiquant `Started TaskmanagerApplication in ... seconds`, l'application est prête.

## Accès à l'application

- **Interface Web** : [http://localhost:8080](http://localhost:8080)
- **Console H2 (Base de données)** : [http://localhost:8080/h2-console](http://localhost:8080/h2-console)
  - **JDBC URL** : `jdbc:h2:mem:testdb` (par défaut pour Spring Boot)
  - **User Name** : `sa`
  - **Password** : (laisser vide)

## Commandes Utiles

- **Nettoyer et compiler** : `./mvnw clean compile`
- **Lancer les tests** : `./mvnw test`
- **Générer le package (JAR)** : `./mvnw clean package`
