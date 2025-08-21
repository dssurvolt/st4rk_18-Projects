# 📚 Cours Complet : Les Annotations Spring Boot

> Guide complet pour comprendre `@RestController`, `@Service`, et `@Repository`
> 
> *Expliqué de manière simple et progressive - De débutant à expert*

## 📋 Table des Matières

1. [Introduction - Qu'est-ce qu'une annotation ?](#1-introduction---quest-ce-quune-annotation)
2. [Le Principe de Base : Séparer les Responsabilités](#2-le-principe-de-base--séparer-les-responsabilités)
3. [@Repository - La Couche de Données](#3-repository---la-couche-de-données)
4. [@Service - La Logique Métier](#4-service---la-logique-métier)
5. [@RestController - L'Interface Web](#5-restcontroller---linterface-web)
6. [Comment Tout Fonctionne Ensemble](#6-comment-tout-fonctionne-ensemble)
7. [Exemples Concrets et Progressifs](#7-exemples-concrets-et-progressifs)
8. [Bonnes Pratiques et Pièges à Éviter](#8-bonnes-pratiques-et-pièges-à-éviter)
9. [Exercices Pratiques](#9-exercices-pratiques)

---

## 1. Introduction - Qu'est-ce qu'une annotation ?

### 🤔 Imaginez une étiquette sur une boîte

Vous savez ces petites étiquettes qu'on colle sur les boîtes pour savoir ce qu'il y a dedans ? 

```
📦 [ÉTIQUETTE: "Jouets"]  ←  Ça, c'est comme une annotation !
```

En Java, une **annotation** c'est pareil : c'est une **étiquette** qu'on colle sur nos classes pour dire à Spring Boot :

> *"Hey ! Cette classe, c'est pour faire ça !"*

### 💡 Pourquoi on a besoin d'annotations ?

Imaginez que vous dirigez une entreprise avec 100 employés. Comment vous faites pour savoir qui fait quoi ?

```
👨‍💼 [BADGE: "DIRECTEUR"]     ← Il prend les décisions
👨‍🔧 [BADGE: "MÉCANICIEN"]    ← Il répare les machines  
👨‍💻 [BADGE: "PROGRAMMEUR"]   ← Il écrit le code
```

C'est exactement pareil avec Spring Boot ! Les annotations sont les **badges** de nos classes.

### 🎯 Les 3 Grandes Familles d'Annotations

Dans une application, on a besoin de 3 types de "travailleurs" :

1. **@RestController** 🌐 → *"Je parle aux clients"*
2. **@Service** 🔧 → *"Je fais le travail important"*  
3. **@Repository** 🗄️ → *"Je m'occupe des données"*

---

## 2. Le Principe de Base : Séparer les Responsabilités

### 🏠 L'Analogie de la Maison

Imaginez que vous construisez une maison. Vous ne demandez pas au **plombier** de faire l'**électricité**, n'est-ce pas ?

```
🏠 Construction d'une Maison
├── 🔌 Électricien    → S'occupe SEULEMENT de l'électricité
├── 🚿 Plombier       → S'occupe SEULEMENT de la plomberie  
└── 🎨 Peintre        → S'occupe SEULEMENT de la peinture
```

C'est pareil en programmation ! Chaque classe doit avoir **UNE SEULE responsabilité** :

```
🏢 Application Spring Boot
├── 🌐 @RestController → S'occupe SEULEMENT de recevoir les requêtes
├── 🔧 @Service        → S'occupe SEULEMENT de la logique métier
└── 🗄️ @Repository     → S'occupe SEULEMENT des données
```

### 🤝 Pourquoi Séparer ?

**Sans séparation** (le chaos !) :
```java
// ❌ MAUVAIS EXEMPLE - Tout dans une seule classe
public class MessyController {
    public String getUser() {
        // Je reçois la requête
        // Je calcule des trucs compliqués  
        // Je vais chercher dans la base de données
        // Je renvoie la réponse
        // JE FAIS TOUT ! C'est le chaos !
    }
}
```

**Avec séparation** (l'harmonie !) :
```java
// ✅ BON EXEMPLE - Chacun son travail
@RestController  // "Je reçois et je renvoie"
public class UserController { }

@Service         // "Je calcule et je décide"  
public class UserService { }

@Repository      // "Je stocke et je récupère"
public class UserRepository { }
```

---

## 3. @Repository - La Couche de Données

### 🗄️ Le Gardien des Données

Imaginez un **bibliothécaire**. Son travail ? 

- 📚 **Ranger** les livres
- 🔍 **Retrouver** les livres qu'on lui demande
- ➕ **Ajouter** de nouveaux livres
- ❌ **Supprimer** les vieux livres

C'est exactement le rôle de `@Repository` !

### 📝 Définition Simple

```java
@Repository  // ← "Je suis le gardien des données !"
public class UserRepository {
    // Mon travail : parler à la base de données
}
```

### 🎯 Responsabilités de @Repository

`@Repository` s'occupe **UNIQUEMENT** de :

1. **CREATE** → Sauvegarder de nouvelles données
2. **READ** → Lire/chercher des données
3. **UPDATE** → Modifier des données existantes  
4. **DELETE** → Supprimer des données

*C'est ce qu'on appelle **CRUD** !*

### 💻 Exemple Concret : Repository d'Utilisateurs

```java
@Repository
public class UserRepository {
    
    // 📖 LIRE : Trouver un utilisateur par son ID
    public User findById(Long id) {
        // Je vais chercher dans la base de données
        // et je renvoie l'utilisateur trouvé
        return database.selectUserById(id);
    }
    
    // 💾 CRÉER : Sauvegarder un nouvel utilisateur  
    public User save(User user) {
        // Je sauvegarde l'utilisateur dans la base
        return database.insertUser(user);
    }
    
    // 🗑️ SUPPRIMER : Effacer un utilisateur
    public void deleteById(Long id) {
        // Je supprime l'utilisateur de la base
        database.deleteUserById(id);
    }
}
```

### 🚨 Ce que @Repository ne doit PAS faire

```java
@Repository  
public class UserRepository {
    
    // ❌ PAS LE TRAVAIL DE REPOSITORY !
    public boolean isUserVip(User user) {
        // Calculer si un user est VIP = LOGIQUE MÉTIER
        // Ça c'est le travail de @Service !
    }
    
    // ❌ PAS LE TRAVAIL DE REPOSITORY !  
    public ResponseEntity<User> sendUserInfo() {
        // Envoyer des réponses HTTP = TRAVAIL DE CONTROLLER
        // Ça c'est le travail de @RestController !
    }
}
```

### 🔧 Avec Spring Data JPA (Plus Facile)

Spring nous facilite la vie avec **JPA** :

```java
@Repository
public interface UserRepository extends JpaRepository<User, Long> {
    
    // 🪄 Spring génère automatiquement ces méthodes :
    // - save(user)
    // - findById(id)  
    // - findAll()
    // - deleteById(id)
    
    // 🎯 Je peux ajouter mes propres méthodes :
    User findByEmail(String email);
    List<User> findByAgeGreaterThan(int age);
    
    // 📝 Avec des requêtes personnalisées :
    @Query("SELECT u FROM User u WHERE u.name LIKE %:name%")
    List<User> findByNameContaining(@Param("name") String name);
}
```

---

## 4. @Service - La Logique Métier

### 🧠 Le Cerveau de l'Application

Si `@Repository` est le **bibliothécaire**, alors `@Service` est le **professeur** !

Le professeur :
- 🤔 **Réfléchit** et prend des décisions
- 📊 **Analyse** les informations  
- ⚖️ **Applique** les règles métier
- 🎯 **Coordonne** le travail des autres

### 📝 Définition Simple

```java
@Service  // ← "Je suis le cerveau qui réfléchit !"
public class UserService {
    // Mon travail : appliquer la logique métier
}
```

### 🎯 Responsabilités de @Service

`@Service` s'occupe de :

1. **Logique Métier** → Les règles de votre application
2. **Validation** → Vérifier que les données sont correctes
3. **Calculs** → Faire des opérations complexes
4. **Coordination** → Faire travailler les Repository ensemble
5. **Transformation** → Convertir les données d'un format à l'autre

### 💻 Exemple Concret : Service d'Utilisateurs

```java
@Service
public class UserService {
    
    // 🔗 J'ai besoin du Repository pour accéder aux données
    @Autowired
    private UserRepository userRepository;
    
    // 🎯 LOGIQUE MÉTIER : Créer un nouvel utilisateur
    public User createUser(String email, String password) {
        
        // 1. 🛡️ VALIDATION : Vérifier les données
        if (email == null || email.isEmpty()) {
            throw new IllegalArgumentException("L'email est obligatoire !");
        }
        
        if (password.length() < 8) {
            throw new IllegalArgumentException("Le mot de passe doit faire au moins 8 caractères !");
        }
        
        // 2. 🔍 VÉRIFICATION : L'utilisateur existe-t-il déjà ?
        User existingUser = userRepository.findByEmail(email);
        if (existingUser != null) {
            throw new IllegalArgumentException("Un utilisateur avec cet email existe déjà !");
        }
        
        // 3. 🔐 TRAITEMENT : Hasher le mot de passe
        String hashedPassword = hashPassword(password);
        
        // 4. 🏗️ CONSTRUCTION : Créer l'objet utilisateur
        User newUser = new User();
        newUser.setEmail(email);
        newUser.setPassword(hashedPassword);
        newUser.setCreatedAt(LocalDateTime.now());
        newUser.setActive(true);
        
        // 5. 💾 SAUVEGARDE : Demander au Repository de sauvegarder
        return userRepository.save(newUser);
    }
    
    // 🎯 LOGIQUE MÉTIER : Vérifier si un utilisateur est VIP
    public boolean isUserVip(Long userId) {
        User user = userRepository.findById(userId);
        
        if (user == null) {
            return false;
        }
        
        // 📊 RÈGLE MÉTIER : Un user est VIP si :
        // - Il a plus de 100 commandes OU
        // - Il a dépensé plus de 1000€
        return user.getOrderCount() > 100 || user.getTotalSpent() > 1000;
    }
    
    // 🔧 Méthode privée pour hasher les mots de passe
    private String hashPassword(String password) {
        // Logique de hashage...
        return BCrypt.hashpw(password, BCrypt.gensalt());
    }
}
```

### 🤝 Service qui Coordonne Plusieurs Repository

```java
@Service
public class OrderService {
    
    @Autowired
    private OrderRepository orderRepository;
    
    @Autowired  
    private UserRepository userRepository;
    
    @Autowired
    private ProductRepository productRepository;
    
    // 🎯 COORDINATION : Créer une commande complète
    public Order createOrder(Long userId, List<Long> productIds) {
        
        // 1. Vérifier que l'utilisateur existe
        User user = userRepository.findById(userId);
        if (user == null) {
            throw new IllegalArgumentException("Utilisateur introuvable !");
        }
        
        // 2. Vérifier que tous les produits existent
        List<Product> products = new ArrayList<>();
        double totalPrice = 0;
        
        for (Long productId : productIds) {
            Product product = productRepository.findById(productId);
            if (product == null) {
                throw new IllegalArgumentException("Produit " + productId + " introuvable !");
            }
            products.add(product);
            totalPrice += product.getPrice();
        }
        
        // 3. Appliquer les règles métier (remises, taxes, etc.)
        if (isUserVip(user)) {
            totalPrice *= 0.9; // 10% de remise pour les VIP
        }
        
        // 4. Créer et sauvegarder la commande
        Order order = new Order();
        order.setUser(user);
        order.setProducts(products);
        order.setTotalPrice(totalPrice);
        order.setOrderDate(LocalDateTime.now());
        
        return orderRepository.save(order);
    }
}
```

### 🚨 Ce que @Service ne doit PAS faire

```java
@Service
public class UserService {
    
    // ❌ PAS LE TRAVAIL DE SERVICE !
    public ResponseEntity<User> handleHttpRequest(HttpServletRequest request) {
        // Gérer HTTP = TRAVAIL DE CONTROLLER !
    }
    
    // ❌ PAS LE TRAVAIL DE SERVICE !
    public void directDatabaseAccess() {
        // Accès direct à la base = TRAVAIL DE REPOSITORY !
        // Utilisez plutôt @Autowired UserRepository
    }
}
```

---

## 5. @RestController - L'Interface Web

### 🚪 La Porte d'Entrée de votre Application

Imaginez un **réceptionniste** dans un hôtel :

- 👂 **Écoute** les demandes des clients
- 📋 **Comprend** ce qu'ils veulent
- 🤝 **Dirige** vers le bon service
- 📢 **Répond** aux clients

C'est exactement le rôle de `@RestController` !

### 📝 Définition Simple

```java
@RestController  // ← "Je suis la porte d'entrée web !"
public class UserController {
    // Mon travail : recevoir les requêtes HTTP et renvoyer des réponses
}
```

### 🎯 Responsabilités de @RestController

`@RestController` s'occupe de :

1. **Recevoir** les requêtes HTTP (GET, POST, PUT, DELETE)
2. **Extraire** les paramètres de la requête
3. **Appeler** le bon Service pour faire le travail
4. **Convertir** la réponse au bon format (JSON, XML...)
5. **Renvoyer** la réponse HTTP

### 🌐 Les Verbes HTTP (Les Actions Possibles)

```
📞 HTTP = Comment parler à votre application

GET    → 👀 "Montre-moi quelque chose"    (Lire)
POST   → ➕ "Crée quelque chose de nouveau" (Créer)  
PUT    → ✏️ "Modifie quelque chose"        (Modifier)
DELETE → 🗑️ "Supprime quelque chose"       (Supprimer)
```

### 💻 Exemple Concret : Controller d'Utilisateurs

```java
@RestController
@RequestMapping("/api/users")  // ← Toutes mes URLs commencent par /api/users
public class UserController {
    
    // 🔗 J'ai besoin du Service pour faire le vrai travail
    @Autowired
    private UserService userService;
    
    // 👀 GET : Récupérer tous les utilisateurs
    @GetMapping  // URL : GET /api/users
    public List<User> getAllUsers() {
        // 1. Je reçois la requête
        // 2. Je demande au Service de faire le travail
        // 3. Je renvoie la réponse
        return userService.getAllUsers();
    }
    
    // 👀 GET : Récupérer un utilisateur par son ID
    @GetMapping("/{id}")  // URL : GET /api/users/123
    public User getUserById(@PathVariable Long id) {
        // @PathVariable récupère {id} dans l'URL
        return userService.getUserById(id);
    }
    
    // ➕ POST : Créer un nouvel utilisateur
    @PostMapping  // URL : POST /api/users
    public User createUser(@RequestBody CreateUserRequest request) {
        // @RequestBody convertit le JSON en objet Java
        return userService.createUser(request.getEmail(), request.getPassword());
    }
    
    // ✏️ PUT : Modifier un utilisateur existant
    @PutMapping("/{id}")  // URL : PUT /api/users/123
    public User updateUser(@PathVariable Long id, @RequestBody UpdateUserRequest request) {
        return userService.updateUser(id, request);
    }
    
    // 🗑️ DELETE : Supprimer un utilisateur
    @DeleteMapping("/{id}")  // URL : DELETE /api/users/123
    public ResponseEntity<Void> deleteUser(@PathVariable Long id) {
        userService.deleteUser(id);
        return ResponseEntity.ok().build(); // Réponse vide avec statut 200 OK
    }
}
```

### 🔍 Comprendre les Annotations de Mapping

```java
@RestController
public class UserController {
    
    // 🎯 Récupérer des paramètres de différentes façons :
    
    // 1. @PathVariable : Depuis l'URL
    @GetMapping("/users/{id}")
    public User getUser(@PathVariable Long id) {
        // URL : /users/123 → id = 123
    }
    
    // 2. @RequestParam : Depuis les paramètres d'URL  
    @GetMapping("/users")
    public List<User> getUsers(@RequestParam(required = false) String name) {
        // URL : /users?name=john → name = "john"
    }
    
    // 3. @RequestBody : Depuis le corps de la requête (JSON)
    @PostMapping("/users")
    public User createUser(@RequestBody User user) {
        // Le JSON dans le body est converti en objet User
    }
    
    // 4. Combinaisons multiples
    @GetMapping("/users/{id}/orders")
    public List<Order> getUserOrders(
        @PathVariable Long id,              // Depuis l'URL
        @RequestParam int page,             // Depuis les paramètres
        @RequestParam(defaultValue = "10") int size  // Avec valeur par défaut
    ) {
        // URL : /users/123/orders?page=1&size=20
    }
}
```

### 🛡️ Gestion des Erreurs

```java
@RestController  
public class UserController {
    
    @Autowired
    private UserService userService;
    
    @GetMapping("/users/{id}")
    public ResponseEntity<User> getUserById(@PathVariable Long id) {
        try {
            User user = userService.getUserById(id);
            return ResponseEntity.ok(user);  // 200 OK avec l'utilisateur
            
        } catch (UserNotFoundException e) {
            return ResponseEntity.notFound().build();  // 404 Not Found
            
        } catch (Exception e) {
            return ResponseEntity.internalServerError().build();  // 500 Internal Server Error
        }
    }
    
    // 📝 Ou encore mieux, avec @ExceptionHandler
    @ExceptionHandler(UserNotFoundException.class)
    public ResponseEntity<String> handleUserNotFound(UserNotFoundException e) {
        return ResponseEntity.status(404).body("Utilisateur non trouvé : " + e.getMessage());
    }
}
```

### 🚨 Ce que @RestController ne doit PAS faire

```java
@RestController
public class UserController {
    
    // ❌ PAS LE TRAVAIL DE CONTROLLER !
    @PostMapping("/users")  
    public User createUser(@RequestBody User user) {
        // Validation complexe = TRAVAIL DE SERVICE !
        if (user.getAge() < 18) {
            // Logique métier = SERVICE !
        }
        
        // Accès direct à la base = TRAVAIL DE REPOSITORY !
        database.save(user);
    }
}
```

---

## 6. Comment Tout Fonctionne Ensemble

### 🎭 La Pièce de Théâtre Complète

Imaginez une pièce de théâtre avec 3 acteurs qui doivent jouer ensemble :

```
🎬 SCÈNE : "Créer un nouvel utilisateur"

👤 CLIENT    → "Je veux créer un utilisateur !"
              ↓
🌐 CONTROLLER → "J'ai reçu ta demande, laisse-moi m'en occuper"
              ↓  
🔧 SERVICE   → "Ok, je vérifie tout et je prépare"
              ↓
🗄️ REPOSITORY → "Je sauvegarde dans la base de données"
              ↑
🔧 SERVICE   ← "Merci ! Voici le résultat"
              ↑
🌐 CONTROLLER ← "Parfait ! Voici ta réponse"
              ↑
👤 CLIENT    ← "Super, merci !"
```

### 🔄 Le Flux Complet (Step by Step)

Voici ce qui se passe quand quelqu'un fait une requête `POST /api/users` :

#### Étape 1 : Le Controller Reçoit
```java
@RestController
public class UserController {
    
    @Autowired
    private UserService userService;  // ← Il connaît le Service
    
    @PostMapping("/api/users")
    public User createUser(@RequestBody CreateUserRequest request) {
        System.out.println("🌐 Controller : J'ai reçu une demande de création !");
        
        // Je passe le relais au Service
        return userService.createUser(request.getEmail(), request.getPassword());
    }
}
```

#### Étape 2 : Le Service Traite
```java
@Service  
public class UserService {
    
    @Autowired
    private UserRepository userRepository;  // ← Il connaît le Repository
    
    public User createUser(String email, String password) {
        System.out.println("🔧 Service : Je vais valider et traiter ça !");
        
        // 1. Validation
        if (email == null) {
            throw new IllegalArgumentException("Email obligatoire !");
        }
        
        // 2. Vérification unicité  
        if (userRepository.existsByEmail(email)) {
            throw new IllegalArgumentException("Email déjà utilisé !");
        }
        
        // 3. Préparation des données
        User user = new User();
        user.setEmail(email);
        user.setPassword(hashPassword(password));
        user.setCreatedAt(LocalDateTime.now());
        
        // Je passe le relais au Repository
        return userRepository.save(user);
    }
}
```

#### Étape 3 : Le Repository Sauvegarde
```java
@Repository
public interface UserRepository extends JpaRepository<User, Long> {
    
    boolean existsByEmail(String email);
    
    // La méthode save() est héritée de JpaRepository
    // Elle fait automatiquement :
    // INSERT INTO users (email, password, created_at) VALUES (?, ?, ?)
}
```

### 🔗 L'Injection de Dépendances (@Autowired)

**Comment ils se connaissent entre eux ?**

```java
// 🤔 SANS @Autowired (le cauchemar !)
@RestController  
public class UserController {
    
    public User createUser(@RequestBody CreateUserRequest request) {
        // Je dois créer le Service moi-même...
        UserRepository userRepository = new UserRepository();
        UserService userService = new UserService(userRepository);
        
        // Et si UserService a besoin d'autres services ?
        // Et si ces services ont besoin d'autres services ?
        // C'est l'enfer ! 😱
    }
}
```

```java
// 😇 AVEC @Autowired (la magie !)
@RestController
public class UserController {
    
    @Autowired
    private UserService userService;  // ← Spring s'occupe de tout !
    
    public User createUser(@RequestBody CreateUserRequest request) {
        // Je peux directement utiliser userService
        // Spring a tout préparé pour moi ! ✨
        return userService.createUser(request.getEmail(), request.getPassword());
    }
}
```

**Comment Spring fait cette magie ?**

1. 🔍 **Scan** : Spring scanne toutes vos classes
2. 🏷️ **Détection** : Il trouve celles avec `@Service`, `@Repository`, `@RestController`
3. 🏗️ **Création** : Il crée une instance de chaque classe (un "bean")
4. 🔗 **Injection** : Il injecte automatiquement les dépendances avec `@Autowired`

```
🧙‍♂️ Spring Boot au démarrage :

"Oh, je vois une classe UserController qui a besoin d'un UserService...
 Et UserService a besoin d'un UserRepository...
 Pas de problème ! Je vais créer tout ça et les connecter !"

UserRepository userRepo = new UserRepository();
UserService userService = new UserService(userRepo);  
UserController userController = new UserController(userService);

"Et voilà ! Tout est prêt !" ✨
```

---

## 7. Exemples Concrets et Progressifs

### 🌱 Niveau 1 : Application Simple (Blog)

Créons ensemble une petite application de blog étape par étape.

#### L'Entité Article
```java
@Entity
@Table(name = "articles")
public class Article {
    @Id
    @GeneratedValue(strategy = GenerationType.IDENTITY)
    private Long id;
    
    @Column(nullable = false)
    private String title;
    
    @Column(columnDefinition = "TEXT")
    private String content;
    
    private String author;
    
    @CreationTimestamp
    private LocalDateTime createdAt;
    
    // Constructeurs, getters, setters...
}
```

#### 🗄️ Repository : Accès aux Données
```java
@Repository
public interface ArticleRepository extends JpaRepository<Article, Long> {
    
    // 🔍 Méthodes de recherche générées automatiquement
    List<Article> findByAuthor(String author);
    List<Article> findByTitleContaining(String keyword);
    
    // 📝 Requête personnalisée
    @Query("SELECT a FROM Article a WHERE a.createdAt >= :date ORDER BY a.createdAt DESC")
    List<Article> findRecentArticles(@Param("date") LocalDateTime date);
}
```

#### 🔧 Service : Logique Métier
```java
@Service
public class ArticleService {
    
    @Autowired
    private ArticleRepository articleRepository;
    
    // 📖 Récupérer tous les articles
    public List<Article> getAllArticles() {
        return articleRepository.findAll();
    }
    
    // 📖 Récupérer un article par ID
    public Article getArticleById(Long id) {
        return articleRepository.findById(id)
            .orElseThrow(() -> new ArticleNotFoundException("Article non trouvé avec l'ID : " + id));
    }
    
    // ✍️ Créer un nouvel article
    public Article createArticle(String title, String content, String author) {
        // 🛡️ Validation
        if (title == null || title.trim().isEmpty()) {
            throw new IllegalArgumentException("Le titre est obligatoire !");
        }
        
        if (content == null || content.trim().isEmpty()) {
            throw new IllegalArgumentException("Le contenu est obligatoire !");
        }
        
        if (author == null || author.trim().isEmpty()) {
            throw new IllegalArgumentException("L'auteur est obligatoire !");
        }
        
        // 🏗️ Construction
        Article article = new Article();
        article.setTitle(title.trim());
        article.setContent(content.trim());
        article.setAuthor(author.trim());
        
        // 💾 Sauvegarde
        return articleRepository.save(article);
    }
    
    // 🔍 Rechercher des articles
    public List<Article> searchArticles(String keyword) {
        if (keyword == null || keyword.trim().isEmpty()) {
            return getAllArticles();
        }
        
        return articleRepository.findByTitleContaining(keyword.trim());
    }
    
    // 📅 Articles récents (derniers 30 jours)
    public List<Article> getRecentArticles() {
        LocalDateTime thirtyDaysAgo = LocalDateTime.now().minusDays(30);
        return articleRepository.findRecentArticles(thirtyDaysAgo);
    }
}
```

#### 🌐 Controller : Interface Web
```java
@RestController
@RequestMapping("/api/articles")
public class ArticleController {
    
    @Autowired
    private ArticleService articleService;
    
    // 📋 GET /api/articles - Tous les articles
    @GetMapping
    public List<Article> getAllArticles() {
        return articleService.getAllArticles();
    }
    
    // 📄 GET /api/articles/123 - Un article spécifique
    @GetMapping("/{id}")
    public ResponseEntity<Article> getArticle(@PathVariable Long id) {
        try {
            Article article = articleService.getArticleById(id);
            return ResponseEntity.ok(article);
        } catch (ArticleNotFoundException e) {
            return ResponseEntity.notFound().build();
        }
    }
    
    // ✍️ POST /api/articles - Créer un nouvel article
    @PostMapping
    public ResponseEntity<Article> createArticle(@RequestBody CreateArticleRequest request) {
        try {
            Article article = articleService.createArticle(
                request.getTitle(),
                request.getContent(), 
                request.getAuthor()
            );
            return ResponseEntity.status(201).body(article); // 201 Created
        } catch (IllegalArgumentException e) {
            return ResponseEntity.badRequest().build(); // 400 Bad Request
        }
    }
    
    // 🔍 GET /api/articles/search?keyword=spring - Rechercher
    @GetMapping("/search")
    public List<Article> searchArticles(@RequestParam(required = false) String keyword) {
        return articleService.searchArticles(keyword);
    }
    
    // 📅 GET /api/articles/recent - Articles récents
    @GetMapping("/recent")
    public List<Article> getRecentArticles() {
        return articleService.getRecentArticles();
    }
}

// 📝 DTO pour la création d'articles
class CreateArticleRequest {
    private String title;
    private String content;
    private String author;
    
    // Getters et setters...
    public String getTitle() { return title; }
    public void setTitle(String title) { this.title = title; }
    public String getContent() { return content; }
    public void setContent(String content) { this.content = content; }
    public String getAuteur() { return author; }
    public void setAuthor(String author) { this.author = author; }
}
```

### 🌿 Niveau 2 : Application Plus Complexe (E-commerce)

Maintenant, créons quelque chose de plus complexe avec plusieurs entités qui interagissent.

#### Les Entités
```java
// 👤 Utilisateur
@Entity
public class User {
    @Id
    @GeneratedValue(strategy = GenerationType.IDENTITY)
    private Long id;
    private String email;
    private String password;
    private String firstName;
    private String lastName;
    private boolean isVip;
    
    @OneToMany(mappedBy = "user")
    private List<Order> orders = new ArrayList<>();
    
    // Constructeurs, getters, setters...
}

// 📦 Produit  
@Entity
public class Product {
    @Id
    @GeneratedValue(strategy = GenerationType.IDENTITY)
    private Long id;
    private String name;
    private String description;
    private BigDecimal price;
    private int stockQuantity;
    
    // Constructeurs, getters, setters...
}

// 🛒 Commande
@Entity
@Table(name = "orders")
public class Order {
    @Id
    @GeneratedValue(strategy = GenerationType.IDENTITY)
    private Long id;
    
    @ManyToOne
    private User user;
    
    @ManyToMany
    private List<Product> products;
    
    private BigDecimal totalAmount;
    private LocalDateTime orderDate;
    private OrderStatus status;
    
    // Constructeurs, getters, setters...
}

enum OrderStatus {
    PENDING, CONFIRMED, SHIPPED, DELIVERED, CANCELLED
}
```

#### 🗄️ Repositories
```java
@Repository
public interface UserRepository extends JpaRepository<User, Long> {
    Optional<User> findByEmail(String email);
    List<User> findByIsVip(boolean isVip);
}

@Repository  
public interface ProductRepository extends JpaRepository<Product, Long> {
    List<Product> findByNameContaining(String name);
    List<Product> findByPriceBetween(BigDecimal minPrice, BigDecimal maxPrice);
    List<Product> findByStockQuantityGreaterThan(int quantity);
}

@Repository
public interface OrderRepository extends JpaRepository<Order, Long> {
    List<Order> findByUser(User user);
    List<Order> findByStatus(OrderStatus status);
    
    @Query("SELECT o FROM Order o WHERE o.orderDate >= :startDate AND o.orderDate <= :endDate")
    List<Order> findOrdersBetweenDates(@Param("startDate") LocalDateTime start, 
                                       @Param("endDate") LocalDateTime end);
}
```

#### 🔧 Services (Plus Complexes)
```java
@Service
@Transactional // ← Important pour les opérations qui modifient plusieurs tables
public class OrderService {
    
    @Autowired
    private OrderRepository orderRepository;
    
    @Autowired
    private UserRepository userRepository;
    
    @Autowired
    private ProductRepository productRepository;
    
    @Autowired
    private EmailService emailService; // Service pour envoyer des emails
    
    // 🛒 Créer une nouvelle commande
    public Order createOrder(Long userId, List<Long> productIds) {
        
        // 1. 🔍 Vérifier que l'utilisateur existe
        User user = userRepository.findById(userId)
            .orElseThrow(() -> new UserNotFoundException("Utilisateur introuvable"));
        
        // 2. 🔍 Vérifier que tous les produits existent et sont en stock
        List<Product> products = new ArrayList<>();
        BigDecimal totalAmount = BigDecimal.ZERO;
        
        for (Long productId : productIds) {
            Product product = productRepository.findById(productId)
                .orElseThrow(() -> new ProductNotFoundException("Produit " + productId + " introuvable"));
            
            if (product.getStockQuantity() <= 0) {
                throw new OutOfStockException("Produit " + product.getName() + " en rupture de stock");
            }
            
            products.add(product);
            totalAmount = totalAmount.add(product.getPrice());
        }
        
        // 3. 💰 Appliquer les remises (logique métier)
        if (user.isVip()) {
            totalAmount = totalAmount.multiply(BigDecimal.valueOf(0.9)); // 10% de remise VIP
        }
        
        if (totalAmount.compareTo(BigDecimal.valueOf(100)) >= 0) {
            totalAmount = totalAmount.subtract(BigDecimal.valueOf(5)); // -5€ si > 100€
        }
        
        // 4. 🏗️ Créer la commande
        Order order = new Order();
        order.setUser(user);
        order.setProducts(products);
        order.setTotalAmount(totalAmount);
        order.setOrderDate(LocalDateTime.now());
        order.setStatus(OrderStatus.PENDING);
        
        // 5. 📉 Diminuer les stocks
        for (Product product : products) {
            product.setStockQuantity(product.getStockQuantity() - 1);
            productRepository.save(product);
        }
        
        // 6. 💾 Sauvegarder la commande
        Order savedOrder = orderRepository.save(order);
        
        // 7. 📧 Envoyer un email de confirmation (asynchrone)
        emailService.sendOrderConfirmation(user.getEmail(), savedOrder);
        
        return savedOrder;
    }
    
    // 📊 Statistiques des ventes
    public OrderStatistics getOrderStatistics() {
        List<Order> allOrders = orderRepository.findAll();
        
        BigDecimal totalRevenue = allOrders.stream()
            .map(Order::getTotalAmount)
            .reduce(BigDecimal.ZERO, BigDecimal::add);
            
        long totalOrders = allOrders.size();
        
        BigDecimal averageOrderValue = totalOrders > 0 
            ? totalRevenue.divide(BigDecimal.valueOf(totalOrders), 2, RoundingMode.HALF_UP)
            : BigDecimal.ZERO;
        
        return new OrderStatistics(totalRevenue, totalOrders, averageOrderValue);
    }
    
    // 🔄 Changer le statut d'une commande
    public Order updateOrderStatus(Long orderId, OrderStatus newStatus) {
        Order order = orderRepository.findById(orderId)
            .orElseThrow(() -> new OrderNotFoundException("Commande introuvable"));
            
        // 🛡️ Validation des transitions de statut
        if (!isValidStatusTransition(order.getStatus(), newStatus)) {
            throw new InvalidStatusTransitionException(
                "Impossible de passer de " + order.getStatus() + " à " + newStatus);
        }
        
        order.setStatus(newStatus);
        
        // 📧 Notifier le client selon le nouveau statut
        switch (newStatus) {
            case CONFIRMED:
                emailService.sendOrderConfirmed(order.getUser().getEmail(), order);
                break;
            case SHIPPED:
                emailService.sendOrderShipped(order.getUser().getEmail(), order);
                break;
            case DELIVERED:
                emailService.sendOrderDelivered(order.getUser().getEmail(), order);
                break;
        }
        
        return orderRepository.save(order);
    }
    
    // 🔧 Méthode privée pour valider les transitions de statut
    private boolean isValidStatusTransition(OrderStatus currentStatus, OrderStatus newStatus) {
        switch (currentStatus) {
            case PENDING:
                return newStatus == OrderStatus.CONFIRMED || newStatus == OrderStatus.CANCELLED;
            case CONFIRMED:
                return newStatus == OrderStatus.SHIPPED || newStatus == OrderStatus.CANCELLED;
            case SHIPPED:
                return newStatus == OrderStatus.DELIVERED;
            case DELIVERED:
            case CANCELLED:
                return false; // Statuts finaux
            default:
                return false;
        }
    }
}

// 📧 Service pour les emails
@Service
public class EmailService {
    
    public void sendOrderConfirmation(String email, Order order) {
        // Logique d'envoi d'email...
        System.out.println("📧 Email de confirmation envoyé à " + email);
    }
    
    public void sendOrderConfirmed(String email, Order order) {
        System.out.println("📧 Email de confirmation de commande envoyé à " + email);
    }
    
    public void sendOrderShipped(String email, Order order) {
        System.out.println("📧 Email d'expédition envoyé à " + email);
    }
    
    public void sendOrderDelivered(String email, Order order) {
        System.out.println("📧 Email de livraison envoyé à " + email);
    }
}
```

#### 🌐 Controllers (API REST Complète)
```java
@RestController
@RequestMapping("/api/orders")
public class OrderController {
    
    @Autowired
    private OrderService orderService;
    
    // 🛒 POST /api/orders - Créer une commande
    @PostMapping
    public ResponseEntity<Order> createOrder(@RequestBody CreateOrderRequest request) {
        try {
            Order order = orderService.createOrder(request.getUserId(), request.getProductIds());
            return ResponseEntity.status(201).body(order);
        } catch (UserNotFoundException | ProductNotFoundException e) {
            return ResponseEntity.badRequest().build();
        } catch (OutOfStockException e) {
            return ResponseEntity.status(409).build(); // 409 Conflict
        }
    }
    
    // 📋 GET /api/orders/{id} - Détails d'une commande
    @GetMapping("/{id}")
    public ResponseEntity<Order> getOrder(@PathVariable Long id) {
        try {
            Order order = orderService.getOrderById(id);
            return ResponseEntity.ok(order);
        } catch (OrderNotFoundException e) {
            return ResponseEntity.notFound().build();
        }
    }
    
    // 🔄 PUT /api/orders/{id}/status - Changer le statut
    @PutMapping("/{id}/status")
    public ResponseEntity<Order> updateOrderStatus(
        @PathVariable Long id, 
        @RequestBody UpdateOrderStatusRequest request
    ) {
        try {
            Order order = orderService.updateOrderStatus(id, request.getStatus());
            return ResponseEntity.ok(order);
        } catch (OrderNotFoundException e) {
            return ResponseEntity.notFound().build();
        } catch (InvalidStatusTransitionException e) {
            return ResponseEntity.badRequest().build();
        }
    }
    
    // 📊 GET /api/orders/statistics - Statistiques
    @GetMapping("/statistics")  
    public OrderStatistics getStatistics() {
        return orderService.getOrderStatistics();
    }
}

// 📝 DTOs
class CreateOrderRequest {
    private Long userId;
    private List<Long> productIds;
    // Getters et setters...
}

class UpdateOrderStatusRequest {
    private OrderStatus status;
    // Getters et setters...
}

class OrderStatistics {
    private BigDecimal totalRevenue;
    private long totalOrders;
    private BigDecimal averageOrderValue;
    
    public OrderStatistics(BigDecimal totalRevenue, long totalOrders, BigDecimal averageOrderValue) {
        this.totalRevenue = totalRevenue;
        this.totalOrders = totalOrders;
        this.averageOrderValue = averageOrderValue;
    }
    // Getters et setters...
}
```

---

## 8. Bonnes Pratiques et Pièges à Éviter

### ✅ Bonnes Pratiques

#### 1. **Utilisez les Interfaces pour les Services**
```java
// ✅ BON : Interface + Implémentation
public interface UserService {
    User createUser(String email, String password);
    User getUserById(Long id);
}

@Service
public class UserServiceImpl implements UserService {
    // Implémentation...
}

// ✅ Dans le Controller
@Autowired
private UserService userService; // ← Interface, pas l'implémentation
```

#### 2. **Validation dans les Services**
```java
@Service
public class UserService {
    
    public User createUser(String email, String password) {
        // ✅ BON : Validation dans le Service
        if (email == null || email.trim().isEmpty()) {
            throw new IllegalArgumentException("Email obligatoire");
        }
        
        if (!email.matches("^[A-Za-z0-9+_.-]+@(.+)$")) {
            throw new IllegalArgumentException("Format d'email invalide");
        }
        
        if (password == null || password.length() < 8) {
            throw new IllegalArgumentException("Mot de passe trop court");
        }
        
        // Suite du traitement...
    }
}
```

#### 3. **Gestion d'Erreurs Centralisée**
```java
// ✅ BON : Gestionnaire d'erreurs global
@ControllerAdvice
public class GlobalExceptionHandler {
    
    @ExceptionHandler(IllegalArgumentException.class)
    public ResponseEntity<ErrorResponse> handleValidationError(IllegalArgumentException e) {
        ErrorResponse error = new ErrorResponse("VALIDATION_ERROR", e.getMessage());
        return ResponseEntity.badRequest().body(error);
    }
    
    @ExceptionHandler(UserNotFoundException.class)
    public ResponseEntity<ErrorResponse> handleUserNotFound(UserNotFoundException e) {
        ErrorResponse error = new ErrorResponse("USER_NOT_FOUND", e.getMessage());
        return ResponseEntity.notFound().body(error);
    }
    
    @ExceptionHandler(Exception.class)
    public ResponseEntity<ErrorResponse> handleGenericError(Exception e) {
        ErrorResponse error = new ErrorResponse("INTERNAL_ERROR", "Une erreur est survenue");
        return ResponseEntity.internalServerError().body(error);
    }
}

class ErrorResponse {
    private String code;
    private String message;
    private LocalDateTime timestamp;
    
    public ErrorResponse(String code, String message) {
        this.code = code;
        this.message = message;
        this.timestamp = LocalDateTime.now();
    }
    // Getters et setters...
}
```

#### 4. **Transactions pour les Opérations Complexes**
```java
@Service
@Transactional // ✅ BON : Transaction au niveau de la classe
public class OrderService {
    
    @Transactional // ✅ BON : Peut aussi être au niveau de la méthode
    public Order createOrder(Long userId, List<Long> productIds) {
        // Si une erreur survient, TOUT sera annulé (rollback)
        User user = userRepository.findById(userId).orElseThrow();
        
        // Diminuer les stocks
        for (Long productId : productIds) {
            Product product = productRepository.findById(productId).orElseThrow();
            product.setStockQuantity(product.getStockQuantity() - 1);
            productRepository.save(product);
        }
        
        // Créer la commande
        Order order = new Order(/* ... */);
        return orderRepository.save(order);
        
        // Si une exception est lancée, tous les changements sont annulés !
    }
}
```

### ❌ Pièges à Éviter

#### 1. **Mélanger les Responsabilités**
```java
// ❌ MAUVAIS : Controller qui fait tout
@RestController  
public class UserController {
    
    @PostMapping("/users")
    public User createUser(@RequestBody User user) {
        // ❌ Validation dans le Controller (devrait être dans Service)
        if (user.getEmail() == null) {
            throw new IllegalArgumentException("Email obligatoire");
        }
        
        // ❌ Accès direct à la base (devrait être dans Repository)  
        if (database.userExists(user.getEmail())) {
            throw new IllegalArgumentException("Email déjà utilisé");
        }
        
        // ❌ Logique métier dans Controller (devrait être dans Service)
        user.setPassword(hashPassword(user.getPassword()));
        
        // ❌ Sauvegarde directe (devrait être dans Repository)
        return database.save(user);
    }
}
```

#### 2. **Oublier la Gestion d'Erreurs**
```java
// ❌ MAUVAIS : Pas de gestion d'erreur
@RestController
public class UserController {
    
    @GetMapping("/users/{id}")
    public User getUser(@PathVariable Long id) {
        // ❌ Que se passe-t-il si l'utilisateur n'existe pas ?
        // L'application va planter avec une exception !
        return userService.getUserById(id);
    }
}

// ✅ BON : Avec gestion d'erreur
@RestController  
public class UserController {
    
    @GetMapping("/users/{id}")
    public ResponseEntity<User> getUser(@PathVariable Long id) {
        try {
            User user = userService.getUserById(id);
            return ResponseEntity.ok(user);
        } catch (UserNotFoundException e) {
            return ResponseEntity.notFound().build();
        }
    }
}
```

#### 3. **Services qui Retournent des ResponseEntity**
```java
// ❌ MAUVAIS : Service qui retourne ResponseEntity
@Service
public class UserService {
    
    public ResponseEntity<User> getUserById(Long id) {
        // ❌ ResponseEntity, c'est pour les Controllers !
        User user = userRepository.findById(id).orElse(null);
        if (user == null) {
            return ResponseEntity.notFound().build();
        }
        return ResponseEntity.ok(user);
    }
}

// ✅ BON : Service qui retourne l'objet métier
@Service
public class UserService {
    
    public User getUserById(Long id) {
        // ✅ Service retourne l'objet ou lance une exception
        return userRepository.findById(id)
            .orElseThrow(() -> new UserNotFoundException("User not found with id: " + id));
    }
}
```

#### 4. **Repository avec Logique Métier**
```java
// ❌ MAUVAIS : Repository avec logique métier
@Repository
public class UserRepository extends JpaRepository<User, Long> {
    
    public boolean isUserVip(Long userId) {
        User user = findById(userId).orElse(null);
        if (user == null) return false;
        
        // ❌ Logique métier dans Repository !
        return user.getOrderCount() > 100 || user.getTotalSpent() > 1000;
    }
}

// ✅ BON : Repository simple, logique dans Service
@Repository  
public interface UserRepository extends JpaRepository<User, Long> {
    // ✅ Juste des requêtes simples
    Optional<User> findByEmail(String email);
    List<User> findByCreatedAtAfter(LocalDateTime date);
}

@Service
public class UserService {
    
    public boolean isUserVip(Long userId) {
        User user = userRepository.findById(userId)
            .orElseThrow(() -> new UserNotFoundException("User not found"));
            
        // ✅ Logique métier dans Service
        return user.getOrderCount() > 100 || user.getTotalSpent() > 1000;
    }
}
```

---

## 9. Exercices Pratiques

### 🎯 Exercice 1 : Blog Simple (Débutant)

**Objectif :** Créer un système de blog avec articles et commentaires.

**Entités à créer :**
- `Article` (id, title, content, author, createdAt)
- `Comment` (id, content, author, article, createdAt)

**À implémenter :**

1. **Repository :** 
   - ArticleRepository avec recherche par titre
   - CommentRepository avec recherche par article

2. **Service :**
   - ArticleService avec validation des données
   - CommentService avec vérification que l'article existe

3. **Controller :**
   - API REST complète pour articles et commentaires
   - GET, POST, PUT, DELETE

**Questions :**
- Où mettez-vous la validation "un commentaire ne peut pas être vide" ?
- Où mettez-vous la logique "un article doit avoir un titre" ?
- Comment gérer l'erreur "article introuvable" ?

### 🎯 Exercice 2 : Système de Réservation (Intermédiaire)

**Objectif :** Créer un système de réservation de salles.

**Entités à créer :**
- `Room` (id, name, capacity, pricePerHour)
- `User` (id, email, firstName, lastName)  
- `Reservation` (id, room, user, startTime, endTime, totalPrice)

**Logique métier à implémenter :**
- Une salle ne peut pas être réservée si elle est déjà occupée
- Le prix total = (heures réservées) × (prix par heure)
- Une réservation doit durer minimum 1 heure
- On ne peut pas réserver dans le passé

**Questions :**
- Dans quelle couche vérifiez-vous les conflits de réservation ?
- Où calculez-vous le prix total ?
- Comment gérez-vous la validation des dates ?

### 🎯 Exercice 3 : E-commerce Avancé (Expert)

**Objectif :** Système e-commerce avec gestion des stocks et promotions.

**Entités :**
- `Product`, `User`, `Order`, `OrderItem`, `Promotion`

**Fonctionnalités avancées :**
- Gestion des stocks en temps réel
- Application automatique des promotions
- Gestion des remises par type d'utilisateur (VIP, Normal)
- Historique des prix
- Notifications par email

**Défis :**
- Gérer les transactions pour éviter la survente
- Appliquer plusieurs promotions en même temps
- Calculer les prix avec remises, taxes, frais de port
- Gérer les erreurs complexes (rupture de stock partielle)

---

## 🎯 Résumé Final

### 🔑 Les Points Clés à Retenir

| Annotation | Rôle | Responsabilités | ❌ Ne doit PAS |
|-----------|------|-----------------|----------------|
| **@Repository** | 🗄️ Gardien des données | CREATE, READ, UPDATE, DELETE | Logique métier, Validation complexe |
| **@Service** | 🧠 Cerveau logique | Validation, Calculs, Règles métier, Coordination | HTTP, Accès direct BDD |
| **@RestController** | 🚪 Porte d'entrée | Recevoir requêtes, Appeler services, Renvoyer réponses | Logique métier, Accès BDD |

### 🎭 L'Analogie Finale : L'Orchestre

Imaginez un orchestre :

```
🎼 CHEF D'ORCHESTRE (@RestController)
   ├── 👂 Écoute les demandes du public
   ├── 📋 Dirige l'orchestre  
   └── 🎵 Présente le résultat final

🎻 VIOLONISTES (@Service)  
   ├── 🎯 Jouent la mélodie principale
   ├── 🤝 Coordonnent entre eux
   └── 🎨 Créent la beauté musicale

📚 BIBLIOTHÉCAIRE MUSICAL (@Repository)
   ├── 🗄️ Garde toutes les partitions
   ├── 🔍 Trouve la bonne partition quand on la demande
   └── 📝 Range les nouvelles partitions
```

Chacun a son rôle, et ensemble ils créent une symphonie magnifique ! 🎵

### 💡 Le Conseil Final

**Rappelez-vous toujours :**
- Une classe = Une responsabilité
- Les annotations sont vos guides
- Spring Boot s'occupe de la plomberie, vous vous occupez de la logique
- En cas de doute, demandez-vous : "Si j'étais cette classe, quel serait MON travail ?"

**Et surtout... Amusez-vous ! 🚀**

La programmation, c'est comme apprendre un instrument : au début c'est difficile, mais une fois qu'on a compris les bases, on peut créer des merveilles !

---

*🎓 Félicitations ! Vous maîtrisez maintenant les annotations Spring Boot ! 
N'hésitez pas à pratiquer avec les exercices et à expérimenter. 
C'est en forgeant qu'on devient forgeron ! ⚒️*