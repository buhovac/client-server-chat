# Client-Server Chat Application

## 1. Présentation du projet
Ce projet a pour objectif de créer une **application client/serveur de type chat**. Le projet doit permettre à plusieurs utilisateurs de communiquer en temps réel via différents salons. L’application est composée de deux parties principales :

- **Serveur** : Gère les connexions clients, la création et la gestion des salons, ainsi que la diffusion des messages.
- **Client** : Permet à l’utilisateur de se connecter au serveur, d’envoyer et de recevoir des messages via une interface graphique.

Le projet sera réalisé en **Python**, utilisant les librairies suivantes :  
- `asyncio` pour la gestion asynchrone des connexions  
- `websockets` pour le transport fiable des messages  
- `tkinter` pour l’interface graphique  
- `json` pour la structuration des messages  

---

## 2. Analyse du travail à faire

### Serveur
- Gestion des connexions et déconnexions clients de manière asynchrone et non bloquante.
- Gestion des **salons** : création, rejoindre, quitter.
- Diffusion des messages à tous les clients d’un salon.
- Gestion des utilisateurs uniques et du salon par défaut.
- Journalisation (logging) des messages et événements.

### Client
- Connexion au serveur en spécifiant IP, port et nom d’utilisateur.
- Affichage des salons actifs et possibilité de changer de salon.
- Envoi et réception de messages dans le salon actif.
- Interface graphique ergonomique et claire.
- Gestion des erreurs côté client (salon inexistant, serveur déconnecté…).

### Protocole JSON
Le serveur et le client communiqueront via un **protocole JSON** structuré comprenant les actions suivantes :
- `create_salon` : créer un nouveau salon  
- `join_salon` : rejoindre un salon existant  
- `leave_salon` : quitter un salon  
- `send_message` : envoyer un message dans le salon actif  
- `receive_message` : recevoir un message du salon  
- `list_salons` : obtenir la liste des salons actifs  

---

## 3. Répartition des tâches pour les 3 membres

| Membre | Rôle principal | Tâches concrètes |
|--------|----------------|-----------------|
| **Membre 1 – Serveur** | Développement serveur et logique centrale | Création serveur asynchrone, gestion des salons, diffusion des messages, gestion des utilisateurs uniques, journalisation. |
| **Membre 2 – Client et interface graphique** | Développement client | Connexion au serveur, interface graphique, gestion des salons et messages, tests côté client. |
| **Membre 3 – Tests, logging et documentation** | Qualité et documentation | Ajout du logging serveur et client, tests unitaires, gestion des erreurs, rédaction de la documentation et rapport final. |

---

## 4. Planning de travail détaillé (Semaine 1 à 4)

### Semaine 1 – Préparation et conception
| Jour | M1 (Serveur) | Temps | M2 (Client) | Temps | M3 (Tests/Doc) | Temps | Objectif commun |
|------|---------------|-------|-------------|-------|----------------|-------|----------------|
| Jour 1 | Analyse cahier des charges côté serveur | 1h | Analyse côté client | 1h | Analyse côté tests/logs et documentation | 1h | Décider langage, protocole et librairies |
| Jour 2 | Définir structure de données salons/clients | 1.5h | Maquettage interface graphique | 1.5h | Définir protocole JSON et plan documentation | 1h | Valider architecture globale et flux messages |
| Jour 3 | Ébauche architecture serveur | 1h | Ébauche architecture client | 1h | Ébauche protocole JSON complet | 1h | Synchroniser architecture serveur-client |
| Jour 4 | Créer dépôt Git côté serveur | 0.5h | Créer dépôt Git côté client | 0.5h | Créer dépôt Git pour docs/tests | 0.5h | Structure projet commune et branches Git |
| Jour 5 | Rédiger mini-doc serveur | 1h | Rédiger mini-doc client | 1h | Documenter protocole JSON et diagrammes | 1.5h | Valider documentation initiale |

### Semaine 2 – Développement serveur/client de base
| Jour | M1 (Serveur) | Temps | M2 (Client) | Temps | M3 (Tests/Doc) | Temps | Objectif commun |
|------|---------------|-------|-------------|-------|----------------|-------|----------------|
| Jour 1 | Serveur asynchrone, gestion connexion clients | 3h | Client asynchrone, test connexion serveur | 3h | Préparer tests de connexion et logs | 2h | Vérifier communication serveur-client minimale |
| Jour 2 | Gestion salons : création, salon par défaut | 3h | Affichage liste salons côté client | 2h | Préparer tests salons côté serveur-client | 2h | Vérifier cohérence salon initial |
| Jour 3 | Implémenter rejoindre/quitter salon | 3h | Gestion changement salon côté client | 3h | Tests de changement de salon | 2h | Tester échange salons et messages |
| Jour 4 | Envoi/réception messages JSON, diffusion salon | 3h | Envoi/réception messages côté client | 3h | Tests messages, logs messages | 2h | Vérifier échanges messages corrects |
| Jour 5 | Logging serveur complet | 2h | Logging client | 2h | Vérification logs, tests unitaires basiques | 3h | Tests finaux semaine 2 |

### Semaine 3 – Interface client + robustesse serveur
| Jour | M1 (Serveur) | Temps | M2 (Client) | Temps | M3 (Tests/Doc) | Temps | Objectif commun |
|------|---------------|-------|-------------|-------|----------------|-------|----------------|
| Jour 1 | Gestion erreurs serveur | 3h | Améliorer interface graphique | 3h | Tests robustesse serveur-client | 2h | Vérifier stabilité et non blocage |
| Jour 2 | Optimisation asynchronisme serveur | 2h | Affichage dynamique messages | 3h | Tests robustesse client | 2h | Vérifier fluidité communication et GUI |
| Jour 3 | Préparer structure tests unitaires serveur | 2h | Préparer structure tests unitaires client | 2h | Début rédaction documentation | 2h | Tests unitaires côté serveur et client |
| Jour 4 | Tests serveur avec clients simulés | 3h | Tests client avec plusieurs salons/messages | 3h | Identifier et corriger bugs | 2h | Debug complet et validation fonctionnalités |
| Jour 5 | Finalisation serveur stable | 2h | Finalisation interface client ergonomique | 3h | Vérification finale des logs et documentation | 2h | Test complet serveur + clients |

### Semaine 4 – Finitions et rapport
| Jour | M1 (Serveur) | Temps | M2 (Client) | Temps | M3 (Tests/Doc) | Temps | Objectif commun |
|------|---------------|-------|-------------|-------|----------------|-------|----------------|
| Jour 1 | Tests finaux serveur + logs complets | 2h | Tests finaux client GUI + messages | 3h | Vérification protocoles JSON et logs | 2h | Vérification complète fonctionnalité |
| Jour 2 | Optimisation code serveur | 2h | Optimisation code client | 3h | Vérification documentation et diagrammes | 2h | Préparer rendu final stable |
| Jour 3 | Rédaction partie serveur rapport | 2h | Rédaction partie client rapport | 2h | Consolidation documentation, annexes | 3h | Préparer première version du rapport |
| Jour 4 | Ajouter annexes serveur | 1h | Ajouter annexes client | 1h | Ajouter annexes protocole JSON et tests | 2h | Compiler rapport final |
| Jour 5 | Relecture et corrections serveur | 1h | Relecture et corrections client | 1h | Relecture documentation complète | 2h | Préparer rendu final et dépôt Git complet |

---

## 5. Notes importantes
- Chaque jour, il est conseillé de faire un **point rapide (10-15 min)** pour synchroniser le groupe.  
- Utiliser des branches Git pour chaque membre et merge régulier pour éviter les conflits.  
- Commencer par un **prototype console minimal** avant de passer à l’interface graphique et la journalisation complète.  
