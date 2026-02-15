# Roadmap : Transition vers iLôt

Ce document trace la route pour transformer le gestionnaire de tâches actuel en la plateforme de sécurisation foncière **iLôt**.

## Phase 1 : Refonte du Modèle Utilisateur (Priorité Haute)
- [ ] Ajouter le champ `phoneNumber` à `AppUser` (clé de voûte pour l'accès local).
- [ ] Implémenter le choix du type de profil à l'inscription (Acheteur, Vendeur, Propriétaire, Notaire).
- [ ] Intégrer Lombok pour simplifier les entités.

## Phase 2 : Module de Vérification de Titres (MVP)
- [ ] Créer l'entité `LandTitle` (Numéro, Propriétaire, Localisation, Statut).
- [ ] Développer le service de vérification (simulation d'OCR et appel API e-foncier).
- [ ] Créer l'interface de scan et d'affichage des résultats.

## Phase 3 : Marketplace Foncière
- [ ] Créer l'entité `Ad` (Annonce) liée à un `LandTitle`.
- [ ] Implémenter la recherche avec filtres (Budget, Surface, Localisation).
- [ ] Gérer l'upload de photos pour les terrains.

## Phase 4 : Sécurisation et Services Avancés
- [ ] Implémenter le système de messagerie interne.
- [ ] Intégrer un système de paiement séquestre (Escrow).
- [ ] Ajouter le Chatbot IA pour le conseil juridique.

## Phase 5 : Optimisation UX/UI
- [ ] Appliquer les designs premium décrits dans `ilot_foncier_ux5.md`.
- [ ] Ajouter les micro-animations et le mode sombre.
