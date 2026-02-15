
---

## 8. SPÉCIFICATIONS DES MODULES DE FORMATION (CURRICULUM DÉTAILLÉ)

### Introduction au Parcours "Elite Cyber-Agent"
Le curriculum d'IronSecur est conçu pour transformer un débutant motivé en un expert opérationnel en 12 semaines d'immersion totale. Chaque semaine correspond à un jalon de compétences dans le **Skill Tree** et débloque des capacités spécifiques dans l'**Arène PvP**.

#### SEMAINE 1 : Fondations et Environnement de Combat (Linux & Networking)
*   **Objectifs** : Maîtrise du terminal Linux, architecture du noyau, et protocoles réseau fondamentaux (Modèle OSI, TCP/IP, DNS, DHCP).
*   **Labs Pratiques** : Configuration d'un serveur Debian sécurisé, scripts Bash d'automatisation, analyse de trames Wireshark pour comprendre le handshake TCP.
*   **Outils VDI** : Terminal, SSH, tcpdump, Vim/Nano.
*   **Défi Arène** : Course de rapidité dans le terminal (Série de commandes de manipulation de fichiers sous pression).

#### SEMAINE 2 : Web Sécurité - La Rupture des Frontières (OWASP Top 10)
*   **Objectifs** : Comprendre comment fonctionnent les serveurs web et comment les attaquer/défendre. Focus sur les Injections (XSS, CSRF, IDOR).
*   **Labs Pratiques** : Infiltration d'une boutique en ligne vulnérable, contournement de filtres d'authentification par session hijacking.
*   **Outils VDI** : Burp Suite, OWASP ZAP, Nikto, Gobuster.
*   **Défi Arène** : Duel PvP 1v1 d'infiltration CMS. Le premier qui change la page d'accueil du site gagne.

#### SEMAINE 3 : Bases de Données et Injections SQL (Deep Dive)
*   **Objectifs** : Structure des bases de données SQL/NoSQL et techniques d'extraction de données sensibles.
*   **Labs Pratiques** : Extraction manuelle de bases de données MySQL, automatisation avec SQLMap, sécurisation par requêtes préparées.
*   **Outils VDI** : SQLMap, Beekeeper Studio, MySQL Client.
*   **Défi Arène** : Duel d'extraction de données. Récupérer le hash du mot de passe administrateur dans une base de données protégée.

#### SEMAINE 4 : Cryptographie et Gestion des Identités (PKI & IAM)
*   **Objectifs** : Cryptographie symétrique/asymétrique, certificats SSL, signatures numériques et protocoles d'authentification moderne (OAuth, JWT).
*   **Labs Pratiques** : Création d'une autorité de certification (CA) privée, déchiffrement de fichiers protégés, analyse de jetons JWT mal sécurisés.
*   **Outils VDI** : OpenSSL, GnuPG, JWT.io.
*   **Défi Arène** : Casse-tête cryptographique de faction. Déchiffrer un message intercepté pour obtenir les coordonnées du prochain objectif.

#### SEMAINE 5 : Pentest Réseau et Reconnaissance (Scanning & Enumeration)
*   **Objectifs** : Apprendre à cartographier un réseau complexe sans se faire détecter par les IDS (Intrusion Detection Systems).
*   **Labs Pratiques** : Scanning de ports furtif (Stealth Scan), énumération de services SNMP/SMB, découverte d'hôtes sur un réseau local simulé.
*   **Outils VDI** : Nmap, Masscan, Enum4linux, NetDiscover.
*   **Défi Arène** : "Ghost Recon" - Identifier tous les serveurs actifs d'un réseau adverse sans déclencher une seule alerte sonore sur la plateforme.

#### SEMAINE 6 : Exploitation Active Directory (Windows Security)
*   **Objectifs** : Comprendre le cœur des réseaux d'entreprise. Kerberos, LDAP, Group Policies, et techniques de pivotement (Lateral Movement).
*   **Labs Pratiques** : Attaque Pass-the-Hash, exploitation de vulnérabilités Kerberos (Golden Ticket), élévation de privilèges locale.
*   **Outils VDI** : Metasploit, Mimikatz, BloodHound, Impacket.
*   **Défi Arène** : Capture de la Forteresse (Blue vs Red). Une équipe défend l'AD, l'autre tente de devenir Domain Admin.

#### SEMAINE 7 : Analyse de Malware et Obscuration (Reverse Engineering)
*   **Objectifs** : Analyse statique et dynamique de binaires suspects. Comprendre comment les malwares échappent aux antivirus.
*   **Labs Pratiques** : Analyse d'un échantillon de ransomware dans une sandbox isolée, modification d'un exécutable pour contourner une vérification de licence.
*   **Outils VDI** : Ghidra, x64dbg, IDA Free, PeStudio.
*   **Défi Arène** : Analyse Forensics express. Identifier le point d'entrée d'un virus dans un système de fichiers en moins de 15 minutes.

#### SEMAINE 8 : SOC et Réponse aux Incidents (Blue Team Ops)
*   **Objectifs** : Gestion des logs, alertes SIEM, et rédaction de rapports d'incidents professionnels.
*   **Labs Pratiques** : Configuration d'une stack ELK, corrélation d'attaques en temps réel, isolation de machines compromises.
*   **Outils VDI** : Elasticsearch, Kibana, Suricata, Wazuh.
*   **Défi Arène** : Survie SOC. Tenir le site de faction en ligne pendant qu'une attaque automatisée (Botnet) tente de le saturer.

#### SEMAINE 9 : Gouvernance, Risque et Conformité (GRC & ISO 27001)
*   **Objectifs** : Aspects non-techniques mais vitaux. Analyse de risques (EBIOS), normes ISO, RGPD, et audit de sécurité.
*   **Labs Pratiques** : Réalisation d'une analyse de risque complète pour une entreprise fictive, audit de configuration d'un serveur Linux.
*   **Outils VDI** : Tableurs de calcul de risque, outils d'audit automatique (Lynis).
*   **Défi Arène** : "L'Inspecteur" - Trouver le maximum de failles de configuration dans un temps limité.

#### SEMAINE 10 : Sécurité Cloud et DevSecOps (AWS / Azure / K8s)
*   **Objectifs** : Sécuriser les infrastructures modernes. Gestion des secrets, CI/CD sécurisé, et isolation de conteneurs.
*   **Labs Pratiques** : Sécurisation d'un bucket S3, déploiement d'une application via un pipeline GitLab CI sécurisé, audit de cluster Kubernetes.
*   **Outils VDI** : Terraform, AWS CLI, Kubectl, Checkov.
*   **Défi Arène** : Cloud Infiltration. Accéder au panneau de contrôle d'une infrastructure cloud mal configurée.

#### SEMAINE 11 : Sans-fil, IoT et Ingénierie Sociale
*   **Objectifs** : Sécurité Wi-Fi, attaques sur les objets connectés (Bluetooth/RFID), et sensibilisation au Phishing.
*   **Labs Pratiques** : Craquage de clé WPA2 (simulation), création d'une campagne de phishing crédible pour tester les employés virtuels.
*   **Outils VDI** : Aircrack-ng, SET (Social Engineer Toolkit), GoPhish.
*   **Défi Arène** : "The Whisperer" - Duel d'ingénierie sociale via chat interne. Convaincre un NPC de donner un mot de passe.

#### SEMAINE 12 : Projet Final - La Simulation "Iron-Fortress"
*   **Objectifs** : Synthétiser toutes les connaissances. Examen final sous forme de simulation d'invasion cyber à grande échelle.
*   **Scénario** : L'élève est parachuté numériquement dans une ville virtuelle dont les services critiques (Électricité, Eau, Banque) sont sous attaque. Il doit reprendre le contrôle.
*   **Livrable** : Un rapport de remédiation complet et une validation blockchain finale.
*   **Recompense** : Graduation officielle, obtention du titre d'Elite Cyber-Agent et activation du profil dans le module de recrutement prioritaire.
