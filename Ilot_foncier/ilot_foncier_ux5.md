## PHASE 1 : ANALYSE DES USE CASES ET USER STORIES

### 1.1 Identification des Personas

#### Persona 1 : **Adjovi** (Primo-Accédant)
- **Âge :** 32 ans
- **Profession :** Fonctionnaire
- **Situation :** Veut acheter son premier terrain à Cotonou
- **Pain Points :** Peur de l'arnaque, ne connaît pas les prix du marché, budget limité
- **Objectif :** Trouver un terrain légitime à bon prix

#### Persona 2 : **Koffi** (Propriétaire Multiple)
- **Âge :** 55 ans  
- **Profession :** Commerçant prospère
- **Situation :** Possède 5 parcelles dans différentes villes
- **Pain Points :** Difficile de suivre les taxes, crainte d'occupation illégale
- **Objectif :** Gérer efficacement son patrimoine foncier

#### Persona 3 : **Maman Fifame** (Vendeuse Rurale)
- **Âge :** 48 ans
- **Profession :** Agricultrice
- **Situation :** Veut vendre une terre familiale pour financer l'école des enfants
- **Pain Points :** Analphabète, ne sait pas utiliser internet, peur des intermédiaires
- **Objectif :** Vendre rapidement et en toute sécurité

#### Persona 4 : **Maître Rodrigue** (Notaire)
- **Âge :** 42 ans
- **Profession :** Notaire
- **Situation :** Gère 200+ dossiers fonciers/an
- **Pain Points :** Clients anxieux qui appellent constamment, vérifications fastidieuses
- **Objectif :** Offrir un meilleur service et réduire sa charge administrative

---

### 1.2 Use Cases Principaux (Priorisés pour MVP)

#### 🔥 PRIORITÉ 1 - MVP (Must Have)

##### UC-001 : Vérifier un Titre Foncier
**Acteur Principal :** Acheteur potentiel (Adjovi)  
**Déclencheur :** Un vendeur présente un titre foncier  
**Préconditions :** Utilisateur inscrit OU accès en mode invité (limité)  
**Flux Principal :**
1. Utilisateur ouvre l'app mobile
2. Clique sur "Vérifier un titre"
3. Choisit mode de scan : QR Code OU Photo du document OU Saisie manuelle du numéro
4. Système analyse le document (OCR + API e-foncier si possible)
5. Affiche le statut : ✅ Authentique | ⚠️ Suspect | ❌ Frauduleux
6. Présente les détails : propriétaire, localisation, historique
7. Propose d'enregistrer l'alerte "Surveiller ce titre"

**Flux Alternatifs :**
- 4a. Document illisible → Demander de reprendre la photo
- 4b. Titre non trouvé dans la base → Suggérer vérification manuelle auprès d'un notaire partenaire
- 4c. Titre sous litige actif → Afficher avertissement rouge + détails du contentieux

**Postconditions :** Rapport de vérification généré (PDF téléchargeable)

**User Stories Associées :**
- US-001 : "En tant qu'acheteur, je veux scanner un titre en 10 secondes pour savoir s'il est authentique"
- US-002 : "En tant qu'acheteur, je veux voir l'historique complet des propriétaires pour détecter les signaux d'alerte"
- US-003 : "En tant qu'utilisateur gratuit, je veux faire 3 vérifications/mois pour tester le service avant de payer"

---

##### UC-002 : S'inscrire et Créer un Compte
**Acteur Principal :** Tout nouveau utilisateur  
**Déclencheur :** Première visite sur la plateforme  
**Flux Principal :**
1. Utilisateur arrive sur l'écran d'accueil
2. Clique sur "Créer un compte"
3. Choisit méthode d'inscription :
   - Numéro de téléphone (+ OTP via SMS)
   - Email + mot de passe
   - Connexion via Google/Facebook
4. Accepte les CGU (case à cocher obligatoire)
5. Reçoit OTP et le valide
6. Remplit profil basique : nom, ville, statut (acheteur/vendeur/propriétaire)
7. Système crée le compte et envoie email/SMS de bienvenue
8. Redirige vers onboarding interactif (3 étapes)

**Flux Alternatifs :**
- 5a. OTP non reçu → Renvoyer après 60 secondes
- 5b. OTP expiré → Redemander génération
- 6a. Numéro déjà utilisé → Proposer "Se connecter" ou récupération de compte

**User Stories :**
- US-004 : "En tant que nouvel utilisateur, je veux m'inscrire en moins de 2 minutes"
- US-005 : "En tant qu'utilisateur sans email, je veux pouvoir créer un compte uniquement avec mon numéro MTN/Moov"

---

##### UC-003 : Rechercher un Terrain à Vendre
**Acteur Principal :** Acheteur (Adjovi)  
**Déclencheur :** Besoin d'acquérir un terrain  
**Flux Principal :**
1. Accède à l'onglet "Marketplace"
2. Définit critères de recherche :
   - Localisation (carte interactive OU liste de quartiers)
   - Budget (slider : min-max)
   - Surface (en m²)
   - Type : résidentiel/commercial/agricole
3. Active filtres optionnels :
   - Avec titre foncier uniquement ✓
   - Viabilisé (eau/électricité)
   - Près des axes routiers
4. Voit résultats sur carte + liste
5. Clique sur une annonce pour voir détails :
   - Photos HD / Vidéo drone
   - Prix au m²
   - Score de confiance (0-100)
   - Documents disponibles
   - Profil vendeur (notation)
6. Sauvegarde favoris OU contacte vendeur

**Flux Alternatifs :**
- 2a. Ne sait pas quel quartier → Active "Autour de moi" (géolocalisation)
- 5a. Annonce signalée frauduleuse → Bannière d'avertissement

**User Stories :**
- US-006 : "En tant qu'acheteur, je veux filtrer par budget pour voir seulement ce que je peux me permettre"
- US-007 : "En tant qu'acheteur, je veux voir les terrains sur une carte pour comprendre l'emplacement"
- US-008 : "En tant qu'acheteur, je veux un score de confiance pour éviter les arnaques"

---

##### UC-004 : Publier une Annonce de Vente
**Acteur Principal :** Vendeur (Maman Fifame via assistance)  
**Préconditions :** Compte vérifié + preuve de propriété  
**Flux Principal :**
1. Clique sur "Vendre mon terrain"
2. Upload documents obligatoires :
   - Photo du titre foncier (scan automatique)
   - Photo de la pièce d'identité
   - Certificat de non-litige (optionnel mais recommandé)
3. Système vérifie automatiquement l'authenticité (UC-001)
4. Si valide, remplit le formulaire :
   - Adresse exacte (+ pin sur carte)
   - Surface
   - Prix demandé
   - Description (guide IA pour suggestions)
5. Upload photos du terrain (min 3, max 20)
6. Choisit option publication :
   - Gratuite (visible 30 jours, position standard)
   - Boostée (10 000 FCFA - top résultats 60 jours)
7. Valide et soumet pour modération (24h max)
8. Reçoit notification de publication

**Flux Alternatifs :**
- 3a. Document invalide → Refus avec explication + option "Contacter support"
- 4a. Terrain déjà en vente par quelqu'un d'autre → Alerte fraude + blocage
- 7a. Photos de mauvaise qualité → Suggestion de photographe partenaire (50 000 FCFA)

**User Stories :**
- US-009 : "En tant que vendeur, je veux que mes documents soient vérifiés automatiquement pour publier rapidement"
- US-010 : "En tant que vendeur analphabète, je veux une assistance vocale pour publier mon annonce"
- US-011 : "En tant que vendeur, je veux savoir si mon prix est cohérent avec le marché"

---

##### UC-005 : Consulter le Prix du Marché
**Acteur Principal :** Tout utilisateur  
**Déclencheur :** Besoin d'évaluer un terrain  
**Flux Principal :**
1. Accède à "Observatoire des Prix"
2. Sélectionne ville → quartier → type de terrain
3. Voit statistiques :
   - Prix moyen au m² (évolution 12 derniers mois en graphique)
   - Prix min/max observés
   - Nombre de transactions récentes
   - Heatmap des prix par zone
4. Utilise calculateur : entre sa surface → obtient estimation
5. Compare avec sa transaction en cours
6. Télécharge rapport PDF (version premium)

**User Stories :**
- US-012 : "En tant qu'acheteur, je veux connaître le prix réel du marché pour négocier"
- US-013 : "En tant que vendeur, je veux savoir à quel prix afficher mon terrain"

---

#### 🔶 PRIORITÉ 2 - Post-MVP (Should Have)

##### UC-006 : Gérer Mon Portefeuille Foncier
**Acteur Principal :** Propriétaire multiple (Koffi)  
**Flux Principal :**
1. Accède à "Mes Biens"
2. Voit dashboard :
   - Carte avec tous ses terrains géolocalisés
   - Valeur totale estimée du patrimoine
   - Alertes actives (taxes à payer, documents à renouveler)
3. Clique sur un bien spécifique :
   - Détails complets
   - Historique de valeur
   - Documents scannés
   - Dépenses associées (taxes, travaux)
4. Active surveillance satellite :
   - Photo satellite actuelle
   - Comparaison avec photo il y a 6 mois
   - Alerte si construction non autorisée détectée

**User Stories :**
- US-014 : "En tant que propriétaire, je veux un rappel automatique pour payer mes taxes foncières"
- US-015 : "En tant que propriétaire, je veux être alerté si quelqu'un construit sur mon terrain"

---

##### UC-007 : Effectuer une Transaction Sécurisée (Escrow)
**Acteur Principal :** Acheteur + Vendeur  
**Flux Principal :**
1. Acheteur et vendeur acceptent de transiger via iLôt
2. Acheteur verse le montant sur compte séquestre iLôt
3. Vendeur reçoit notification de fonds déposés
4. Les deux parties prennent RDV chez le notaire (suggestion dans l'app)
5. Notaire valide le transfert de propriété
6. Notaire clique "Transaction complétée" dans l'app
7. Système libère les fonds au vendeur (- commission 0,5%)
8. Les deux parties se notent mutuellement

**Flux Alternatifs :**
- 4a. Litige détecté → Fonds gelés + médiation proposée
- 6a. Transaction annulée → Remboursement automatique à l'acheteur

**User Stories :**
- US-016 : "En tant qu'acheteur, je veux que mon argent soit protégé jusqu'à la signature définitive"
- US-017 : "En tant que vendeur, je veux être sûr de recevoir l'argent rapidement après la vente"

---

##### UC-008 : Obtenir un Conseil Juridique (Chatbot IA)
**Acteur Principal :** Tout utilisateur  
**Flux Principal :**
1. Clique sur "Avocat IA" (icône chat en bas à droite)
2. Pose question en texte OU vocal (fon, français, yoruba)
3. IA analyse et répond en 3-5 secondes
4. Propose ressources complémentaires (articles, vidéos)
5. Si question complexe : "Voulez-vous parler à un vrai avocat ?"
6. Si oui → réservation consultation vidéo (15 000 FCFA/30min)

**User Stories :**
- US-018 : "En tant qu'utilisateur, je veux des réponses juridiques immédiates sans payer un avocat"
- US-019 : "En tant qu'utilisateur, je veux poser mes questions en fon, pas en français"

---

#### 🔵 PRIORITÉ 3 - Future (Nice to Have)

##### UC-009 : Planifier Ma Succession
**Acteur Principal :** Propriétaire senior  
**Flux Principal :**
1. Accède à "Testament Numérique"
2. Liste tous ses biens enregistrés sur iLôt
3. Désigne héritiers + pourcentages de répartition
4. Nomme exécuteur testamentaire
5. Signe électroniquement (certification légale)
6. Document scellé avec blockchain
7. Au décès (déclaré par famille) → héritiers notifiés automatiquement

---

##### UC-010 : Financer Mon Achat (Crédit Intégré)
**Acteur Principal :** Acheteur  
**Flux Principal :**
1. Sur une annonce, clique "Simuler financement"
2. Remplit formulaire : revenus, apport, durée souhaitée
3. Système calcule capacité d'emprunt
4. Affiche offres de banques partenaires
5. Demande crédit directement via l'app
6. Upload documents (scannés)
7. Suivi du dossier en temps réel
8. Décaissement direct lors de la transaction

---

### 1.3 Priorisation Finale (Méthode MoSCoW)

| Priorité | Use Case | Effort (1-10) | Impact (1-10) | Score |
|----------|----------|---------------|---------------|-------|
| **Must Have** | UC-001 Vérification titre | 7 | 10 | 🔥 |
| **Must Have** | UC-002 Inscription | 3 | 9 | 🔥 |
| **Must Have** | UC-003 Recherche terrain | 6 | 9 | 🔥 |
| **Must Have** | UC-004 Publier annonce | 5 | 8 | 🔥 |
| **Must Have** | UC-005 Prix du marché | 4 | 7 | 🔥 |
| **Should Have** | UC-006 Portefeuille | 6 | 7 | 🔶 |
| **Should Have** | UC-007 Escrow | 9 | 9 | 🔶 |
| **Should Have** | UC-008 Chatbot IA | 7 | 6 | 🔶 |
| **Could Have** | UC-009 Succession | 8 | 5 | 🔵 |
| **Could Have** | UC-010 Crédit intégré | 9 | 6 | 🔵 |

---

## PHASE 2 : MODÉLISATION DES USER FLOWS

### 2.1 User Flow Principal : Vérification d'un Titre Foncier

```
[DÉBUT] Utilisateur a un document foncier à vérifier
    ↓
[Page d'accueil] Affiche 3 options principales
    → "Vérifier un titre" (bouton CTA principal)
    → "Acheter un terrain"
    → "Vendre mon terrain"
    ↓
[Clic sur "Vérifier un titre"]
    ↓
[Modal de choix] "Comment souhaitez-vous vérifier ?"
    → Option A : Scanner QR Code
    → Option B : Photographier le document
    → Option C : Saisir numéro manuellement
    ↓
┌─────────────────────────────────────┐
│ BRANCHE A : QR Code                 │
│ 1. Ouvre caméra                     │
│ 2. Détecte QR automatiquement       │
│ 3. Vibre au succès                  │
│ 4. → VA à [Analyse]                 │
└─────────────────────────────────────┘
    ↓
┌─────────────────────────────────────┐
│ BRANCHE B : Photo Document          │
│ 1. Ouvre caméra                     │
│ 2. Guide visuel (cadre vert)        │
│ 3. Prend photo                      │
│ 4. Preview avec "Valider/Reprendre" │
│ 5. Si Valider → OCR extraction      │
│    ↓                                │
│    [OCR Réussi ?]                   │
│    ├─ OUI → VA à [Analyse]          │
│    └─ NON → Message erreur +        │
│              "Reprendre photo"      │
└─────────────────────────────────────┘
    ↓
┌─────────────────────────────────────┐
│ BRANCHE C : Saisie Manuelle         │
│ 1. Formulaire :                     │
│    - Numéro de titre (obligatoire)  │
│    - Région (dropdown)              │
│    - Année (optionnel)              │
│ 2. Bouton "Vérifier"                │
│ 3. → VA à [Analyse]                 │
└─────────────────────────────────────┘
    ↓
[ANALYSE] Loader animé "Vérification en cours..."
    │ (Appel API backend)
    │ (Requête vers base données + e-foncier si API dispo)
    │ (Durée : 2-5 secondes)
    ↓
[RÉSULTAT] 3 scénarios possibles :

┌──────────────────────────────────────┐
│ SCÉNARIO 1 : ✅ TITRE AUTHENTIQUE    │
│ - Badge vert "Vérifié"               │
│ - Détails complets :                 │
│   • Propriétaire actuel              │
│   • Localisation (carte)             │
│   • Surface                          │
│   • Date d'émission                  │
│   • Historique des transferts (3)    │
│   • Statut taxes : À jour ✓          │
│ - Actions possibles :                │
│   [Télécharger rapport PDF]          │
│   [Surveiller ce titre] (alerte)     │
│   [Contacter un notaire partenaire]  │
│ → Parcours terminé avec succès       │
└──────────────────────────────────────┘

┌──────────────────────────────────────┐
│ SCÉNARIO 2 : ⚠️ TITRE SUSPECT        │
│ - Badge orange "Attention"           │
│ - Signaux d'alerte :                 │
│   • Trop de transferts récents (5)   │
│   • Litige en cours (2019)           │
│   • Zone à risque de fraude          │
│ - Recommandation :                   │
│   "Vérification approfondie requise" │
│ - Actions :                          │
│   [Demander audit complet] (payant)  │
│   [Voir détails du litige]           │
│   [Parler à un expert]               │
└──────────────────────────────────────┘

┌──────────────────────────────────────┐
│ SCÉNARIO 3 : ❌ TITRE FRAUDULEUX     │
│ - Badge rouge "Danger"               │
│ - Message :                          │
│   "Ce titre ne figure dans aucune    │
│    base de données officielle"       │
│ - Raisons possibles :                │
│   • Faux document                    │
│   • Numéro inexistant                │
│   • Titre révoqué                    │
│ - Actions :                          │
│   [Signaler la fraude] (police)      │
│   [Obtenir conseil juridique]        │
│   [Bloquer ce vendeur]               │
└──────────────────────────────────────┘
    ↓
[OPTION] "Vérifier un autre titre ?"
    ├─ OUI → Retour au début du flow
    └─ NON → Retour à la page d'accueil

[FIN]
```

**Points de Friction Identifiés :**
1. **OCR pas fiable** → Solution : Permettre ajustements manuels si erreur détectée
2. **Temps d'attente de l'analyse** → Solution : Animation engageante + messages "Le saviez-vous ?" pendant le chargement
3. **Résultat ambigu (suspect)** → Solution : Guide décisionnel clair "Que faire maintenant ?"
4. **Limite gratuite atteinte (3 vérifications)** → Solution : Paywall doux avec explication de la valeur premium

---

### 2.2 User Flow Secondaire : Publication d'une Annonce

```
[DÉBUT] Utilisateur veut vendre son terrain
    ↓
[Page "Vendre"] Explique processus en 5 étapes + durée estimée (10 min)
    ↓
[ÉTAPE 1/5 : Vérification Propriété]
"Prouvez que vous êtes le propriétaire"
    ↓
Upload titre foncier (photo/scan)
    ↓
[Vérification automatique via UC-001]
    ├─ ✅ Valide → Continue
    ├─ ⚠️ Suspect → Avertissement + "Continuer quand même ?" 
    └─ ❌ Invalide → STOP + "Contactez le support"
    ↓
[ÉTAPE 2/5 : Localisation]
"Où se trouve votre terrain ?"
    ↓
Deux options :
    A) Chercher adresse (autocomplete Google Maps)
    B) Placer pin manuellement sur carte
    ↓
Confirme localisation exacte
    ↓
[ÉTAPE 3/5 : Caractéristiques]
Formulaire :
    - Surface (m²) [obligatoire]
    - Type : Résidentiel/Commercial/Agricole [obligatoire]
    - Viabilisé ? (Eau/Électricité) [optionnel]
    - Accessibilité : Route bitumée/Piste [optionnel]
    - Description libre (max 500 caractères)
      → IA suggère amélioration si texte court
    ↓
[ÉTAPE 4/5 : Photos]
"Ajoutez au moins 3 photos"
    ↓
Upload images (drag & drop ou caméra)
    ↓
Système vérifie qualité
    ├─ Floues → "Reprendre pour meilleure visibilité"
    └─ OK → Continue
    ↓
[ÉTAPE 5/5 : Prix]
"Combien demandez-vous ?"
    ↓
Entre prix souhaité (FCFA)
    ↓
Système calcule prix/m² et compare au marché
    ↓
[3 scénarios]
    ├─ Prix cohérent → Badge vert "Prix du marché"
    ├─ 20% au-dessus → Avertissement "Vente difficile"
    └─ 20% en-dessous → "Vous sous-évaluez votre bien"
    ↓
Option boosting :
    [ ] Annonce standard (gratuite, 30j)
    [ ] Annonce premium (10 000 FCFA, top résultats 60j)
    ↓
[RÉCAPITULATIF]
Prévisualisation complète de l'annonce
    ↓
[Valider et Publier]
    ↓
"Votre annonce est en cours de modération (24h max)"
Email + SMS de confirmation
    ↓
[24h plus tard]
Notification : "Votre annonce est en ligne !"
Lien direct vers l'annonce
    ↓
[Tableau de bord vendeur]
Statistiques :
    - Nombre de vues
    - Nombre de contacts
    - Comparaison avec annonces similaires
    ↓
[FIN]
```

**Points de Friction :**
1. **Abandon à l'upload de documents** → Solution : Permettre sauvegarde de brouillon à chaque étape
2. **Prix trop complexe à définir** → Solution : Calculateur automatique basé sur caractéristiques
3. **Photos de mauvaise qualité** → Solution : Guide intégré "Comment bien photographier votre terrain"

---

### 2.3 User Flow Marketplace : Recherche et Contact

```
[DÉBUT] Utilisateur cherche un terrain à acheter
    ↓
[Page Marketplace] Deux modes d'affichage :
    → Vue Carte (par défaut)
    → Vue Liste
    ↓
[Panneau de Filtres] (sidebar gauche)
    - Localisation (autocomplete)
      → Active géolocalisation "Autour de moi"
    - Budget (double slider 0 - 100M FCFA)
    - Surface (slider 100 - 5000 m²)
    - Type de terrain (checkboxes)
    - Avec titre foncier uniquement (toggle)
    - Trier par : Prix | Date | Pertinence
    ↓
[Application des filtres]
Loader 1 seconde
    ↓
[Résultats] 
Carte avec pins colorés selon prix
    + Liste synchronisée sur le côté
    ↓
Hover sur pin → Preview card (photo, prix, m²)
    ↓
[Clic sur annonce]
    ↓
[Page Détail Annonce]
Sections :
    1. Galerie photos (carousel) + badge "Titre vérifié ✓"
    2. Prix + boutons d'action principaux :
       [💬 Contacter] [❤️ Sauvegarder] [📊 Comparer]
    3. Caractéristiques clés (icônes)
    4. Description complète
    5. Carte de localisation
    6. Score de confiance (gauge 0-100)
       → Explications détaillées au clic
    7. Profil vendeur :
       - Photo + nom
       - Note moyenne (⭐ 4.8/5)
       - Nombre de ventes
       - Temps de réponse moyen
       - [Voir autres annonces]
    8. Annonces similaires (suggestion)
    ↓
[Utilisateur clique "Contacter"]
    ↓
[Modal Contact]
Deux options :
    A) Message interne (formulaire pré-rempli)
    B) Appel direct (numéro masqué via VoIP)
    ↓
[Option A : Message]
    ↓
Écrit message (ou utilise modèles suggérés)
    ↓
Envoie → Notification push + SMS au vendeur
    ↓
[Vendeur répond]
    ↓
Notification à l'acheteur
    ↓
[Messagerie interne]
Conversation 1-to-1
    - Envoi de messages texte
    - Partage de documents
    - Proposition de RDV (intégration calendrier)
    - [Passer en transaction sécurisée] (UC-007)
    ↓
[Accord trouvé]
    ↓
Initie transaction escrow OU
Meeting physique arrangé
    ↓
[FIN - CONVERSION]
```

---

## PHASE 3 : WIREFRAMES DÉTAILLÉS (Description Textuelle)

### 3.1 Écran : Page d'Accueil Mobile

**Layout :**
```
┌─────────────────────────────┐
│  [Logo iLôt]    [☰ Menu]    │ ← Header sticky
├─────────────────────────────┤
│                             │
│  👋 Bonjour Adjovi !        │ ← Personnalisation
│                             │
│  ┏━━━━━━━━━━━━━━━━━━━━━━┓   │
│  ┃  [📷 Icon]           ┃   │ ← Card 1 (CTA Principal)
│  ┃  Vérifier un titre   ┃   │   Background gradient bleu
│  ┃  Scannez en 10 sec   ┃   │   Action principale
│  ┗━━━━━━━━━━━━━━━━━━━━━━┛   │
│                             │
│  ┌──────────┐ ┌──────────┐  │ ← Grid 2 colonnes
│  │ Acheter  │ │ Vendre   │  │   Cards secondaires
│  │ [🏘️]     │ │ [💰]     │ │
│  └──────────┘ └──────────┘  │
│                             │
│  📊 Prix du Marché          │ ← Section informative
│  Cotonou: 12 500 F/m²       │
│  [Voir détails →]           │
│                             │
│  🔥 Annonces du Jour        │
│  ┌─────────────────────────┐│
│  │ [Photo] 500m² Akpakpa   ││ ← Carousel horizontal
│  │ 6.5M FCFA ✓             ││   swipe left/right
│  └─────────────────────────┘│
│                             │
│  ⚡ Actions Rapides         │
│  [Mes favoris] [Alertes]    │
│  [Historique] [Support]     │
│                             │
├─────────────────────────────┤
│ [🏠] [🔍] [➕] [💬] [👤]  │ ← Bottom Navigation
└─────────────────────────────┘
```

**Annotations UX :**
- Header transparent qui devient opaque au scroll
- Card "Vérifier" avec micro-animation (pulse subtil)
- Bottom nav fixe, icône centrale "➕" plus grande (action rapide)
- Pull-to-refresh pour actualiser les annonces
- Dark mode toggle dans le menu burger

---

### 3.2 Écran : Scan de Titre Foncier

**Layout :**
```
┌─────────────────────────────┐
│  [← Retour]  Vérification   │
├─────────────────────────────┤
│                             │
│  ┌─────────────────────┐   │
│  │                     │   │
│  │   [Viewfinder       │   │ ← Caméra full screen
│  │    Caméra Active]   │   │   avec overlay
│  │                     │   │
│  │   ┏━━━━━━━━━━━┓    │   │
│  │   ┃           ┃    │   │ ← Cadre de scan vert
│  │   ┃  Placez   ┃    │   │   animé (coins)
│  │   ┃  le QR    ┃    │   │
│  │   ┃   Code    ┃    │   │
│  │   ┗━━━━━━━━━━━┛    │   │
│  │                     │   │
│  └─────────────────────┘   │
│                             │
│  💡 Conseil: Assurez-vous   │ ← Tooltip pédagogique
│     que le document est     │   change selon contexte
│     bien éclairé            │
│                             │
│  ┌───────────────────────┐ │
│  │  📷 Photo Document    │ │ ← Tabs de sélection
│  │  🔢 Saisie Manuelle   │ │   mode actif surligné
│  └───────────────────────┘ │
│                             │
│  [○] Flash  [🖼️] Galerie   │ ← Contrôles caméra
│                             │
└─────────────────────────────┘
```

**États Interactifs :**
1. **Scanning** : Cadre vert + animation scanning lines
2. **Détecté** : Haptic feedback + son + cadre devient bleu
3. **Erreur** : Cadre rouge + message "Document illisible"
4. **Success** : Transition vers écran résultat (slide up)

---

### 3.3 Écran : Résultat de Vérification (Titre Authentique)

**Layout :**
```
┌─────────────────────────────┐
│  [← Retour]  Résultat       │
├─────────────────────────────┤
│                             │
│  ┌─────────────────────┐   │
│  │   ✅ TITRE VÉRIFIÉ  │   │ ← Badge success animé
│  │                     │   │   (checkmark animation)
│  │   Authenticité      │   │
│  │   confirmée         │   │
│  └─────────────────────┘   │
│                             │
│  📋 Détails du Titre        │
│  ┌─────────────────────┐   │
│  │ N°: TF-2024-0012345 │   │
│  │ 📍 Akpakpa, Lot 42B │   │
│  │ 📐 Surface: 450 m²  │   │
│  │ 👤 Proprio: DOSSOU  │   │
│  │ 📅 Émis: 12/03/2020 │   │
│  │ 💰 Taxes: ✓ À jour  │   │
│  └─────────────────────┘   │
│                             │
│  🗺️ Localisation            │
│  [Mini carte interactive]   │ ← Google Maps embed
│  [Voir en grand →]          │
│                             │
│  📊 Historique (3)          │
│  ┌─────────────────────┐   │
│  │ 2020: KOUASSI       │   │ ← Timeline verticale
│  │   ↓ Vente           │   │   expandable
│  │ 2024: DOSSOU        │   │
│  │   (Actuel)          │   │
│  └─────────────────────┘   │
│                             │
│  ⚠️ Signaux               │
│  • Aucun litige détecté ✓  │
│  • Zone sécurisée ✓        │
│  • 1 seul transfert ✓      │
│                             │
│  ┌─────────────────────┐   │
│  │ [📥 Télécharger PDF]│   │ ← Actions principales
│  └─────────────────────┘   │
│  ┌─────────────────────┐   │
│  │ [🔔 Surveiller]     │   │ ← Toggle (ON/OFF)
│  └─────────────────────┘   │
│  ┌─────────────────────┐   │
│  │ [📞 Contacter       │   │
│  │     un Notaire]     │   │
│  └─────────────────────┘   │
│                             │
│  [Vérifier un autre titre] │ ← Action secondaire
│                             │
└─────────────────────────────┘
```

**Micro-interactions :**
- Badge ✅ avec animation Lottie (1 seconde)
- Swipe horizontal sur historique pour voir détails complets
- Bouton "Surveiller" toggle avec animation de cloche
- Share button en haut à droite pour partager le rapport

---

### 3.4 Écran : Marketplace - Vue Liste

**Layout :**
```
┌─────────────────────────────┐
│ [☰]  Terrains  [🔍] [⚙️]   │
├─────────────────────────────┤
│  📍 Localisation: Cotonou   │ ← Filtres actifs
│  💰 Budget: 0 - 10M FCFA    │   (chips cliquables
│  [× Effacer filtres]        │    pour modifier)
├─────────────────────────────┤
│  42 résultats trouvés       │
│  Trier par: [Prix ▼]        │ ← Dropdown de tri
├─────────────────────────────┤
│                             │
│  ┌─────────────────────┐   │
│  │[Photo] ❤️          │   │ ← Card annonce 1
│  │                     │   │
│  │ 500m² - Akpakpa     │   │
│  │ ✅ Titre vérifié    │   │
│  │                     │   │
│  │ 6 500 000 FCFA      │   │
│  │ 13 000 F/m²         │   │
│  │                     │   │
│  │ 👤 Jean DOSSOU ⭐4.8│   │
│  │ 📍 2.3 km           │   │
│  └─────────────────────┘   │
│                             │
│  ┌─────────────────────┐   │
│  │[Photo] ❤️          │   │ ← Card annonce 2
│  │                     │   │
│  │ 350m² - Cadjehoun   │   │
│  │ ⚠️ À vérifier       │   │ ← Badge orange si 
│  │                     │   │   titre suspect
│  │ 4 200 000 FCFA      │   │
│  │ 12 000 F/m²         │   │
│  │                     │   │
│  │ 👤 Marie KOFFI ⭐4.2│   │
│  │ 📍 5.7 km           │   │
│  └─────────────────────┘   │
│                             │
│  ┌─────────────────────┐   │
│  │[Photo] ❤️ 🔥BOOST  │   │ ← Annonce premium
│  │                     │   │   bordure dorée
│  │ 1000m² - Godomey    │   │
│  │ ✅ Titre vérifié    │   │
│  │                     │   │
│  │ 8 000 000 FCFA      │   │
│  │ 8 000 F/m² 📉-20%   │   │ ← Badge promo
│  │                     │   │
│  │ 👤 Pro Immo ⭐4.9   │   │
│  │ 📍 8.1 km           │   │
│  └─────────────────────┘   │
│                             │
│  [Charger plus...]          │ ← Infinite scroll
│                             │
└─────────────────────────────┘
```

**Interactions :**
- Swipe gauche sur card → Actions rapides (Sauvegarder, Partager, Comparer)
- Tap sur photo → Galerie full screen
- Tap sur vendeur → Profil vendeur
- Long press → Preview rapide sans ouvrir la page

---

### 3.5 Écran : Détail d'une Annonce

**Layout (Scrollable) :**
```
┌─────────────────────────────┐
│ [← Retour]      [⋮ Plus]    │
├─────────────────────────────┤
│                             │
│ ┌─────────────────────────┐│
│ │     [Photo Principale]  ││ ← Carousel photos
│ │                         ││   Swipe horizontal
│ │     ● ○ ○ ○ ○           ││   Indicateurs
│ └─────────────────────────┘│
│  ✅ Titre foncier vérifié   │ ← Badge de confiance
│                             │
│  500 m² - Akpakpa           │ ← Titre principal
│                             │
│  💰 6 500 000 FCFA          │ ← Prix (gros)
│     (13 000 F/m²)           │   + prix/m²
│                             │
│  ┌──────────┐ ┌──────────┐ │
│  │ 💬 Contact│ │❤️Sauver │ │ ← CTAs principaux
│  └──────────┘ └──────────┘ │
│                             │
│  ━━━━━━━━━━━━━━━━━━━━━━━  │ ← Séparateur
│                             │
│  📊 Score de Confiance      │
│  ┌─────────────────────┐   │
│  │   [Gauge 85/100]    │   │ ← Jauge circulaire
│  │                     │   │   verte si >70
│  │   Excellent         │   │
│  │   [Voir détails →]  │   │
│  └─────────────────────┘   │
│                             │
│  🏡 Caractéristiques        │
│  ┌─────────────────────┐   │
│  │ 📐 Surface: 500 m²  │   │ ← Grid d'icônes
│  │ 🏘️ Type: Résidentiel│   │   + texte
│  │ 💧 Eau: ✓           │   │
│  │ ⚡ Électricité: ✓   │   │
│  │ 🛣️ Route bitumée: ✓ │   │
│  └─────────────────────┘   │
│                             │
│  📝 Description             │
│  ┌─────────────────────┐   │
│  │ Beau terrain bien   │   │ ← Texte expandable
│  │ situé à Akpakpa,    │   │   "Lire plus..."
│  │ proche de toutes... │   │
│  │ [Lire plus]         │   │
│  └─────────────────────┘   │
│                             │
│  🗺️ Localisation            │
│  ┌─────────────────────┐   │
│  │  [Carte Interactive]│   │ ← Google Maps
│  │                     │   │   avec pin
│  │  📍 Akpakpa, Lot 42B│   │
│  │  [Itinéraire]       │   │
│  └─────────────────────┘   │
│                             │
│  👤 Vendeur                 │
│  ┌─────────────────────┐   │
│  │ [Photo] Jean DOSSOU │   │
│  │ ⭐⭐⭐⭐⭐ 4.8/5      │   │
│  │ • 12 ventes réussies│   │
│  │ • Répond en 2h      │   │
│  │ • Membre depuis 2023│   │
│  │                     │   │
│  │ [Voir profil complet│   │
│  │  + autres annonces] │   │
│  └─────────────────────┘   │
│                             │
│  💬 Avis Acheteurs (8)      │
│  ┌─────────────────────┐   │
│  │ ⭐⭐⭐⭐⭐ Marie K.   │   │ ← Carousel reviews
│  │ "Vendeur sérieux,   │   │   Swipe horizontal
│  │  transaction rapide"│   │
│  │  Il y a 2 mois      │   │
│  └─────────────────────┘   │
│  [Voir tous les avis]       │
│                             │
│  🏘️ Annonces Similaires     │
│  ┌────┐ ┌────┐ ┌────┐     │ ← Horizontal scroll
│  │[Im]│ │[Im]│ │[Im]│     │   3 suggestions
│  │450m│ │520m│ │480m│     │
│  │6.2M│ │7.1M│ │5.8M│     │
│  └────┘ └────┘ └────┘     │
│                             │
│  ⚠️ Signaler un problème    │ ← Footer action
│                             │
└─────────────────────────────┘
```

**Animations :**
- Parallax effect sur la photo principale au scroll
- Score de confiance s'anime au chargement (compteur)
- Carte interactive avec zoom au tap
- Skeleton loader pour chaque section pendant le chargement

---

### 3.6 Écran : Formulaire de Publication d'Annonce (Étape 1/5)

**Layout :**
```
┌─────────────────────────────┐
│ [× Fermer]  Vendre          │
├─────────────────────────────┤
│  ┌─────────────────────┐   │
│  │ ① ━━ ② ── ③ ── ④ ── ⑤│ │ ← Progress bar
│  │ Propriété             │   │   Étape active = bleu
│  └─────────────────────┘   │
│                             │
│  📄 Vérification de Propriété│
│                             │
│  Prouvez que vous êtes      │ ← Instructions claires
│  le propriétaire légitime   │
│                             │
│  ┌─────────────────────┐   │
│  │                     │   │
│  │   📷 Photographier  │   │ ← Zone upload
│  │   votre titre       │   │   Drag & drop
│  │   foncier           │   │   OU tap to browse
│  │                     │   │
│  │   Types acceptés:   │   │
│  │   JPG, PNG, PDF     │   │
│  │   Max: 5 MB         │   │
│  └─────────────────────┘   │
│                             │
│  [OU Choisir dans galerie]  │ ← Alternative action
│                             │
│  ❓ Pourquoi cette étape ?  │ ← Accordion FAQ
│  [Afficher explication]     │   expandable
│                             │
│                             │
│  ┌─────────────────────┐   │
│  │   [Suivant]         │   │ ← CTA désactivé tant
│  └─────────────────────┘   │   que pas d'upload
│                             │
│  💾 Brouillon sauvegardé    │ ← Auto-save indicator
│     il y a 2 minutes        │
│                             │
└─────────────────────────────┘
```

**États du Formulaire :**
1. **Vide** : Zone upload en pointillés, CTA grisé
2. **Upload en cours** : Progress bar circulaire
3. **Document uploadé** : Preview + option "Changer"
4. **Vérification en cours** : Loader "Analyse du titre..."
5. **Vérifié ✅** : Badge vert + CTA activé
6. **Rejeté ❌** : Message d'erreur + option "Contacter support"

---

### 3.7 Écran : Dashboard Vendeur (Mes Annonces)

**Layout :**
```
┌─────────────────────────────┐
│ [☰]  Mes Annonces      [➕] │
├─────────────────────────────┤
│                             │
│  📊 Vue d'ensemble          │
│  ┌─────────────────────┐   │
│  │ 3 Annonces actives  │   │ ← KPIs cards
│  │ 127 Vues totales    │   │   Horizontal scroll
│  │ 18 Contacts reçus   │   │
│  └─────────────────────┘   │
│                             │
│  Filtres: [Toutes ▼]        │
│  • Actives (3)              │
│  • Brouillons (1)           │
│  • Vendues (2)              │
│  • Expirées (0)             │
│                             │
├─────────────────────────────┤
│  ┌─────────────────────┐   │
│  │[Photo] 500m² Akpakpa│   │ ← Card annonce 1
│  │                     │   │
│  │ 🟢 Active           │   │ ← Status badge
│  │ 6 500 000 FCFA      │   │
│  │                     │   │
│  │ 👁️ 45 vues | 💬 6 msg│   │ ← Stats
│  │                     │   │
│  │ Expire dans 22j     │   │
│  │                     │   │
│  │ [Modifier] [Stats]  │   │ ← Quick actions
│  │ [Booster] [Désact.] │   │
│  └─────────────────────┘   │
│                             │
│  ┌─────────────────────┐   │
│  │[Photo] 350m² Godomey│   │ ← Card annonce 2
│  │                     │   │
│  │ 🟡 Brouillon        │   │
│  │ Prix non défini     │   │
│  │                     │   │
│  │ Complété à 60%      │   │
│  │ [▓▓▓▓▓▓░░░░]       │   │ ← Progress bar
│  │                     │   │
│  │ [Continuer]         │   │
│  └─────────────────────┘   │
│                             │
│  ┌─────────────────────┐   │
│  │[Photo] 700m² Cotonou│   │ ← Card annonce 3
│  │                     │   │
│  │ ✅ Vendue           │   │
│  │ 9 500 000 FCFA      │   │
│  │                     │   │
│  │ Vendue le 02/01/25  │   │
│  │ via iLôt Escrow ✓   │   │
│  │                     │   │
│  │ [Voir détails]      │   │
│  │ [Noter l'acheteur]  │   │
│  └─────────────────────┘   │
│                             │
└─────────────────────────────┘
```

---

### 3.8 Écran : Messagerie Interne

**Layout :**
```
┌─────────────────────────────┐
│ [← Retour]  Jean DOSSOU     │
│             🟢 En ligne      │ ← Header avec status
├─────────────────────────────┤
│                             │
│ ┌─────────────────────┐    │
│ │ Annonce: 500m² Akpakpa│  │ ← Context card
│ │ 6.5M FCFA           │    │   (cliquable)
│ │ [Voir l'annonce →]  │    │
│ └─────────────────────┘    │
│                             │
│  📅 Hier                    │ ← Date separator
│                             │
│  Bonjour, le terrain est-il │ ← Message reçu
│  encore disponible ?        │   aligné gauche
│  14:32                      │   bubble gris
│                             │
│              Oui, toujours ! │ ← Message envoyé
│              Voulez-vous    │   aligné droite
│              le visiter ?   │   bubble bleu
│              ✓✓ 14:35       │   double check = lu
│                             │
│  Super ! Je peux samedi     │
│  matin ?                    │
│  14:38                      │
│                             │
│  📅 Aujourd'hui             │
│                             │
│          Parfait ! RDV à 9h │
│          sur place          │
│          ✓ 08:12            │
│                             │
│  ┌─────────────────────┐   │
│  │ 📍 Position partagée│   │ ← Shared location
│  │ [Voir sur la carte] │   │   bubble spécial
│  └─────────────────────┘   │
│  08:15                      │
│                             │
│                             │ ← Espace scroll
│                             │
├─────────────────────────────┤
│ [📎]  [Message...]      [➤]│ ← Input + actions
│                             │
│ [📷 Photo] [📍 Position]    │ ← Actions rapides
│ [📄 Document] [💰 Offre]    │   (expandable)
└─────────────────────────────┘
```

**Features :**
- Typing indicator "Jean est en train d'écrire..."
- Read receipts (✓ envoyé, ✓✓ lu)
- Long press message → Copier/Supprimer/Signaler
- Bouton "Passer en transaction sécurisée" si accord trouvé
- Notifications push quand nouveau message

---

### 3.9 Écran : Portefeuille Foncier (Dashboard Propriétaire)

**Layout :**
```
┌─────────────────────────────┐
│ [☰]  Mon Patrimoine    [➕]│
├─────────────────────────────┤
│                             │
│  💰 Valeur Totale Estimée   │
│  ┌─────────────────────┐    │
│  │                     │    │
│  │  32 500 000 FCFA    │    │ ← Chiffre principal
│  │                     │    │   (compteur animé)
│  │ 📈 +12% cette année │    │
│  └─────────────────────┘    │
│                             │
│  🗺️ Vue Cartographique      │
│  ┌─────────────────────┐    │
│  │  [Carte avec pins]  │    │ ← Tous les terrains
│  │                     │    │   géolocalisés
│  │  ① ② ③ ④            │    │   Numérotés
│  │                     │    │
│  │[Voir en plein écran]|    │
│  └─────────────────────┘    │
│                             │
│  ⚠️ Alertes (2)             │
│  ┌─────────────────────┐    │
│  │ 🔴 Taxe foncière    │    │ ← Alertes urgentes
│  │    Terrain #2       │    │   en rouge
│  │    À payer avant    │    │
│  │    le 15/10         │    │
│  │    [Payer 45 000 F] │    │
│  └─────────────────────┘    │
│  ┌─────────────────────┐    │
│  │ 🟡 Document expire  │    │
│  │    Terrain #4       │    │
│  │    Renouveler avant │    │
│  │    le 30/11         │    │
│  │    [Planifier]      │    │
│  └─────────────────────┘    │
│                             │
│  🏘️ Mes Biens (4)           │
├─────────────────────────────┤
│  ┌─────────────────────┐    │
│  │[Photo] #1 Akpakpa   │    │ ← Card terrain 1
│  │                     │    │
│  │ 500 m² - Résidentiel│    │
│  │ TF-2024-0012345     │    │
│  │                     │    │
│  │ Valeur: 8.5M FCFA   │    │
│  │ 📈 +5% (6 mois)    │     │
│  │                     │     │
│  │ ✅ Taxes à jour     │    │
│  │ 🛰️ Surveillance: ON │    │
│  │                     │    │
│  │ [Détails] [Vendre]  │    │
│  └─────────────────────┘    │
│                             │
│  ┌─────────────────────┐    │
│  │[Photo] #2 Godomey   │    │ ← Card terrain 2
│  │                     │    │
│  │ 750 m² - Commercial │    │
│  │ TF-2022-0087654     │    │
│  │                     │    │
│  │ Valeur: 12M FCFA    │    │
│  │ 📈 +18% (6 mois)    │   │
│  │                     │   │
│  │ ⚠️ Taxe en retard   │   │ ← Warning
│  │ 🛰️ Surveillance: OFF│   │
│  │                     │   │
│  │ [Détails] [Payer]   │   │
│  └─────────────────────┘   │
│                             │
│  [Charger plus...]          │
│                             │
└─────────────────────────────┘
```

---

## PHASE 4 : PROTOTYPAGE INTERACTIF

### 4.1 Outils Recommandés

**Figma (Choix Principal)**
- Prototypage complet avec interactions
- Collaboration en temps réel
- Handoff développeur intégré
- Plugins utiles :
  - Stark (accessibilité)
  - Unsplash (images de placeholder)
  - Content Reel (données réalistes)
  - Map Maker (cartes)

**Structure du Projet Figma :**
```
📁 iLôt Foncier
  ├── 📄 Design System
  │   ├── Colors
  │   ├── Typography
  │   ├── Components
  │   └── Icons
  ├── 📱 Mobile Screens
  │   ├── Onboarding
  │   ├── Auth
  │   ├── Home
  │   ├── Verification
  │   ├── Marketplace
  │   ├── Publishing
  │   └── Profile
  ├── 💻 Web Screens
  │   └── (similaire)
  ├── 🔗 Prototypes
  │   ├── User Flow 1: Vérification
  │   ├── User Flow 2: Achat
  │   └── User Flow 3: Vente
  └── 📚 Documentation
```

### 4.2 Interactions Clés à Prototyper

#### Interaction 1 : Scan de QR Code
```
Trigger: Tap sur "Vérifier un titre"
  ↓
Transition: Slide up (300ms, ease-out)
  ↓
État: Caméra active avec overlay
  ↓
Détection QR: Haptic feedback + animation cadre
  ↓
Transition: Fade to white + slide up résultat (500ms)
  ↓
Résultat: Animation checkmark + confettis si authentique
```

#### Interaction 2 : Filtrage Marketplace
```
Trigger: Tap sur filtre "Budget"
  ↓
Transition: Bottom sheet slide up (250ms)
  ↓
État: Double slider avec valeurs dynamiques
  ↓
Drag: Mise à jour en temps réel du nombre de résultats
  ↓
Trigger: Tap "Appliquer"
  ↓
Transition: Bottom sheet slide down + fade list (200ms)
  ↓
Animation: Résultats apparaissent un par un (stagger 50ms)
```

#### Interaction 3 : Publication Progressive
```
Étape 1 → Étape 2
  ↓
Transition: Slide left + progress bar animation
  ↓
Validation: Shake si champs obligatoires manquants
  ↓
Success: Checkmark vert sur progress step
```

#### Interaction 4 : Score de Confiance
```
Trigger: Scroll jusqu'à section score
  ↓
Animation: Gauge remplit de 0 à valeur finale (1 seconde)
  ↓
État: Couleur change selon valeur (rouge/orange/vert)
  ↓
Trigger: Tap sur "Voir détails"
  ↓
Transition: Expand accordion avec détails (300ms)
```

### 4.3 Micro-animations Essentielles

**Pull-to-refresh**
```
State: Idle (liste normale)
  ↓
User pulls down: Loader icon apparaît + rotation
  ↓
Release: Animation "release" + refresh
  ↓
Data loaded: Liste glisse vers le haut + nouveau contenu
```

**Like/Favorite Animation**
```
Tap: Heart outline → filled
Animation: Scale up (1.3x) + slight rotation
Particles: Mini-hearts explosent
Haptic: Light feedback
Duration: 400ms total
```

**CTA Button States**
```
Normal: Solid color, slight shadow
Hover (web): Scale 1.05, deeper shadow
Active: Scale 0.95, shadow removed
Loading: Spinner inside, text fade out
Success: Checkmark animation, green background
Error: Shake animation, red background
```

---

## PHASE 5 : SPÉCIFICATIONS TECHNIQUES

### 5.1 Architecture Frontend (React Native + Web)

#### Stack Technologique Recommandé

**Frontend Mobile & Web:**
```javascript
// Core
- React Native 0.73+ (Mobile)
- React 18+ (Web)
- TypeScript 5+

// Navigation
- React Navigation 6 (Mobile)
- React Router v6 (Web)

// State Management
- Zustand (simple, performant)
- React Query (server state)

// UI Components
- React Native Paper (Mobile)
- Tailwind CSS + shadcn/ui (Web)

// Maps
- react-native-maps (Mobile)
- @react-google-maps/api (Web)

// Camera/Media
- react-native-vision-camera
- react-native-image-picker

// Forms
- React Hook Form + Zod

// Animations
- react-native-reanimated
- Lottie (complexes animations)

// Charts
- Victory Native (Mobile)
- Recharts (Web)
```

#### Structure des Composants

```
src/
├── components/
│   ├── common/
│   │   ├── Button.tsx
│   │   ├── Input.tsx
│   │   ├── Card.tsx
│   │   ├── Badge.tsx
│   │   └── Loader.tsx
│   ├── verification/
│   │   ├── QRScanner.tsx
│   │   ├── DocumentUpload.tsx
│   │   ├── VerificationResult.tsx
│   │   └── TrustScore.tsx
│   ├── marketplace/
│   │   ├── PropertyCard.tsx
│   │   ├── FilterPanel.tsx
│   │   ├── MapView.tsx
│   │   └── SearchBar.tsx
│   ├── publishing/
│   │   ├── StepIndicator.tsx
│   │   ├── DocumentVerification.tsx
│   │   ├── LocationPicker.tsx
│   │   └── PhotoGallery.tsx
│   └── portfolio/
│       ├── PropertyDashboard.tsx
│       ├── AlertCard.tsx
│       └── SatelliteView.tsx
├── screens/
│   ├── HomeScreen.tsx
│   ├── VerificationScreen.tsx
│   ├── MarketplaceScreen.tsx
│   ├── PropertyDetailScreen.tsx
│   ├── PublishScreen.tsx
│   └── PortfolioScreen.tsx
├── navigation/
│   ├── AppNavigator.tsx
│   ├── AuthNavigator.tsx
│   └── TabNavigator.tsx
├── services/
│   ├── api/
│   │   ├── auth.service.ts
│   │   ├── property.service.ts
│   │   ├── verification.service.ts
│   │   └── messaging.service.ts
│   ├── storage/
│   │   └── secureStorage.ts
│   └── analytics/
│       └── tracker.ts
├── hooks/
│   ├── useAuth.ts
│   ├── useProperties.ts
│   ├── useVerification.ts
│   └── useGeolocation.ts
├── store/
│   ├── authStore.ts
│   ├── propertyStore.ts
│   └── uiStore.ts
├── utils/
│   ├── validation.ts
│   ├── formatting.ts
│   └── constants.ts
└── types/
    ├── property.types.ts
    ├── user.types.ts
    └── api.types.ts
```

---

### 5.2 API Endpoints & Spécifications

#### Base URL
```
Production: https://api.ilot-foncier.bj/v1
Staging: https://staging-api.ilot-foncier.bj/v1
```

#### Authentication

**POST /auth/register**
```typescript
Request:
{
  phoneNumber: string;  // Format: +229XXXXXXXX
  password: string;     // Min 8 chars
  firstName: string;
  lastName: string;
  userType: 'buyer' | 'seller' | 'owner';
}

Response: 201 Created
{
  user: {
    id: string;
    phoneNumber: string;
    firstName: string;
    lastName: string;
    userType: string;
    isVerified: boolean;
    createdAt: string;
  };
  tokens: {
    accessToken: string;  // Expires: 1h
    refreshToken: string; // Expires: 30d
  };
}

Errors:
- 409: Phone number already exists
- 422: Validation error
```

**POST /auth/verify-otp**
```typescript
Request:
{
  phoneNumber: string;
  otp: string;  // 6 digits
}

Response: 200 OK
{
  verified: boolean;
  message: string;
}
```

**POST /auth/login**
```typescript
Request:
{
  phoneNumber: string;
  password: string;
}

Response: 200 OK
{
  user: UserObject;
  tokens: TokensObject;
}

Errors:
- 401: Invalid credentials
- 403: Account not verified
```

---

#### Verification

**POST /verification/scan**
```typescript
Request (multipart/form-data):
{
  documentImage: File;  // JPG/PNG, max 5MB
  scanType: 'qr' | 'ocr' | 'manual';
  titleNumber?: string; // If manual
}

Response: 200 OK
{
  status: 'authentic' | 'suspicious' | 'fraudulent';
  confidence: number;  // 0-100
  property: {
    titleNumber: string;
    owner: string;
    location: {
      address: string;
      coordinates: {
        lat: number;
        lng: number;
      };
    };
    surface: number;  // m²
    issuedDate: string;
    taxStatus: 'upToDate' | 'overdue' | 'unknown';
    transferHistory: Array<{
      date: string;
      fromOwner: string;
      toOwner: string;
    }>;
  };
  warnings: Array<{
    type: 'litigation' | 'multiple_transfers' | 'high_risk_zone';
    message: string;
    severity: 'low' | 'medium' | 'high';
  }>;
  reportUrl: string;  // PDF download link
}

Processing Time: 2-5 seconds
Cache: 24 hours

Errors:
- 400: Invalid document format
- 404: Title not found
- 429: Rate limit exceeded (10 requests/hour for free users)
```

**POST /verification/monitor**
```typescript
Request:
{
  titleNumber: string;
  alertTypes: Array<'transaction' | 'litigation' | 'tax'>;
}

Response: 201 Created
{
  monitorId: string;
  titleNumber: string;
  active: boolean;
  createdAt: string;
}
```

---

#### Properties (Marketplace)

**GET /properties**
```typescript
Query Parameters:
{
  location?: string;       // City or district
  minPrice?: number;
  maxPrice?: number;
  minSurface?: number;
  maxSurface?: number;
  type?: 'residential' | 'commercial' | 'agricultural';
  hasTitle?: boolean;
  hasUtilities?: boolean;  // Water + electricity
  page?: number;           // Default: 1
  limit?: number;          // Default: 20, Max: 100
  sortBy?: 'price' | 'date' | 'surface';
  sortOrder?: 'asc' | 'desc';
  bounds?: {               // For map view
    ne: { lat: number, lng: number };
    sw: { lat: number, lng: number };
  };
}

Response: 200 OK
{
  properties: Array<{
    id: string;
    title: string;
    description: string;
    price: number;
    pricePerSqm: number;
    surface: number;
    location: {
      address: string;
      district: string;
      city: string;
      coordinates: { lat: number, lng: number };
    };
    images: Array<{
      url: string;
      thumbnail: string;
      order: number;
    }>;
    features: {
      type: string;
      hasWater: boolean;
      hasElectricity: boolean;
      isPaved: boolean;
    };
    verification: {
      isVerified: boolean;
      trustScore: number;  // 0-100
    };
    seller: {
      id: string;
      name: string;
      avatar: string;
      rating: number;
      responseTime: string;  // "2 hours"
    };
    stats: {
      views: number;
      favorites: number;
      contacts: number;
    };
    isBoosted: boolean;
    createdAt: string;
    expiresAt: string;
  }>;
  pagination: {
    currentPage: number;
    totalPages: number;
    totalItems: number;
    hasNext: boolean;
    hasPrev: boolean;
  };
  aggregations: {
    avgPrice: number;
    avgPricePerSqm: number;
    minPrice: number;
    maxPrice: number;
  };
}

Cache: 5 minutes
```

**GET /properties/:id**
```typescript
Response: 200 OK
{
  ...PropertyDetail (extended version),
  similarProperties: Array<PropertySummary>;
  priceHistory?: Array<{
    date: string;
    price: number;
  }>;
}

Errors:
- 404: Property not found
- 410: Property no longer available
```

**POST /properties**
```typescript
Request (multipart/form-data):
{
  titleDocument: File;     // Required
  ownerIdDocument: File;   // Required
  location: {
    address: string;
    coordinates: { lat: number, lng: number };
  };
  surface: number;
  price: number;
  type: string;
  description: string;
  features: {
    hasWater: boolean;
    hasElectricity: boolean;
    isPaved: boolean;
  };
  images: File[];          // Min 3, Max 20
  isBoosted: boolean;
}

Response: 201 Created
{
  property: PropertyObject;
  status: 'pending_review' | 'published';
  reviewEstimatedTime: string;  // "24 hours"
}

Errors:
- 403: User not verified
- 422: Validation errors
- 409: Property already listed
```

---

#### Messaging

**GET /messages/conversations**
```typescript
Response: 200 OK
{
  conversations: Array<{
    id: string;
    property: {
      id: string;
      title: string;
      image: string;
    };
    participant: {
      id: string;
      name: string;
      avatar: string;
      isOnline: boolean;
      lastSeen?: string;
    };
    lastMessage: {
      content: string;
      timestamp: string;
      isRead: boolean;
      sender: 'me' | 'them';
    };
    unreadCount: number;
  }>;
}
```

**GET /messages/conversations/:id**
```typescript
Query: { page?: number, limit?: number }

Response: 200 OK
{
  messages: Array<{
    id: string;
    content: string;
    type: 'text' | 'image' | 'location' | 'document';
    sender: {
      id: string;
      name: string;
    };
    timestamp: string;
    status: 'sent' | 'delivered' | 'read';
    metadata?: {
      location?: { lat: number, lng: number };
      fileUrl?: string;
      fileName?: string;
    };
  }>;
  pagination: PaginationObject;
}
```

**POST /messages/send**
```typescript
Request:
{
  conversationId: string;
  content: string;
  type: 'text' | 'image' | 'location' | 'document';
  metadata?: object;
}

Response: 201 Created
{
  message: MessageObject;
}

WebSocket: Real-time delivery via Socket.io
```

---

#### Portfolio

**GET /portfolio**
```typescript
Response: 200 OK
{
  summary: {
    totalProperties: number;
    totalValue: number;
    valueChange: {
      amount: number;
      percentage: number;
      period: '6months';
    };
  };
  properties: Array<{
    id: string;
    titleNumber: string;
    location: LocationObject;
    surface: number;
    currentValue: number;
    purchaseValue?: number;
    valueChange?: number;
    taxStatus: 'upToDate' | 'overdue';
    nextTaxDue?: string;
    documents: Array<{
      type: string;
      url: string;
      expiryDate?: string;
    }>;
    surveillance: {
      isActive: boolean;
      lastCheck: string;
      alerts: Array<AlertObject>;
    };
  }>;
  alerts: Array<{
    id: string;
    propertyId: string;
    type: 'tax_due' | 'document_expiry' | 'construction_detected';
    severity: 'low' | 'medium' | 'high';
    message: string;
    actionUrl?: string;
    createdAt: string;
  }>;
}
```

**POST /portfolio/properties/:id/surveillance**
```typescript
Request:
{
  enable: boolean;
}

Response: 200 OK
{
  surveillance: {
    isActive: boolean;
    checkFrequency: 'monthly';
    lastCheck: string;
    nextCheck: string;
  };
}
```

---

#### Market Data

**GET /market/prices**
```typescript
Query:
{
  city: string;
  district?: string;
  type?: string;
  period?: '1month' | '3months' | '6months' | '1year';
}

Response: 200 OK
{
  location: string;
  period: string;
  statistics: {
    avgPricePerSqm: number;
    medianPricePerSqm: number;
    minPrice: number;
    maxPrice: number;
    totalTransactions: number;
  };
  trend: {
    direction: 'up' | 'down' | 'stable';
    changePercentage: number;
  };
  priceHistory: Array<{
    month: string;
    avgPrice: number;
  }>;
  heatmap: Array<{
    district: string;
    avgPricePerSqm: number;
    color: string;  // Hex color for visualization
  }>;
}

Cache: 1 day
```

**POST /market/estimate**
```typescript
Request:
{
  location: { lat: number, lng: number };
  surface: number;
  type: string;
  features?: object;
}

Response: 200 OK
{
  estimatedValue: {
    min: number;
    avg: number;
    max: number;
    confidence: number;  // 0-100
  };
  comparables: Array<{
    propertyId: string;
    price: number;
    surface: number;
    distance: number;  // meters
  }>;
  marketPosition: 'below' | 'average' | 'above';
}
```

---

### 5.3 Base de Données (PostgreSQL Schema)

```sql
-- Users Table
CREATE TABLE users (
  id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
  phone_number VARCHAR(15) UNIQUE NOT NULL,
  email VARCHAR(255) UNIQUE,
  password_hash VARCHAR(255) NOT NULL,
  first_name VARCHAR(100) NOT NULL,
  last_name VARCHAR(100) NOT NULL,
  user_type VARCHAR(20) NOT NULL CHECK (user_type IN ('buyer', 'seller', 'owner', 'notary')),
  avatar_url TEXT,
  is_verified BOOLEAN DEFAULT FALSE,
  is_active BOOLEAN DEFAULT TRUE,
  rating DECIMAL(2,1) DEFAULT 0.0,
  total_transactions INTEGER DEFAULT 0,
  created_at TIMESTAMP DEFAULT NOW(),
  updated_at TIMESTAMP DEFAULT NOW(),
  last_login_at TIMESTAMP
);

CREATE INDEX idx_users_phone ON users(phone_number);
CREATE INDEX idx_users_email ON users(email);

-- Properties Table
CREATE TABLE properties (
  id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
  seller_id UUID REFERENCES users(id) ON DELETE CASCADE,
  title_number VARCHAR(50) UNIQUE NOT NULL,
  title VARCHAR(255) NOT NULL,
  description TEXT,
  price DECIMAL(15,2) NOT NULL,
  price_per_sqm DECIMAL(10,2),
  surface DECIMAL(10,2) NOT NULL,
  property_type VARCHAR(20) NOT NULL CHECK (property_type IN ('residential', 'commercial', 'agricultural')),
  
  -- Location
  address TEXT NOT NULL,
  district VARCHAR(100),
  city VARCHAR(100) NOT NULL,
  latitude DECIMAL(10,8) NOT NULL,
  longitude DECIMAL(11,8) NOT NULL,
  
  -- Features
  has_water BOOLEAN DEFAULT FALSE,
  has_electricity BOOLEAN DEFAULT FALSE,
  is_paved BOOLEAN DEFAULT FALSE,
  
  -- Verification
  is_verified BOOLEAN DEFAULT FALSE,
  trust_score INTEGER CHECK (trust_score BETWEEN 0 AND 100),
  verification_date TIMESTAMP,
  
  -- Status
  status VARCHAR(20) DEFAULT 'pending' CHECK (status IN ('pending', 'active', 'sold', 'expired', 'rejected')),
  is_boosted BOOLEAN DEFAULT FALSE,
  boost_expires_at TIMESTAMP,
  
  -- Stats
  view_count INTEGER DEFAULT 0,
  favorite_count INTEGER DEFAULT 0,
  contact_count INTEGER DEFAULT 0,
  
  created_at TIMESTAMP DEFAULT NOW(),
  updated_at TIMESTAMP DEFAULT NOW(),
  expires_at TIMESTAMP,
  sold_at TIMESTAMP
);

CREATE INDEX idx_properties_location ON properties USING GIST (
  ll_to_earth(latitude, longitude)
);
CREATE INDEX idx_properties_price ON properties(price);
CREATE INDEX idx_properties_city ON properties(city);
CREATE INDEX idx_properties_status ON properties(status);

-- Property Images
CREATE TABLE property_images (
  id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
  property_id UUID REFERENCES properties(id) ON DELETE CASCADE,
  url TEXT NOT NULL,
  thumbnail_url TEXT NOT NULL,
  display_order INTEGER NOT NULL,
  created_at TIMESTAMP DEFAULT NOW()
);

CREATE INDEX idx_images_property ON property_images(property_id);

-- Property Documents
CREATE TABLE property_documents (
  id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
  property_id UUID REFERENCES properties(id) ON DELETE CASCADE,
  document_type VARCHAR(50) NOT NULL CHECK (document_type IN ('title_deed', 'owner_id', 'tax_receipt', 'survey_plan', 'other')),
  file_url TEXT NOT NULL,
  file_name VARCHAR(255),
  upload_date TIMESTAMP DEFAULT NOW(),
  expiry_date DATE,
  is_verified BOOLEAN DEFAULT FALSE
);

-- Verification History
CREATE TABLE verification_logs (
  id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
  user_id UUID REFERENCES users(id),
  title_number VARCHAR(50),
  scan_type VARCHAR(20) CHECK (scan_type IN ('qr', 'ocr', 'manual')),
  result_status VARCHAR(20) CHECK (result_status IN ('authentic', 'suspicious', 'fraudulent', 'not_found')),
  confidence_score INTEGER,
  document_url TEXT,
  ip_address INET,
  created_at TIMESTAMP DEFAULT NOW()
);

CREATE INDEX idx_verification_user ON verification_logs(user_id);
CREATE INDEX idx_verification_date ON verification_logs(created_at);

-- Property Monitoring
CREATE TABLE property_monitors (
  id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
  user_id UUID REFERENCES users(id) ON DELETE CASCADE,
  title_number VARCHAR(50) NOT NULL,
  alert_types TEXT[] NOT NULL,
  is_active BOOLEAN DEFAULT TRUE,
  last_check TIMESTAMP,
  created_at TIMESTAMP DEFAULT NOW()
);

CREATE INDEX idx_monitors_user ON property_monitors(user_id);

-- Alerts
CREATE TABLE alerts (
  id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
  user_id UUID REFERENCES users(id) ON DELETE CASCADE,
  property_id UUID REFERENCES properties(id) ON DELETE SET NULL,
  alert_type VARCHAR(50) NOT NULL,
  severity VARCHAR(20) CHECK (severity IN ('low', 'medium', 'high')),
  message TEXT NOT NULL,
  action_url TEXT,
  is_read BOOLEAN DEFAULT FALSE,
  created_at TIMESTAMP DEFAULT NOW()
);

CREATE INDEX idx_alerts_user ON alerts(user_id, is_read);

-- Conversations
CREATE TABLE conversations (
  id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
  property_id UUID REFERENCES properties(id) ON DELETE CASCADE,
  buyer_id UUID REFERENCES users(id) ON DELETE CASCADE,
  seller_id UUID REFERENCES users(id) ON DELETE CASCADE,
  status VARCHAR(20) DEFAULT 'active' CHECK (status IN ('active', 'archived', 'blocked')),
  created_at TIMESTAMP DEFAULT NOW(),
  updated_at TIMESTAMP DEFAULT NOW(),
  UNIQUE(property_id, buyer_id, seller_id)
);

CREATE INDEX idx_conversations_buyer ON conversations(buyer_id);
CREATE INDEX idx_conversations_seller ON conversations(seller_id);

-- Messages
CREATE TABLE messages (
  id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
  conversation_id UUID REFERENCES conversations(id) ON DELETE CASCADE,
  sender_id UUID REFERENCES users(id) ON DELETE CASCADE,
  content TEXT NOT NULL,
  message_type VARCHAR(20) DEFAULT 'text' CHECK (message_type IN ('text', 'image', 'location', 'document', 'offer')),
  metadata JSONB,
  status VARCHAR(20) DEFAULT 'sent' CHECK (status IN ('sent', 'delivered', 'read')),
  created_at TIMESTAMP DEFAULT NOW()
);

CREATE INDEX idx_messages_conversation ON messages(conversation_id, created_at DESC);

-- Favorites
CREATE TABLE favorites (
  id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
  user_id UUID REFERENCES users(id) ON DELETE CASCADE,
  property_id UUID REFERENCES properties(id) ON DELETE CASCADE,
  created_at TIMESTAMP DEFAULT NOW(),
  UNIQUE(user_id, property_id)
);

-- Transactions (Escrow)
CREATE TABLE transactions (
  id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
  property_id UUID REFERENCES properties(id),
  buyer_id UUID REFERENCES users(id),
  seller_id UUID REFERENCES users(id),
  notary_id UUID REFERENCES users(id),
  amount DECIMAL(15,2) NOT NULL,
  commission DECIMAL(15,2),
  status VARCHAR(20) DEFAULT 'pending' CHECK (status IN ('pending', 'escrowed', 'completed', 'cancelled', 'disputed')),
  escrow_date TIMESTAMP,
  completion_date TIMESTAMP,
  created_at TIMESTAMP DEFAULT NOW()
);

-- Market Data (Aggregated)
CREATE TABLE market_prices (
  id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
  city VARCHAR(100) NOT NULL,
  district VARCHAR(100),
  property_type VARCHAR(20),
  month DATE NOT NULL,
  avg_price_per_sqm DECIMAL(10,2),
  median_price_per_sqm DECIMAL(10,2),
  min_price DECIMAL(15,2),
  max_price DECIMAL(15,2),
  transaction_count INTEGER,
  created_at TIMESTAMP DEFAULT NOW(),
  UNIQUE(city, district, property_type, month)
);

CREATE INDEX idx_market_location_month ON market_prices(city, district, month);
```

---

### 5.4 Validation Rules (Zod Schemas)

```typescript
import { z } from 'zod';

// User Registration
export const registerSchema = z.object({
  phoneNumber: z.string()
    .regex(/^\+229[0-9]{8}$/, 'Format: +229XXXXXXXX'),
  password: z.string()
    .min(8, 'Minimum 8 caractères')
    .regex(/[A-Z]/, 'Au moins une majuscule')
    .regex(/[0-9]/, 'Au moins un chiffre'),
  firstName: z.string().min(2).max(100),
  lastName: z.string().min(2).max(100),
  userType: z.enum(['buyer', 'seller', 'owner']),
});

// Property Creation
export const propertySchema = z.object({
  titleNumber: z.string().regex(/^TF-\d{4}-\d{7}$/),
  title: z.string().min(10).max(255),
  description: z.string().min(50).max(2000),
  price: z.number().positive().max(1000000000), // 1 milliard max
  surface: z.number().positive().min(50).max(100000),
  propertyType: z.enum(['residential', 'commercial', 'agricultural']),
  location: z.object({
    address: z.string().min(10),
    city: z.string(),
    coordinates: z.object({
      lat: z.number().min(6).max(13), // Bénin bounds
      lng: z.number().min(0).max(4),
    }),
  }),
  features: z.object({
    hasWater: z.boolean(),
    hasElectricity: z.boolean(),
    isPaved: z.boolean(),
  }),
});

// Verification Request
export const verificationSchema = z.object({
  scanType: z.enum(['qr', 'ocr', 'manual']),
  titleNumber: z.string().optional(),
  documentImage: z.instanceof(File)
    .refine((file) => file.size <= 5 * 1024 * 1024, 'Max 5MB')
    .refine(
      (file) => ['image/jpeg', 'image/png', 'application/pdf'].includes(file.type),
      'Format: JPG, PNG ou PDF'
    )
    .optional(),
});

// Message
export const messageSchema = z.object({
  conversationId: z.string().uuid(),
  content: z.string().min(1).max(1000),
  type: z.enum(['text', 'image', 'location', 'document']),
  metadata: z.record(z.any()).optional(),
});
```

---

## PHASE 6 : TESTS & VALIDATION

### 6.1 Tests Utilisateurs (Plan)

#### Session 1 : Test du Flow de Vérification
**Participants :** 5 utilisateurs (mix acheteurs/vendeurs)
**Durée :** 30 min/participant
**Objectifs :**
- Temps moyen pour scanner un titre
- Taux de réussite OCR
- Compréhension du résultat

**Scénario :**
```
1. Donnez-leur un faux titre foncier imprimé
2. "Vérifiez si ce titre est authentique"
3. Observer :
   - Choisissent-ils QR, Photo ou Manuel ?
   - Comprennent-ils comment cadrer le document ?
   - Réagissent-ils correctement au résultat ?
4. Questions post-test :
   - "Faites-vous confiance à ce résultat ?"
   - "Que feriez-vous ensuite ?"
```

**Métriques Clés :**
- Task Success Rate (TSR) : >85%
- Time on Task : <30 secondes
- System Usability Scale (SUS) : >75

---

#### Session 2 : Test du Marketplace
**Participants :** 8 acheteurs potentiels
**Durée :** 45 min
**Objectifs :**
- Facilité de recherche
- Pertinence des résultats
- Intention d'achat

**Scénario :**
```
"Vous cherchez un terrain résidentiel de 500m² 
à Cotonou, budget 8 millions FCFA max"

Tasks:
1. Trouvez 3 options qui correspondent
2. Comparez-les
3. Contactez le vendeur de votre choix
```

**Mesures :**
- Temps pour trouver 3 options : <3 min
- Utilisation des filtres : >70%
- Taux d'abandon : <20%

---

### 6.2 Tests A/B à Prévoir

**Test 1 : CTA Principal Page d'Accueil**
- **Variant A :** "Vérifier un titre" (actuel)
- **Variant B :** "Scanner un document foncier"
- **Métrique :** Taux de clic

**Test 2 : Affichage du Prix**
- **Variant A :** Prix total uniquement
- **Variant B :** Prix total + Prix/m² en évidence
- **Métrique :** Taux de contact vendeur

**Test 3 : Onboarding**
- **Variant A :** 3 écrans explicatifs
- **Variant B :** 1 écran + tutoriel interactif
- **Métrique :** Taux de complétion + rétention J+7

**Test 4 : Score de Confiance**
- **Variant A :** Jauge circulaire colorée (actuel)
- **Variant B :** Note sur 5 étoiles + détails textuels
- **Métrique :** Compréhension + confiance perçue

**Test 5 : Formulaire de Publication**
- **Variant A :** Formulaire long (1 page)
- **Variant B :** Multi-étapes avec progress bar
- **Métrique :** Taux de complétion

---

### 6.3 Tests Techniques (QA)

#### Tests Fonctionnels

**Feature : Vérification de Titre**
```gherkin
Scenario: Vérifier un titre authentique via QR Code
  Given l'utilisateur est sur la page d'accueil
  When il clique sur "Vérifier un titre"
  And il sélectionne "Scanner QR Code"
  And il scanne un QR Code valide
  Then le système affiche "Titre Vérifié" en vert
  And les détails du propriétaire sont affichés
  And l'historique des transferts est visible
  And un bouton "Télécharger PDF" est présent

Scenario: Vérifier un titre frauduleux
  Given l'utilisateur scanne un titre invalide
  Then le système affiche "Titre Frauduleux" en rouge
  And un message d'avertissement est affiché
  And un bouton "Signaler la fraude" est présent
  And aucun détail de propriété n'est visible

Scenario: Limite gratuite atteinte
  Given l'utilisateur a fait 3 vérifications ce mois
  When il tente une 4ème vérification
  Then un paywall apparaît
  And les options premium sont affichées
  And un CTA "Passer à Premium" est présent
```

**Feature : Marketplace Search**
```gherkin
Scenario: Recherche avec filtres multiples
  Given l'utilisateur est sur le Marketplace
  When il sélectionne "Cotonou" comme ville
  And il définit un budget de 0-10M FCFA
  And il coche "Avec titre foncier uniquement"
  Then seules les propriétés correspondantes s'affichent
  And le nombre de résultats est affiché
  And les filtres actifs sont visibles en chips

Scenario: Recherche sans résultat
  Given l'utilisateur applique des filtres restrictifs
  When aucune propriété ne correspond
  Then un message "Aucun résultat trouvé" s'affiche
  And des suggestions de recherche alternatives sont proposées
  And un bouton "Effacer les filtres" est présent
```

**Feature : Publication d'Annonce**
```gherkin
Scenario: Publication réussie avec titre vérifié
  Given l'utilisateur a uploadé un titre valide
  And il a rempli tous les champs obligatoires
  And il a ajouté minimum 3 photos
  When il clique sur "Publier"
  Then l'annonce passe en statut "En modération"
  And il reçoit un email de confirmation
  And un délai de 24h est indiqué

Scenario: Rejet pour titre invalide
  Given l'utilisateur upload un titre frauduleux
  When le système le détecte
  Then la publication est bloquée
  And un message d'erreur explicatif s'affiche
  And une option "Contacter le support" est proposée
```

---

#### Tests de Performance

**Benchmarks Cibles**

| Métrique | Cible | Critique |
|----------|-------|----------|
| Temps de chargement initial | <2s | <3s |
| Temps de scan QR | <1s | <2s |
| API response time (P95) | <500ms | <1s |
| Time to Interactive (TTI) | <3s | <5s |
| First Contentful Paint (FCP) | <1.5s | <2.5s |
| Largest Contentful Paint (LCP) | <2.5s | <4s |

**Scénarios de Charge**

```javascript
// Load Test Configuration (k6)
export const options = {
  stages: [
    { duration: '2m', target: 100 },   // Ramp up
    { duration: '5m', target: 100 },   // Steady state
    { duration: '2m', target: 200 },   // Peak
    { duration: '5m', target: 200 },   // Peak steady
    { duration: '2m', target: 0 },     // Ramp down
  ],
  thresholds: {
    http_req_duration: ['p(95)<500'],  // 95% requêtes <500ms
    http_req_failed: ['rate<0.01'],    // <1% d'erreurs
  },
};

// Test scenarios
export default function() {
  // Scenario 1: Homepage
  http.get('https://api.ilot-foncier.bj/properties');
  sleep(1);
  
  // Scenario 2: Search
  http.get('https://api.ilot-foncier.bj/properties?city=Cotonou&maxPrice=10000000');
  sleep(2);
  
  // Scenario 3: Property detail
  http.get('https://api.ilot-foncier.bj/properties/123');
  sleep(3);
  
  // Scenario 4: Verification
  http.post('https://api.ilot-foncier.bj/verification/scan', {
    file: open('sample-title.jpg', 'b'),
  });
  sleep(5);
}
```

**Tests Mobile Spécifiques**
```javascript
// React Native Performance Tests
describe('Performance', () => {
  it('should render property list in <500ms', async () => {
    const start = Date.now();
    render(<PropertyList properties={mockData} />);
    const duration = Date.now() - start;
    expect(duration).toBeLessThan(500);
  });

  it('should maintain 60fps during scroll', async () => {
    const { getByTestId } = render(<PropertyList />);
    const flatList = getByTestId('property-flatlist');
    
    // Simulate fast scroll
    fireEvent.scroll(flatList, { 
      nativeEvent: { contentOffset: { y: 3000 } } 
    });
    
    // Check frame drops
    const metrics = await getFrameMetrics();
    expect(metrics.droppedFrames).toBeLessThan(5);
  });
});
```

---

#### Tests de Sécurité

**Checklist de Sécurité**

1. **Authentication**
   - ✓ Tokens JWT avec expiration courte (1h)
   - ✓ Refresh tokens sécurisés (httpOnly cookies)
   - ✓ Rate limiting sur /auth/login (5 tentatives/5min)
   - ✓ OTP avec expiration (5 minutes)
   - ✓ Passwords hashed (bcrypt, 12 rounds)

2. **Authorization**
   - ✓ RBAC (Role-Based Access Control)
   - ✓ Validation côté serveur de tous les inputs
   - ✓ Propriété ownership check avant modification
   - ✓ API keys pour intégrations tierces

3. **Data Protection**
   - ✓ HTTPS obligatoire (TLS 1.3)
   - ✓ Encryption at rest (AES-256)
   - ✓ PII (Personally Identifiable Information) masquée dans logs
   - ✓ GDPR compliance (droit à l'oubli)
   - ✓ Backup quotidiens chiffrés

4. **Input Validation**
   - ✓ SQL Injection protection (parameterized queries)
   - ✓ XSS protection (sanitize HTML)
   - ✓ File upload validation (type, size, malware scan)
   - ✓ CSRF tokens

5. **API Security**
   - ✓ Rate limiting (100 req/min/user)
   - ✓ CORS configuré strictement
   - ✓ API versioning
   - ✓ Error messages non verbeux (pas de stack traces)

**Penetration Testing Checklist**
```bash
# OWASP ZAP Scan
zap-cli quick-scan --self-contained \
  --start-options '-config api.key=YOUR_KEY' \
  https://api.ilot-foncier.bj

# SQL Injection Test
sqlmap -u "https://api.ilot-foncier.bj/properties?id=1" \
  --batch --random-agent

# XSS Test
xsser --url "https://ilot-foncier.bj/search?q=TEST" \
  --auto

# SSL/TLS Check
testssl.sh --full https://ilot-foncier.bj
```

---

### 6.4 Tests d'Accessibilité

**WCAG 2.1 Level AA Compliance**

**Checklist Prioritaire**

1. **Contraste des Couleurs**
   - Ratio minimum 4.5:1 pour texte normal
   - Ratio minimum 3:1 pour texte large (>18pt)
   - Outil : WebAIM Contrast Checker

2. **Navigation au Clavier**
   - Tab order logique
   - Focus visible sur tous les éléments interactifs
   - Skip to main content link
   - Raccourcis clavier documentés

3. **Screen Readers**
   - Alt text pour toutes les images
   - ARIA labels pour icônes
   - Landmarks HTML5 (nav, main, aside)
   - Live regions pour notifications

4. **Formulaires**
   - Labels associés à tous les inputs
   - Messages d'erreur descriptifs
   - Instructions claires
   - Autocomplete attributes

5. **Responsive & Zoom**
   - Fonctionne à 200% de zoom
   - Pas de scroll horizontal
   - Touch targets ≥44x44px

**Tests Automatisés**
```javascript
// Axe-core integration
import { axe, toHaveNoViolations } from 'jest-axe';
expect.extend(toHaveNoViolations);

describe('Accessibility', () => {
  it('HomePage should have no violations', async () => {
    const { container } = render(<HomePage />);
    const results = await axe(container);
    expect(results).toHaveNoViolations();
  });

  it('Form should be keyboard navigable', () => {
    const { getByLabelText, getByRole } = render(<PublishForm />);
    
    // Tab through form
    const titleInput = getByLabelText('Titre de l\'annonce');
    userEvent.tab();
    expect(titleInput).toHaveFocus();
    
    userEvent.tab();
    expect(getByLabelText('Prix')).toHaveFocus();
  });
});
```

**Tests Manuels**
- VoiceOver (iOS) : Navigation fluide, tous les éléments annoncés
- TalkBack (Android) : Idem
- NVDA (Windows) : Idem
- Navigation clavier uniquement : Toutes les fonctions accessibles

---

## PHASE 7 : DESIGN SYSTEM & DOCUMENTATION

### 7.1 Design Tokens

**Colors**
```javascript
// colors.ts
export const colors = {
  // Brand
  primary: {
    50: '#E6F4FF',
    100: '#BAE0FF',
    200: '#91CAFF',
    300: '#69B1FF',
    400: '#4096FF',
    500: '#1677FF',  // Main
    600: '#0958D9',
    700: '#003EB3',
    800: '#002C8C',
    900: '#001D66',
  },
  
  // Semantic
  success: {
    light: '#95DE64',
    main: '#52C41A',
    dark: '#389E0D',
  },
  warning: {
    light: '#FFC53D',
    main: '#FAAD14',
    dark: '#D48806',
  },
  error: {
    light: '#FF7875',
    main: '#FF4D4F',
    dark: '#CF1322',
  },
  
  // Neutrals
  gray: {
    50: '#FAFAFA',
    100: '#F5F5F5',
    200: '#E8E8E8',
    300: '#D9D9D9',
    400: '#BFBFBF',
    500: '#8C8C8C',
    600: '#595959',
    700: '#434343',
    800: '#262626',
    900: '#1F1F1F',
  },
  
  // Trust Score Colors
  trustScore: {
    excellent: '#52C41A',  // 80-100
    good: '#73D13D',       // 60-79
    average: '#FAAD14',    // 40-59
    poor: '#FF7A45',       // 20-39
    veryPoor: '#FF4D4F',   // 0-19
  },
};

// Tailwind config extension
module.exports = {
  theme: {
    extend: {
      colors: {
        brand: colors.primary,
        // ... autres
      },
    },
  },
};
```

**Typography**
```javascript
export const typography = {
  fontFamily: {
    sans: ['Inter', 'system-ui', 'sans-serif'],
    mono: ['Fira Code', 'monospace'],
  },
  
  fontSize: {
    xs: ['0.75rem', { lineHeight: '1rem' }],      // 12px
    sm: ['0.875rem', { lineHeight: '1.25rem' }],  // 14px
    base: ['1rem', { lineHeight: '1.5rem' }],     // 16px
    lg: ['1.125rem', { lineHeight: '1.75rem' }],  // 18px
    xl: ['1.25rem', { lineHeight: '1.75rem' }],   // 20px
    '2xl': ['1.5rem', { lineHeight: '2rem' }],    // 24px
    '3xl': ['1.875rem', { lineHeight: '2.25rem' }], // 30px
    '4xl': ['2.25rem', { lineHeight: '2.5rem' }], // 36px
  },
  
  fontWeight: {
    normal: 400,
    medium: 500,
    semibold: 600,
    bold: 700,
  },
};
```

**Spacing**
```javascript
export const spacing = {
  0: '0',
  1: '0.25rem',   // 4px
  2: '0.5rem',    // 8px
  3: '0.75rem',   // 12px
  4: '1rem',      // 16px
  5: '1.25rem',   // 20px
  6: '1.5rem',    // 24px
  8: '2rem',      // 32px
  10: '2.5rem',   // 40px
  12: '3rem',     // 48px
  16: '4rem',     // 64px
  20: '5rem',     // 80px
};
```

**Shadows**
```javascript
export const shadows = {
  sm: '0 1px 2px 0 rgba(0, 0, 0, 0.05)',
  base: '0 1px 3px 0 rgba(0, 0, 0, 0.1), 0 1px 2px 0 rgba(0, 0, 0, 0.06)',
  md: '0 4px 6px -1px rgba(0, 0, 0, 0.1), 0 2px 4px -1px rgba(0, 0, 0, 0.06)',
  lg: '0 10px 15px -3px rgba(0, 0, 0, 0.1), 0 4px 6px -2px rgba(0, 0, 0, 0.05)',
  xl: '0 20px 25px -5px rgba(0, 0, 0, 0.1), 0 10px 10px -5px rgba(0, 0, 0, 0.04)',
};
```

**Border Radius**
```javascript
export const borderRadius = {
  none: '0',
  sm: '0.25rem',   // 4px
  base: '0.5rem',  // 8px
  md: '0.75rem',   // 12px
  lg: '1rem',      // 16px
  xl: '1.5rem',    // 24px
  full: '9999px',
};
```

---

### 7.2 Component Library (Exemples)

**Button Component**
```typescript
// Button.tsx
import React from 'react';
import { TouchableOpacity, Text, ActivityIndicator, StyleSheet } from 'react-native';

interface ButtonProps {
  title: string;
  onPress: () => void;
  variant?: 'primary' | 'secondary' | 'outline' | 'ghost';
  size?: 'sm' | 'md' | 'lg';
  isLoading?: boolean;
  disabled?: boolean;
  fullWidth?: boolean;
  icon?: React.ReactNode;
}

export const Button: React.FC<ButtonProps> = ({
  title,
  onPress,
  variant = 'primary',
  size = 'md',
  isLoading = false,
  disabled = false,
  fullWidth = false,
  icon,
}) => {
  return (
    <TouchableOpacity
      style={[
        styles.base,
        styles[variant],
        styles[size],
        fullWidth && styles.fullWidth,
        disabled && styles.disabled,
      ]}
      onPress={onPress}
      disabled={disabled || isLoading}
      activeOpacity={0.7}
    >
      {isLoading ? (
        <ActivityIndicator color={variant === 'primary' ? '#FFF' : '#1677FF'} />
      ) : (
        <>
          {icon && <View style={styles.icon}>{icon}</View>}
          <Text style={[styles.text, styles[`${variant}Text`]]}>{title}</Text>
        </>
      )}
    </TouchableOpacity>
  );
};

const styles = StyleSheet.create({
  base: {
    flexDirection: 'row',
    alignItems: 'center',
    justifyContent: 'center',
    borderRadius: 8,
    paddingHorizontal: 16,
    paddingVertical: 12,
  },
  primary: {
    backgroundColor: '#1677FF',
  },
  secondary: {
    backgroundColor: '#F5F5F5',
  },
  outline: {
    backgroundColor: 'transparent',
    borderWidth: 1,
    borderColor: '#D9D9D9',
  },
  ghost: {
    backgroundColor: 'transparent',
  },
  sm: {
    paddingHorizontal: 12,
    paddingVertical: 8,
  },
  md: {
    paddingHorizontal: 16,
    paddingVertical: 12,
  },
  lg: {
    paddingHorizontal: 24,
    paddingVertical: 16,
  },
  fullWidth: {
    width: '100%',
  },
  disabled: {
    opacity: 0.5,
  },
  text: {
    fontSize: 16,
    fontWeight: '600',
  },
  primaryText: {
    color: '#FFF',
  },
  secondaryText: {
    color: '#262626',
  },
  outlineText: {
    color: '#262626',
  },
  ghostText: {
    color: '#1677FF',
  },
  icon: {
    marginRight: 8,
  },
});
```

**Badge Component (Trust Score)**
```typescript
// TrustScoreBadge.tsx
import React from 'react';
import { View, Text, StyleSheet } from 'react-native';
import { colors } from '../theme/colors';

interface TrustScoreBadgeProps {
  score: number; // 0-100
  showLabel?: boolean;
}

export const TrustScoreBadge: React.FC<TrustScoreBadgeProps> = ({ 
  score, 
  showLabel = true 
}) => {
  const getScoreConfig = (score: number) => {
    if (score >= 80) return { color: colors.trustScore.excellent, label: 'Excellent' };
    if (score >= 60) return { color: colors.trustScore.good, label: 'Bon' };
    if (score >= 40) return { color: colors.trustScore.average, label: 'Moyen' };
    if (score >= 20) return { color: colors.trustScore.poor, label: 'Faible' };
    return { color: colors.trustScore.veryPoor, label: 'Très faible' };
  };

  const config = getScoreConfig(score);

  return (
    <View style={styles.container}>
      <View style={[styles.gauge, { backgroundColor: config.color }]}>
        <Text style={styles.score}>{score}</Text>
      </View>
      {showLabel && <Text style={styles.label}>{config.label}</Text>}
    </View>
  );
};

const styles = StyleSheet.create({
  container: {
    alignItems: 'center',
  },
  gauge: {
    width: 60,
    height: 60,
    borderRadius: 30,
    justifyContent: 'center',
    alignItems: 'center',
  },
  score: {
    fontSize: 24,
    fontWeight: 'bold',
    color: '#FFF',
  },
  label: {
    marginTop: 4,
    fontSize: 14,
    color: '#595959',
  },
});
```

**Property Card Component**
```typescript
// PropertyCard.tsx
import React from 'react';
import { View, Image, Text, TouchableOpacity, StyleSheet } from 'react-native';
import { Heart, MapPin } from 'lucide-react-native';
import { TrustScoreBadge } from './TrustScoreBadge';

interface PropertyCardProps {
  property: {
    id: string;
    image: string;
    title: string;
    price: number;
    pricePerSqm: number;
    surface: number;
    location: string;
    distance?: number;
    trustScore: number;
    isFavorite: boolean;
  };
  onPress: () => void;
  onToggleFavorite: () => void;
}

export const PropertyCard: React.FC<PropertyCardProps> = ({
  property,
  onPress,
  onToggleFavorite,
}) => {
  const formatPrice = (price: number) => {
    return `${(price / 1000000).toFixed(1)}M FCFA`;
  };

  return (
    <TouchableOpacity style={styles.card} onPress={onPress} activeOpacity={0.8}>
      <View style={styles.imageContainer}>
        <Image source={{ uri: property.image }} style={styles.image} />
        <TouchableOpacity 
          style={styles.favoriteButton}
          onPress={onToggleFavorite}
        >
          <Heart 
            size={20} 
            color={property.isFavorite ? '#FF4D4F' : '#FFF'}
            fill={property.isFavorite ? '#FF4D4F' : 'transparent'}
          />
        </TouchableOpacity>
        <View style={styles.badge}>
          <TrustScoreBadge score={property.trustScore} showLabel={false} />
        </View>
      </View>

      <View style={styles.content}>
        <Text style={styles.title} numberOfLines={1}>
          {property.surface}m² - {property.title}
        </Text>

        <View style={styles.locationRow}>
          <MapPin size={14} color="#8C8C8C" />
          <Text style={styles.location}>{property.location}</Text>
          {property.distance && (
            <Text style={styles.distance}> • {property.distance} km</Text>
          )}
        </View>

        <View style={styles.priceRow}>
          <Text style={styles.price}>{formatPrice(property.price)}</Text>
          <Text style={styles.pricePerSqm}>
            {property.pricePerSqm.toLocaleString()} F/m²
          </Text>
        </View>
      </View>
    </TouchableOpacity>
  );
};

const styles = StyleSheet.create({
  card: {
    backgroundColor: '#FFF',
    borderRadius: 12,
    marginBottom: 16,
    shadowColor: '#000',
    shadowOffset: { width: 0, height: 2 },
    shadowOpacity: 0.1,
    shadowRadius: 4,
    elevation: 3,
  },
  imageContainer: {
    position: 'relative',
    height: 200,
  },
  image: {
    width: '100%',
    height: '100%',
    borderTopLeftRadius: 12,
    borderTopRightRadius: 12,
  },
  favoriteButton: {
    position: 'absolute',
    top: 12,
    right: 12,
    backgroundColor: 'rgba(0,0,0,0.3)',
    padding: 8,
    borderRadius: 20,
  },
  badge: {
    position: 'absolute',
    top: 12,
    left: 12,
  },
  content: {
    padding: 12,
  },
  title: {
    fontSize: 16,
    fontWeight: '600',
    color: '#262626',
    marginBottom: 4,
  },
  locationRow: {
    flexDirection: 'row',
    alignItems: 'center',
    marginBottom: 8,
  },
  location: {
    fontSize: 14,
    color: '#8C8C8C',
    marginLeft: 4,
  },
  distance: {
    fontSize: 14,
    color: '#8C8C8C',
  },
  priceRow: {
    flexDirection: 'row',
    justifyContent: 'space-between',
    alignItems: 'center',
  },
  price: {
    fontSize: 18,
    fontWeight: 'bold',
    color: '#1677FF',
  },
  pricePerSqm: {
    fontSize: 14,
    color: '#595959',
  },
});
```

---

### 7.3 Documentation Développeur

**Structure de Documentation**

```
docs/
├── README.md
├── GETTING_STARTED.md
├── ARCHITECTURE.md
├── API_REFERENCE.md
├── COMPONENTS.md
├── DEPLOYMENT.md
└── CONTRIBUTING.md
```

**Exemple: API_REFERENCE.md**

```markdown
# API Reference - iLôt Foncier

## Base URL
```
https://api.ilot-foncier.bj/v1
```

## Authentication

All authenticated endpoints require a Bearer token in the Authorization header:

```bash
Authorization: Bearer <access_token>
```

### Obtain Access Token

```http
POST /auth/login
Content-Type: application/json

{
  "phoneNumber": "+229XXXXXXXX",
  "password": "YourPassword123"
}
```

**Response:**
```json
{
  "user": {
    "id": "uuid",
    "firstName": "Jean",
    "lastName": "DOSSOU"
  },
  "tokens": {
    "accessToken": "eyJhbGc...",
    "refreshToken": "eyJhbGc..."
  }
}
```

---

## Endpoints

### Verification

#### Scan Document

```http
POST /verification/scan
Authorization: Bearer <token>
Content-Type: multipart/form-data

documentImage: <file>
scanType: "qr" | "ocr" | "manual"
titleNumber: "TF-2024-0012345" (optional)
```

**Response:**
```json
{
  "status": "authentic",
  "confidence": 92,
  "property": {
    "titleNumber": "TF-2024-0012345",
    "owner": "Jean DOSSOU",
    "location": {...},
    "surface": 500,
    "transferHistory": [...]
  },
  "warnings": [],
  "reportUrl": "https://..."
}
```

**Rate Limits:**
- Free tier: 3 requests/month
- Premium: Unlimited

**Errors:**
- `400` Invalid document format
- `404` Title not found
- `429` Rate limit exceeded

---

### Properties

#### List Properties

```http
GET /properties?city=Cotonou&minPrice=0&maxPrice=10000000&page=1&limit=20
```

**Query Parameters:**

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| city | string | No | Filter by city |
| minPrice | number | No | Minimum price in FCFA |
| maxPrice | number | No | Maximum price in FCFA |
| minSurface | number | No | Minimum surface in m² |
| hasTitle | boolean | No | Only verified titles |
| page | number | No | Page number (default: 1) |
| limit | number | No | Items per page (default: 20, max: 100) |

**Response:**
```json
{
  "properties": [...],
  "pagination": {
    "currentPage": 1,
    "totalPages": 5,
    "totalItems": 94
  }
}
```

---

## Error Handling

All errors follow this format:

```json
{
  "error": {
    "code": "VALIDATION_ERROR",
    "message": "Invalid phone number format",
    "details": {
      "field": "phoneNumber",
      "expected": "+229XXXXXXXX"
    }
  }
}
```

**Common Error Codes:**
- `AUTH_REQUIRED` (401)
- `FORBIDDEN` (403)
- `NOT_FOUND` (404)
- `VALIDATION_ERROR` (422)
- `RATE_LIMIT_EXCEEDED` (429)
- `SERVER_ERROR` (500)
```

---

## RÉCAPITULATIF FINAL

### Livrables du Projet UX/UI

✅ **Phase 1 - Complétée**
- 4 Personas détaillés
- 10 Use Cases prioritaires (méthode MoSCoW)
- 24 User Stories

✅ **Phase 2 - Complétée**
- 3 User Flows détaillés (Vérification, Publication, Marketplace)
- Points de friction identifiés + solutions

✅ **Phase 3 - Complétée**
- 9 Wireframes mobiles détaillés
- Annotations UX complètes
- États interactifs documentés

✅ **Phase 4 - Complétée**
- Outils recommandés (Figma)
- 4 Interactions clés prototypées
- Micro-animations définies

✅ **Phase 5 - Complétée**
- Stack technique complet (React Native/React)
- Architecture frontend
- 15+ API endpoints documentés
- Schéma base de données PostgreSQL
- Validation schemas (Zod)

✅ **Phase 6 - Complétée**
- Plan de tests utilisateurs (2 sessions)
- 5 Tests A/B à exécuter
- Tests fonctionnels (Gherkin)
- Tests de performance (k6)
- Checklist sécurité OWASP
- Tests d'accessibilité WCAG 2.1

✅ **Phase 7 - Complétée**
- Design System (tokens, couleurs, typographie)
- 3 Composants React Native exemplaires
- Documentation API complète

---

## PROCHAINES ÉTAPES RECOMMANDÉES

### Phase 8 : Développement du MVP (8-12 semaines)

#### Sprint 1 : Infrastructure & Auth (2 semaines)
- Setup environnements (Dev/Staging/Prod)
- Configuration CI/CD (GitHub Actions)
- Base de données PostgreSQL + migrations
- API Authentication complète
- App mobile : Navigation + Auth screens

#### Sprint 2 : Vérification de Titres (3 semaines)
- Backend : API /verification/scan
- Intégration OCR (Google Vision API ou Tesseract)
- Intégration e-foncier (si API disponible)
- Mobile : Caméra + Scan QR + Résultats
- Tests unitaires + intégration

#### Sprint 3 : Marketplace (3 semaines)
- Backend : CRUD Properties + Search
- Intégration Google Maps API
- Mobile : Liste, filtres, carte, détail
- Upload images (Cloudinary/AWS S3)
- Tests de performance

#### Sprint 4 : Publication & Messagerie (2 semaines)
- Backend : Publication workflow + modération
- Messagerie en temps réel (Socket.io)
- Mobile : Formulaire multi-étapes
- Chat interface
- Notifications push (Firebase)

#### Sprint 5 : Polish & Testing (2 semaines)
- Tests utilisateurs (5-10 participants)
- Corrections bugs critiques
- Optimisations performances
- Tests de pénétration
- Documentation finale

---

## BUDGET ESTIMÉ

### Équipe Recommandée

| Rôle | Durée | Taux/mois | Total |
|------|-------|-----------|-------|
| Product Owner | 3 mois | 800 000 F | 2 400 000 F |
| Lead Developer (Full-stack) | 3 mois | 1 200 000 F | 3 600 000 F |
| Mobile Developer (React Native) | 3 mois | 1 000 000 F | 3 000 000 F |
| Backend Developer | 2 mois | 900 000 F | 1 800 000 F |
| UI/UX Designer | 1.5 mois | 700 000 F | 1 050 000 F |
| QA Tester | 2 mois | 500 000 F | 1 000 000 F |
| DevOps Engineer | 1 mois | 800 000 F | 800 000 F |

**Total Équipe : 13 650 000 FCFA**

### Infrastructure & Services (Première Année)

| Service | Coût/mois | Coût annuel |
|---------|-----------|-------------|
| AWS/Digital Ocean (Hosting) | 150 000 F | 1 800 000 F |
| Base de données (RDS) | 100 000 F | 1 200 000 F |
| CDN + Stockage (S3/Cloudinary) | 50 000 F | 600 000 F |
| Google Maps API | 80 000 F | 960 000 F |
| Firebase (Push notifications) | 30 000 F | 360 000 F |
| SSL Certificates | 10 000 F | 120 000 F |
| Monitoring (Sentry, DataDog) | 40 000 F | 480 000 F |
| SMS Gateway (OTP) | 60 000 F | 720 000 F |
| Email Service (SendGrid) | 20 000 F | 240 000 F |

**Total Infrastructure : 6 480 000 FCFA**

### Licences & Outils

| Outil | Coût annuel |
|-------|-------------|
| Figma (Professional) | 180 000 F |
| GitHub (Team) | 100 000 F |
| Postman (Team) | 80 000 F |
| Testing Tools (BrowserStack) | 200 000 F |

**Total Licences : 560 000 FCFA**

### Marketing & Légal

| Poste | Coût |
|-------|------|
| Création d'entreprise | 500 000 F |
| Conseil juridique (CGU, Privacy) | 800 000 F |
| Logo & Identité visuelle | 600 000 F |
| Campagne lancement (3 mois) | 3 000 000 F |
| Tests utilisateurs (rémunération) | 500 000 F |

**Total Marketing/Légal : 5 400 000 FCFA**

---

### BUDGET TOTAL MVP

| Catégorie | Montant |
|-----------|---------|
| Équipe de développement | 13 650 000 F |
| Infrastructure (1 an) | 6 480 000 F |
| Licences & Outils | 560 000 F |
| Marketing & Légal | 5 400 000 F |
| **Contingence (15%)** | **3 900 000 F** |
| **TOTAL** | **29 990 000 FCFA** |

*≈ 50 000 USD au taux de 600 FCFA/USD*

---

## MODÈLE ÉCONOMIQUE & PROJECTIONS

### Sources de Revenus

#### 1. Freemium Vérification
- **Gratuit :** 3 vérifications/mois
- **Premium :** 2 000 FCFA/mois (vérifications illimitées)
  - Objectif Année 1 : 500 abonnés = 1 000 000 F/mois

#### 2. Annonces Marketplace
- **Standard :** Gratuite (30 jours)
- **Boosted :** 10 000 FCFA (60 jours, top résultats)
  - Objectif Année 1 : 50 boosts/mois = 500 000 F/mois

#### 3. Commission Transactions (Escrow)
- **0.5%** du montant de la transaction
  - Si 10 ventes/mois à 8M FCFA moyen : 400 000 F/mois

#### 4. Services Partenaires
- **Référencement notaires :** 20 000 F/lead qualifié
  - 30 leads/mois = 600 000 F/mois
- **Partenariat banques :** Commission sur crédits accordés
  - 2% du montant du crédit
  - 5 crédits/mois à 5M moyen = 500 000 F/mois

#### 5. Publicité Ciblée
- **Promoteurs immobiliers, IMF, assurances**
  - Bannières in-app : 200 000 F/mois
  - Articles sponsorisés : 150 000 F/article

### Projections Revenus (Année 1)

| Mois | Abonnés | Boosts | Transactions | Leads | Total/mois |
|------|---------|--------|--------------|-------|------------|
| M1-3 | 50 | 10 | 2 | 5 | 500 000 F |
| M4-6 | 150 | 25 | 5 | 15 | 1 200 000 F |
| M7-9 | 300 | 40 | 8 | 25 | 2 100 000 F |
| M10-12 | 500 | 50 | 10 | 30 | 3 000 000 F |

**Revenus Année 1 : ~20 000 000 FCFA**

### Projections Année 2-3

**Année 2 :** 60 000 000 FCFA (x3)
- 2000 abonnés premium
- Expansion Porto-Novo, Parakou
- Lancement service succession

**Année 3 :** 150 000 000 FCFA (x2.5)
- 5000 abonnés premium
- API pour notaires (licensing)
- Expansion régionale (Togo, Bénin)

---

## RISQUES & MITIGATION

### Risques Techniques

| Risque | Impact | Probabilité | Mitigation |
|--------|--------|-------------|------------|
| API e-foncier indisponible | Élevé | Moyenne | Base de données propriétaire + crowdsourcing |
| Fraude via faux documents | Élevé | Moyenne | ML pour détection + modération humaine |
| Problèmes de scalabilité | Moyen | Faible | Architecture microservices dès le début |
| Attaques de sécurité | Élevé | Moyenne | Pen testing réguliers + bug bounty |

### Risques Business

| Risque | Impact | Probabilité | Mitigation |
|--------|--------|-------------|------------|
| Adoption lente | Élevé | Moyenne | Campagne éducative + freemium généreux |
| Concurrence (e-foncier évolue) | Moyen | Faible | Différenciation par UX + services complémentaires |
| Régulation restrictive | Élevé | Faible | Dialogue proactif avec autorités |
| Coûts infrastructure explosent | Moyen | Moyenne | Monitoring strict + optimisation continue |

### Risques Légaux

| Risque | Impact | Probabilité | Mitigation |
|--------|--------|-------------|------------|
| Protection données (GDPR Bénin) | Élevé | Faible | Conformité dès le design (privacy by design) |
| Responsabilité erreurs vérification | Élevé | Moyenne | Disclaimers clairs + assurance professionnelle |
| Litiges utilisateurs | Moyen | Moyenne | CGU solides + médiation intégrée |

---

## KPIs & MÉTRIQUES DE SUCCÈS

### Acquisition

| Métrique | Cible M3 | Cible M6 | Cible M12 |
|----------|----------|----------|-----------|
| Téléchargements app | 1 000 | 3 000 | 10 000 |
| Inscriptions | 500 | 1 500 | 5 000 |
| Taux de conversion (install → signup) | 40% | 45% | 50% |
| CAC (Coût d'Acquisition Client) | 5 000 F | 4 000 F | 3 000 F |

### Engagement

| Métrique | Cible M3 | Cible M6 | Cible M12 |
|----------|----------|----------|-----------|
| DAU (Daily Active Users) | 100 | 300 | 800 |
| MAU (Monthly Active Users) | 400 | 1 200 | 3 500 |
| Session duration | 5 min | 7 min | 10 min |
| Retention J+7 | 30% | 40% | 50% |
| Retention J+30 | 15% | 20% | 30% |

### Monétisation

| Métrique | Cible M3 | Cible M6 | Cible M12 |
|----------|----------|----------|-----------|
| Abonnés Premium | 20 | 100 | 500 |
| Taux de conversion Premium | 4% | 6% | 10% |
| ARPU (Average Revenue Per User) | 500 F | 800 F | 1 200 F |
| LTV (Lifetime Value) | 10 000 F | 15 000 F | 25 000 F |

### Qualité

| Métrique | Cible | Seuil Alerte |
|----------|-------|--------------|
| App Store Rating | >4.5/5 | <4.0 |
| Crash-free rate | >99% | <98% |
| API uptime | >99.5% | <99% |
| Response time P95 | <500ms | >1s |
| NPS (Net Promoter Score) | >50 | <30 |

---

## ROADMAP POST-MVP (6-18 mois)

### Q1 Post-Launch (M4-6)
- ✨ Chatbot IA juridique (UC-008)
- 🗺️ Surveillance satellite automatique
- 📊 Dashboard analytics pour vendeurs
- 🔔 Système d'alertes avancé
- 🌍 Version web responsive

### Q2 (M7-9)
- 💰 Intégration crédit immobilier (UC-010)
- 🤝 Programme de parrainage
- 📱 App pour notaires (B2B)
- 🎯 Publicité ciblée géolocalisée
- 🌐 Expansion Porto-Novo

### Q3 (M10-12)
- 📜 Testament numérique (UC-009)
- 🏗️ Module suivi de construction
- 💳 Paiement mobile money intégré
- 🔐 Blockchain pour certifications
- 🌍 Lancement Togo/Niger

### Q4 (M13-18)
- 🤖 ML pour détection fraudes avancée
- 📹 Visites virtuelles 360°
- 🏦 Marketplace secondaire (revente)
- 📊 API publique pour développeurs
- 🌍 Levée de fonds Série A

---

## ANNEXES

### A. Glossaire Technique

**OCR (Optical Character Recognition)**
: Technologie d'extraction de texte depuis images

**Escrow**
: Service de séquestre (tiers de confiance) pour transactions sécurisées

**KYC (Know Your Customer)**
: Vérification d'identité des utilisateurs

**WebSocket**
: Protocole pour communication bidirectionnelle temps réel

**JWT (JSON Web Token)**
: Standard pour authentification stateless

**GDPR/RGPD**
: Réglementation protection des données personnelles

### B. Ressources Utiles

**Design**
- [Figma Community - Mobile Design Kits](https://figma.com/community)
- [Material Design Guidelines](https://material.io/design)
- [iOS Human Interface Guidelines](https://developer.apple.com/design)

**Développement**
- [React Native Documentation](https://reactnative.dev)
- [Expo Documentation](https://docs.expo.dev)
- [PostgreSQL Best Practices](https://wiki.postgresql.org/wiki/Don't_Do_This)

**Testing**
- [React Native Testing Library](https://callstack.github.io/react-native-testing-library)
- [K6 Load Testing](https://k6.io/docs)
- [OWASP Testing Guide](https://owasp.org/www-project-web-security-testing-guide)

**Bénin Specific**
- [e-foncier Bénin](https://e-foncier.bj) (si API disponible)
- [ANDF (Agence Nationale du Domaine)](https://andf.bj)
- [Chambre des Notaires du Bénin](https://notaires-benin.org)

### C. Contact & Support

**Questions Techniques**
: dev@ilot-foncier.bj

**Partenariats**
: partnerships@ilot-foncier.bj

**Support Utilisateurs**
: support@ilot-foncier.bj

**Signaler une Fraude**
: fraud@ilot-foncier.bj (24/7)

---

## CONCLUSION

Le projet **iLôt Foncier** représente une opportunité unique de digitaliser et sécuriser le marché foncier béninois. En s'appuyant sur une UX irréprochable, une technologie robuste et un modèle économique viable, la plateforme peut :

✅ **Résoudre un problème structurel pérenne**
- La fraude foncière existera toujours
- Le besoin de transparence est universel
- La demande de terrains ne fera qu'augmenter

✅ **Créer de la valeur pour tous**
- Acheteurs : Sécurité et transparence
- Vendeurs : Visibilité et crédibilité
- État : Formalisation et taxation
- Notaires : Efficacité et volume

✅ **Scaler régionalement**
- Modèle réplicable (Togo, Niger, Burkina)
- Technologie agnostique du contexte
- Network effects puissants

**Le succès repose sur :**
1. **Exécution technique impeccable** (ce document donne la roadmap)
2. **Partenariats stratégiques** (notaires, banques, État)
3. **Campagne éducative forte** (le problème existe mais n'est pas conscient)
4. **Croissance organique** (bouche-à-oreille dans un marché de confiance)

**Next Action Immédiat :**
👉 Valider l'intérêt marché via MVP minimaliste (vérification uniquement) avant investissement complet

---

*Document généré le 10 octobre 2025 par l'équipe iLôt Foncier*
*Version 1.0 - Confidentiel*
