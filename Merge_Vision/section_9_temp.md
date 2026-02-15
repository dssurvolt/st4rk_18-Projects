
---

## 9. SPÉCIFICATIONS TECHNIQUES BACKEND ET MOBILE (DEEP DIVE APPLICATION)

### 9.1 Architecture de l'Application Mobile (React Native / Expo)
L'application mobile IronSecur est conçue pour être le compagnon de terrain indispensable de l'apprenant. Contrairement à une simple vue web (WebView), nous avons opté pour un développement en **React Native** afin de garantir des performances natives et une expérience utilisateur fluide sur iOS et Android.

#### 9.1.1 Le Moteur de Micro-Learning Offline
Le cœur de l'application mobile est son système de gestion de contenu hors-ligne. 
*   **Synchronisation Delta** : Lorsque l'utilisateur est connecté, l'application télécharge uniquement les nouveaux chapitres et les mises à jour des leçons. Nous utilisons une base de données locale **SQLite** (via WatermelonDB pour des performances de synchronisation optimales) pour stocker les textes, les quiz et les statistiques de progression.
*   **Lecteur Vidéo Optimisé** : Les vidéos de cours peuvent être téléchargées en plusieurs résolutions (360p, 720p, 1080p). L'application gère automatiquement l'espace de stockage et propose de supprimer les chapitres déjà terminés.
*   **Mode Avion / Tunnel** : L'apprenant peut continuer à répondre aux quiz et à lire ses leçons dans les transports ou en zone blanche. Les scores sont mis en cache et envoyés au serveur central dès que la connexion est rétablie, avec un mécanisme de résolution de conflits intelligent.

#### 9.1.2 Le Wallet de Récompenses et Profil Gamifié
L'application mobile sert de "Wallet" pour l'identité numérique de l'élève.
*   **Visualisation 3D du Skill Tree** : Grâce à des bibliothèques de rendu performantes, l'apprenant peut naviguer dans son arbre de compétences avec des animations fluides.
*   **Gestion des Cyber-Crédits** : L'utilisateur peut consulter son solde, voir l'historique de ses achats (via KKIAPAY intégré en mode natif) et transférer des crédits à d'autres membres de sa faction.
*   **Notifications Tactiques** : Utilisation des notifications push (Firebase Cloud Messaging) pour alerter l'élève : "Votre duel contre X commence dans 5 minutes", "Nouveau lab disponible", "Votre facture est prête".

### 9.2 Architecture des API et Micros-services (Spécifications)
Le backend d'IronSecur est une constellation de services robustes et sécurisés. Voici le détail de certains modules critiques.

#### 9.2.1 Service d'Authentification et de Sécurité (Auth-Service)
*   **Standard d'Industrie** : Implémentation complète de OAuth 2.0 et OpenID Connect. 
*   **Multi-Facteur (MFA)** : Support natif des codes TOTP (Google Authenticator) et des notifications push in-app.
*   **Gestion des Jetons (JWT)** : Utilisation de jetons signés avec l'algorithme RS256. Chaque demande d'API est vérifiée par la passerelle de sécurité (API Gateway). Les jetons contiennent les revendications (claims) spécifiques au "Tenant-ID" pour assurer l'étanchéité Multi-SaaS.

#### 9.2.2 Service de Simulation Orchestrée (Lab-Engine)
Ce service est le plus complexe. Il communique avec l'Operator Kubernetes.
*   **Endpoints Critiques** :
    - `POST /labs/start/:labId` : Initie le provisioning.
    - `GET /labs/stream/:sessionId` : Fournit les informations de connexion WebSocket au Bureau Virtuel.
    - `POST /labs/verify/:flagId` : Soumet un flag pour validation pédagogique.
*   **Nettoyage Automatique (Garbage Collector)** : Un service surveille l'inactivité des élèves. Si aucune commande n'est tapée pendant 30 minutes (configurable par le client), la session est mise en pause et les ressources Kubernetes sont libérées pour optimiser les coûts Cloud.

#### 9.2.3 Data Models et Persistance (Schémas)
*   **Table Users** : Stocke les informations de base, le hachage sécurisé du mot de passe (Argon2id), et les métadonnées de profil.
*   **Table Tenants** : Gère les configurations spécifiques de chaque client entreprise (Couleurs, Logo, Domaine, Limite d'utilisateurs).
*   **Table SkillTree** : Un graphe de données représentant tous les nœuds, leurs dépendances (parent/enfant) et les ressources associées (vidéos, labs).
*   **Table Transactions** : Journal exhaustif de tous les paiements KKIAPAY, des Cyber-Crédits générés et consommés.

### 9.3 Infrastructure d'Hébergement et Edge Computing
Pour garantir une expérience sans latence partout dans le monde, IronSecur utilise une stratégie multi-cloud.
*   **Cluster Central (Management Layer)** : Hébergé sur AWS ou Google Cloud pour la robustesse des services managés (Base de données, Queueing).
*   **Nœuds de Simulation Edge (Simulation Layer)** : Déploiement de serveurs Kubernetes dans des data centers régionaux (ex: Datacenters en Afrique de l'Ouest, serveurs OVH en France, DigitalOcean aux USA). L'API Gateway dirige l'élève vers le serveur de simulation le plus proche géographiquement de sa position IP.
*   **CDN (Content Delivery Network)** : Utilisation de Cloudflare pour la mise en cache des images, des vidéos et des fichiers statiques de l'application, réduisant considérablement le temps de chargement initial.

### 9.4 Cycle de Développement et Intégration Continue (DevSecOps)
L'équipe technique d'IronSecur applique les principes du "Secure by Design".
*   **Pipeline CI/CD (GitLab)** : Chaque commit subit une batterie de tests automatiques de qualité de code (Linting) et de sécurité (SAST - Static Application Security Testing).
*   **Scan de Dépendances** : Utilisation d'outils comme Snyk ou Renovate pour s'assurer qu'aucune bibliothèque tierce utilisée dans le projet ne contient de vulnérabilité connue.
*   **Auto-Documentation Swagger** : Toutes les APIs sont documentées dynamiquement, permettant une intégration facile pour nos partenaires B2B qui souhaitent connecter leurs propres outils à l'écosystème IronSecur.
*   **Déploiement en "Canary"** : Les nouvelles fonctionnalités sont d'abord déployées pour 5% des utilisateurs afin de vérifier la stabilité avant une généralisation mondiale.
