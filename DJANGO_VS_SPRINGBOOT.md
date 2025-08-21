# 🏗️ Django vs Spring Boot - Guide de Transition

> Comprendre Spring Boot à partir de vos connaissances Django

## 📋 Table des Matières

- [Vue d'ensemble](#vue-densemble)
- [Architecture Comparée](#architecture-comparée)
- [Correspondances Conceptuelles](#correspondances-conceptuelles)
- [Différences Clés](#différences-clés)
- [Structure des Projets](#structure-des-projets)
- [Exemples de Code](#exemples-de-code)
- [Points Clés pour la Transition](#points-clés-pour-la-transition)

## Vue d'ensemble

| Aspect | Django (Python) | Spring Boot (Java) |
|--------|-----------------|-------------------|
| **Architecture** | MVT (Model-View-Template) | MVC + IoC Container |
| **Philosophie** | "Batteries incluses" | Auto-configuration flexible |
| **ORM** | Django ORM intégré | JPA/Hibernate |
| **Configuration** | settings.py centralisé | application.yml + annotations |
| **Dépendances** | pip + requirements.txt | Maven/Gradle |

## Architecture Comparée

### 🐍 Django - Architecture MVT

```
🌐 URLs & Routing
   ↓ urls.py → urlpatterns
   
👁️ Views (Contrôleurs)
   ↓ views.py → function/class-based views
   
🏗️ Models (ORM)
   ↓ models.py → Django ORM
   
🎨 Templates
   ↓ templates/ → Django Template Language
   
⚙️ Settings & Configuration
   ↓ settings.py → DATABASES, MIDDLEWARE
```

### ☕ Spring Boot - Architecture MVC + IoC

```
🌐 Controllers & Routing
   ↓ @RestController, @RequestMapping
   
🔧 Services (Logique métier)
   ↓ @Service, @Component
   
🏗️ Repositories (JPA/Hibernate)
   ↓ @Repository, JpaRepository
   
🎯 Entities/DTOs
   ↓ @Entity, @Table, POJO classes
   
⚙️ Configuration
   ↓ application.yml, @Configuration
```

## Correspondances Conceptuelles

| Django | ↔️ | Spring Boot | Description |
|--------|---|-------------|-------------|
| `urls.py` | ↔️ | `@RequestMapping` | Routage des URLs vs Annotations sur contrôleurs |
| `Views` | ↔️ | `Controllers + Services` | Logique de traitement vs Séparation contrôleur/logique |
| `Models (ORM)` | ↔️ | `Entities + Repositories` | Django ORM intégré vs JPA/Hibernate |
| `settings.py` | ↔️ | `application.yml` | Configuration centralisée vs Fichiers de propriétés |
| `Middleware` | ↔️ | `Filters/Interceptors` | Traitement inter-requêtes vs AOP et filtres servlet |

## Différences Clés

### 🐍 Django - Convention over Configuration

**Philosophie :** "Batteries incluses" - tout est intégré et configuré par défaut

**Caractéristiques :**
- Structure de projet imposée et rigide
- ORM intégré avec migrations automatiques
- Configuration centralisée dans `settings.py`
- Imports directs, pas d'IoC container natif

### ☕ Spring Boot - Configuration par Annotations

**Philosophie :** Auto-configuration intelligente mais flexible

**Caractéristiques :**
- Structure Maven/Gradle plus flexible
- JPA/Hibernate avec configuration explicite
- IoC Container avec injection automatique
- Configuration par annotations et fichiers de propriétés

## Structure des Projets

### Django Structure
```
myproject/
├── myproject/
│   ├── __init__.py
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── myapp/
│   ├── models.py
│   ├── views.py
│   ├── urls.py
│   ├── admin.py
│   └── templates/
│       └── myapp/
├── static/
├── media/
├── requirements.txt
└── manage.py
```

### Spring Boot Structure
```
src/
├── main/
│   ├── java/
│   │   └── com/example/myapp/
│   │       ├── controller/
│   │       │   └── UserController.java
│   │       ├── service/
│   │       │   └── UserService.java
│   │       ├── repository/
│   │       │   └── UserRepository.java
│   │       ├── entity/
│   │       │   └── User.java
│   │       └── Application.java
│   └── resources/
│       ├── application.yml
│       ├── static/
│       └── templates/
├── test/
└── pom.xml (ou build.gradle)
```

## Exemples de Code

### Gestion des Utilisateurs - Django

**models.py**
```python
from django.db import models

class User(models.Model):
    username = models.CharField(max_length=150, unique=True)
    email = models.EmailField()
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.username
```

**views.py**
```python
from django.shortcuts import render
from django.http import JsonResponse
from .models import User

def user_list(request):
    users = User.objects.all()
    return render(request, 'users.html', {'users': users})

def api_users(request):
    users = list(User.objects.values())
    return JsonResponse({'users': users})
```

**urls.py**
```python
from django.urls import path
from . import views

urlpatterns = [
    path('users/', views.user_list, name='user_list'),
    path('api/users/', views.api_users, name='api_users'),
]
```

### Gestion des Utilisateurs - Spring Boot

**Entity - User.java**
```java
@Entity
@Table(name = "users")
public class User {
    @Id
    @GeneratedValue(strategy = GenerationType.IDENTITY)
    private Long id;
    
    @Column(unique = true)
    private String username;
    
    private String email;
    
    @CreationTimestamp
    private LocalDateTime createdAt;
    
    // Getters et Setters
}
```

**Repository - UserRepository.java**
```java
@Repository
public interface UserRepository extends JpaRepository<User, Long> {
    Optional<User> findByUsername(String username);
    List<User> findByEmailContaining(String email);
}
```

**Service - UserService.java**
```java
@Service
public class UserService {
    
    @Autowired
    private UserRepository userRepository;
    
    public List<User> findAll() {
        return userRepository.findAll();
    }
    
    public User findByUsername(String username) {
        return userRepository.findByUsername(username)
            .orElseThrow(() -> new UserNotFoundException("User not found"));
    }
}
```

**Controller - UserController.java**
```java
@RestController
@RequestMapping("/api")
public class UserController {
    
    @Autowired
    private UserService userService;
    
    @GetMapping("/users")
    public List<User> getUsers() {
        return userService.findAll();
    }
    
    @GetMapping("/users/{username}")
    public User getUser(@PathVariable String username) {
        return userService.findByUsername(username);
    }
}
```

### Configuration

**Django - settings.py**
```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'myapp_db',
        'USER': 'myuser',
        'PASSWORD': 'mypassword',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'rest_framework',
    'myapp',
]
```

**Spring Boot - application.yml**
```yaml
server:
  port: 8080

spring:
  datasource:
    url: jdbc:postgresql://localhost:5432/myapp_db
    username: myuser
    password: mypassword
    driver-class-name: org.postgresql.Driver
    
  jpa:
    hibernate:
      ddl-auto: update
    show-sql: true
    database-platform: org.hibernate.dialect.PostgreSQLDialect
    
logging:
  level:
    com.example.myapp: DEBUG
```

### Gestion des Dépendances

**Django - requirements.txt**
```txt
Django==4.2.0
djangorestframework==3.14.0
psycopg2-binary==2.9.5
python-decouple==3.6
```

**Spring Boot - pom.xml (Maven)**
```xml
<dependencies>
    <dependency>
        <groupId>org.springframework.boot</groupId>
        <artifactId>spring-boot-starter-web</artifactId>
    </dependency>
    <dependency>
        <groupId>org.springframework.boot</groupId>
        <artifactId>spring-boot-starter-data-jpa</artifactId>
    </dependency>
    <dependency>
        <groupId>org.postgresql</groupId>
        <artifactId>postgresql</artifactId>
        <scope>runtime</scope>
    </dependency>
</dependencies>
```

## Injection de Dépendances

### Django - Imports Directs
```python
# Pas d'IoC container natif - imports directs
from myapp.models import User
from django.shortcuts import render

def user_list(request):
    users = User.objects.all()  # Accès direct
    return render(request, 'users.html', {'users': users})
```

### Spring Boot - Inversion of Control
```java
// IoC Container avec injection automatique
@RestController
public class UserController {
    
    @Autowired  // Injection automatique
    private UserService userService;
    
    @GetMapping("/users")
    public List<User> getUsers() {
        return userService.findAll();  // Service injecté
    }
}
```

## Points Clés pour la Transition

### 🚀 Ce qui va vous aider

- ✅ **Concepts MVC déjà maîtrisés** - L'architecture reste similaire
- ✅ **Compréhension de l'ORM** - JPA fonctionne comme Django ORM
- ✅ **Gestion des routes et URLs** - Même logique, syntaxe différente
- ✅ **Séparation des responsabilités** - Couches bien définies
- ✅ **Architecture en couches** - Models → Repositories, Views → Controllers

### ⚠️ Nouveaux concepts à apprendre

- 🔄 **Annotations Java** - `@Service`, `@Repository`, `@Controller`, `@Entity`
- 🔧 **Injection de dépendances** - `@Autowired`, `@Component`
- ⚙️ **Configuration YAML** - `application.yml` vs `settings.py`
- 🏗️ **JPA/Hibernate** - Différences avec Django ORM
- 📦 **Maven/Gradle** - Build tools vs pip/requirements
- 🎯 **IoC Container** - Gestion automatique des dépendances

### 💡 Conseils pour débuter

1. **Commencez par les annotations** - Comprenez `@RestController`, `@Service`, `@Repository`
2. **Maîtrisez l'injection de dépendances** - `@Autowired` est partout
3. **Apprenez JPA progressivement** - Beaucoup de similitudes avec Django ORM
4. **Configurez avec application.yml** - Plus flexible que settings.py
5. **Utilisez Spring Boot Initializr** - Équivalent de `django-admin startproject`

### 🛠️ Ressources utiles

- [Spring Boot Documentation](https://docs.spring.io/spring-boot/docs/current/reference/html/)
- [Spring Initializr](https://start.spring.io/) - Générateur de projets
- [Baeldung Spring Tutorials](https://www.baeldung.com/spring-boot)
- [JPA/Hibernate Guide](https://hibernate.org/orm/documentation/)

---

## 🎯 Résumé

En tant que développeur Django, vous avez déjà une excellente base pour apprendre Spring Boot. Les concepts fondamentaux restent les mêmes :

- **Architecture MVC** ✅
- **Séparation des couches** ✅  
- **ORM/Mapping objet-relationnel** ✅
- **Routage et contrôleurs** ✅

Spring Boot ajoute principalement :
- L'**injection de dépendances** automatique
- Une approche **déclarative par annotations**
- Plus de **flexibilité** dans la configuration

La courbe d'apprentissage sera douce car vous maîtrisez déjà les concepts architecturaux !

---