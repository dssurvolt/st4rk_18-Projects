
---

## 5. ARCHITECTURE TECHNIQUE ET SÉCURITÉ DE HAUTE PRÉCISION (DÉTAIL EXHAUSTIF)

### 5.1 Architecture Microservices Orientée "Simulation" (Micro-VM & Containers)
L'infrastructure d'IronSecur est un chef-d'œuvre d'ingénierie logicielle conçu pour la haute disponibilité et l'isolation extrême. Contrairement aux architectures monolithiques du passé, nous avons adopté un modèle de **Microservices Cloud-Native** orchestré par **Kubernetes (K8s)**. Ce choix technologique permet de séparer les fonctions métier des fonctions de simulation lourde, garantissant une stabilité exemplaire.

#### 5.1.1 Le Core Backend (Logical Layer) : NestJS & TypeScript
L'intelligence administrative de la plateforme est portée par un cluster de services Node.js utilisant le framework **NestJS**. 
*   **API Gateway** : Point d'entrée unique protégé par un pare-feu applicatif (WAF) et un rate-limiter agressif. Elle gère la validation des JWT tokens et le routage des requêtes vers les microservices concernés.
*   **Service d'Identité (IAM Service)** : Gère le cycle de vie des utilisateurs, le RBAC (Role-Based Access Control) et les connexions SSO via OAuth/OpenID Connect.
*   **Service de Paiement (Financial Engine)** : Interfacé avec l'API KKIAPAY, ce service gère les transactions, les abonnements récurrents et la base de données de facturation sécurisée (PCI-DSS compliant).
*   **Service de Notification (Push & Mail)** : Un moteur asynchrone géré via une file d'attente (Redis Pub/Sub) pour envoyer des alertes instantanées de simulation ou des relances de paiement.

#### 5.1.2 Le Moteur de Simulation (Provisionsing Layer) : K8s Operator
Le cœur d'IronSecur est un **K8s Operator propriétaire**. Il s'agit d'un logiciel intelligent qui surveille les demandes de "Labs" des élèves. Lorsqu'un élève clique sur "Démarrer Lab", l'Operator :
1.  Vérifie les ressources disponibles sur le cluster (Auto-scaling proactif).
2.  Provisionne un **Pod à conteneurs multiples** (Sidecar pattern). L'un contient l'interface VDI, l'autre la machine cible vulnérable.
3.  Configure dynamiquement les **Network Policies** pour isoler ce Lab de tous les autres Labs de la plateforme (Isolement L3/L4).
4.  Monte le volume persistant (PVC) de l'élève pour qu'il retrouve ses fichiers.
Ce processus, qui prend moins de 4 secondes, est la clé de l'expérience utilisateur sans couture d'IronSecur.

### 5.2 Technologie VDI (Virtual Desktop Infrastructure) Basse Latence
Pour offrir une expérience de "Bureau" dans un navigateur web, nous utilisons des technologies de pointe en matière de streaming de pixels et de commandes d'entrée.
*   **Connectivité WebSocket / gRPC** : Nous utilisons un tunnel de communication bidirectionnel chiffré. Chaque mouvement de souris et chaque frappe de touche est transmis via WebSocket, tandis que les flux de données lourds utilisent gRPC pour minimiser la latence réseau.
*   **Moteur de Rendu WebGL** : L'interface du Bureau Virtuel sur le client utilise le GPU de l'ordinateur de l'élève pour décompresser et afficher les trames d'image à 60 FPS, offrant une sensation de fluidité identique à une machine locale.
*   **Adaptation Dynamique au Réseau (QoS)** : IronSecur intègre un algorithme de détection de latence. Si l'élève est sur une connexion 3G instable, le système réduit intelligemment la profondeur des couleurs et la résolution du bureau pour privilégier la réactivité au visuel. Dès que le réseau s'améliore, la haute définition est rétablie automatiquement.

### 5.3 Sécurité de l'Infrastructure et Modèle "Zero-Trust"
Une plateforme de cybersécurité ne peut se permettre aucune faille. Notre modèle de sécurité repose sur le principe du **Zero-Trust (Confiance Nulle)**.
*   **Micro-Segmentation Réseau** : Aucun composant de l'infrastructure ne peut parler à un autre sans une autorisation explicite et authentifiée. Les bases de données ne sont accessibles que par les microservices autorisés via des certificats TLS mutuels (mTLS).
*   **Gestion des Secrets (HashiCorp Vault)** : Aucune clé API, aucun mot de passe système n'est stocké en clair dans le code ou les variables d'environnement. Tous les secrets sont gérés par un serveur Vault hautement sécurisé avec rotation automatique hebdomadaire.
*   **Intégrité de la Plateforme (Immutable Infrastructure)** : Les serveurs d'IronSecur sont immutables. En cas de suspicion de compromission d'un nœud Kubernetes, celui-ci est immédiatement détruit et recréé à partir d'une image certifiée saine ("Auto-healing & Remediation").
*   **Protection Anti-DDoS et WAF** : La plateforme est protégée par une couche de protection Cloudflare Enterprise, capable d'absorber des attaques de déni de service massives et de bloquer les attaques applicatives de type OWASP Top 10 avant qu'elles n'atteignent nos serveurs.

### 5.4 Intelligence Artificielle et Moteur Game Master (GMAI)
Le GMAI est un service distribué écrit en Python (FastAPI/TensorFlow) pour ses capacités innées en science des données.
*   **Pipeline de Données en Temps Réel** : Tous les événements de la simulation (commandes terminal, succès quiz, duels) sont injectés dans un flux de données (Kafka). Le GMAI consomme ce flux pour mettre à jour ses modèles de prédiction comportementale.
*   **Analyse de Sentiments et Tuteur IA** : Le tuteur avec lequel l'apprenant discute sur le chat interne virtuel utilise un LLM (Large Language Model) optimisé pour les domaines techniques. Il est capable de comprendre les erreurs de l'élève dans son code et de lui expliquer ses fautes avec une approche pédagogique socratrique (ne pas donner la réponse, mais poser la question qui mène à la réponse).
*   **Détection d'Anomalies (Anti-Cheat)** : Un réseau de neurones surveille les statistiques de duels. Si un joueur progresse trop vite par rapport aux limites physiologiques humaines (ex: capture de flag en 0.5 seconde), le système met son compte en "Observation" pour vérification par un instructeur humain, garantissant que les classements mondiaux restent méritocratiques.

### 5.5 Persistance, Sauvegarde et Continuité d'Activité (PCA/PRA)
Les données de nos apprenants et de nos entreprises partenaires sont précieuses.
*   **Base de Données Haute Disponibilité** : Nous utilisons des clusters PostgreSQL avec réplication synchrone sur trois zones de disponibilité (Regions Cloud) différentes. En cas de panne d'un data center entier, IronSecur bascule en automatique sur le second en moins de 30 secondes.
*   **Stratégie de Backup "3-2-1"** : Trois copies des données, sur deux supports différents, avec une copie hors-site (Air-gapped). Les volumes des Bureaux Virtuels sont sauvegardés quotidiennement de manière incrémentale.
*   **Ancrage Blockchain des Preuves de Maîtrise** : Les résultats des examens et les certificats finaux ne sont pas seulement sauvés en base MySQL. Ils sont hachés et écrits sur la blockchain **Polygon (Ethereum Layer 2)** ou une blockchain privée équivalente. Cela rend les diplômes IronSecur infalsifiables et vérifiables mondialement par n'importe quel recruteur via une application mobile dédiée ou un explorateur de blocs public.

### 5.6 Scalabilité et Optimisation des Coûts Cloud
Gérer des milliers de machines virtuelles simultanément peut coûter cher. Notre architecture a été optimisée pour la rentabilité.
*   **Pods Éphémères** : Dès qu'un élève d'arrête son lab, les ressources (CPU/RAM) sont immédiatement libérées pour les autres.
*   **Instances "Spot" & Réservées** : L'Operator utilise des instances Cloud préemptibles (moins chères) pour les labs non-critiques, réduisant les coûts d'infrastructure de 60%.
*   **Cache Global de Docker Images** : Toutes les images de labs sont pré-chargées dans un registre local ultra-rapide sur chaque nœud physique, évitant les téléchargements lourds et permettant un démarrage de lab quasi-instantané.
