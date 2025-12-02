# Client-Server Chat Application

## 1. Présentation du projet
Ce projet a pour objectif de créer une **application client/serveur de type chat**. Le projet permet à plusieurs utilisateurs de communiquer en temps réel via différents salons. L’application est composée de deux parties principales :

- **Serveur** : Gère les connexions clients, la création et la gestion des salons, ainsi que la diffusion des messages.
- **Client** : Permet à l’utilisateur de se connecter au serveur, d’envoyer et de recevoir des messages via une interface graphique.

Le projet est développé en **Python**, utilisant les librairies suivantes :  
- `asyncio` pour la gestion asynchrone  
- `websockets` pour le transport fiable des messages  
- `tkinter` pour l’interface graphique  
- `json` pour structurer les messages  

---

## 2. Extended Description

Cette application est un projet pédagogique de type **client/serveur de chat**, développé en Python par un trinôme. L’objectif principal est de créer une plateforme permettant à plusieurs utilisateurs de communiquer en temps réel dans différents salons, tout en appliquant les principes de la programmation asynchrone, de la communication réseau fiable et de la conception d’interfaces graphiques ergonomiques.  

### Objectifs détaillés
- Permettre aux utilisateurs de se connecter à un serveur central et d’échanger des messages en temps réel.  
- Créer et gérer dynamiquement plusieurs salons de discussion.  
- Assurer que chaque utilisateur est unique et qu’il n’est présent que dans un salon à la fois.  
- Fournir un système de journalisation pour tracer les événements importants côté serveur et client.  
- Développer une interface graphique claire, ergonomique et réactive pour le client.  

### Fonctionnalités
- Gestion des salons : création, rejoindre, quitter, salon par défaut initial.  
- Communication en temps réel : envoi et réception de messages JSON structurés.  
- Interface graphique client : affichage des salons actifs, messages du salon actif, zone de saisie pour l’envoi de messages.  
- Asynchronisme : gestion non bloquante des connexions multiples côté serveur et client.  
- Logging : traçabilité des messages et événements importants pour faciliter les tests et le débogage.  

### Architecture
- **Serveur** : responsable des connexions clients, de la gestion des salons, de la diffusion des messages et de la journalisation.  
- **Client** : permet à l’utilisateur de se connecter au serveur, de sélectionner un salon actif, d’envoyer et recevoir des messages via une interface graphique.  
- **Protocole JSON** : toutes les actions entre le client et le serveur sont structurées via JSON, incluant `create_salon`, `join_salon`, `leave_salon`, `send_message`, `receive_message`, et `list_salons`.  

### Technologies et librairies
- Python 3.x  
- `asyncio`  
- `websockets`  
- `tkinter`  
- `json`  

### Cas d’usage
1. L’utilisateur démarre le client, saisit son nom d’utilisateur et se connecte au serveur.  
2. Le client récupère la liste des salons disponibles et rejoint le salon de son choix.  
3. L’utilisateur peut envoyer des messages qui seront diffusés à tous les clients présents dans le même salon.  
4. L’utilisateur peut quitter un salon et rejoindre un autre salon à tout moment, tout en respectant la règle d’un seul salon actif par utilisateur.  

---

## 3. Répartition des tâches

| Membre | Rôle principal | Tâches concrètes |
|--------|----------------|-----------------|
| **Marko Buhovac** | Serveur | Développement serveur asynchrone, gestion des salons, diffusion des messages, journalisation, gestion des utilisateurs uniques. |
| **Jonathan Pauwels** | Client | Développement client et interface graphique, gestion des salons et messages côté client, tests côté client. |
| **Adel** | Tests et documentation | Ajout du logging serveur et client, tests unitaires, gestion des erreurs, rédaction de la documentation et rapport final. |

---

## 4. Planning condensé (02/12 – 16/12)

### Semaine 1 : 02/12 – 08/12 → Conception + Prototype minimal

| Jour | M1 (Marko - Serveur) | M2 (Jonathan - Client) | M3 (Adel - Tests/Doc) | Objectif commun |
|------|---------------------|-----------------------|----------------------|----------------|
| 02/12 | Analyse cahier des charges, définir structure serveur | Analyse cahier des charges, maquette interface client | Analyse tests/logs, définir protocole JSON | Décider architecture, protocoles et librairies |
| 03/12 | Ébauche serveur asynchrone, salon par défaut | Client asynchrone minimal, connexion serveur | Rédaction protocole JSON, plan documentation | Valider communication serveur-client de base |
| 04/12 | Implémenter rejoindre/quitter salon | Affichage liste salons côté client | Tests salons côté serveur-client | Prototype minimal fonctionnel pour un salon |
| 05/12 | Envoi/réception messages JSON | Envoi/réception messages côté client | Tests messages, logging basique | Communication messages fonctionnelle |
| 06/12 | Gestion erreurs serveur | Gestion erreurs côté client | Tests robustesse, correction bugs | Prototype serveur-client stable |
| 07/12 | Logging complet serveur | Logging client | Vérification logs et documentation | Journaux fonctionnels, test complet |
| 08/12 | Optimisation code serveur | Optimisation code client | Consolidation documentation | Prototype prêt pour test multi-utilisateurs |

---

### Semaine 2 : 09/12 – 16/12 → Finalisation, GUI avancée, tests et rapport

| Jour | M1 (Marko - Serveur) | M2 (Jonathan - Client) | M3 (Adel - Tests/Doc) | Objectif commun |
|------|---------------------|-----------------------|----------------------|----------------|
| 09/12 | Tests serveur avec clients simulés | Tests interface client et messages | Début rédaction documentation | Débogage et validation fonctionnalités |
| 10/12 | Optimisation serveur | Amélioration interface GUI | Tests robustesse client/serveur | GUI fluide, serveur stable |
| 11/12 | Préparer structure tests unitaires serveur | Préparer tests unitaires client | Début rédaction rapport et annexes | Tests automatisés côté serveur et client |
| 12/12 | Tests multi-salons serveur | Tests multi-salons client | Correction bugs, tests finaux | Validation multi-salons et échanges messages |
| 13/12 | Finalisation serveur | Finalisation GUI client | Rédaction protocole JSON et annexes | Préparer version finale code + documentation |
| 14/12 | Vérification serveur complet | Vérification client complet | Vérification documentation complète | Validation finale, correction dernières erreurs |
| 15/12 | Optimisation finale serveur | Optimisation finale client | Relecture rapport et README | Projet prêt pour dépôt Git |
| 16/12 | Révision finale + push final sur GitHub | Révision finale + push final sur GitHub | Compilation rapport final | Livraison du projet |

---

## 5. Notes importantes
- Chaque jour, faire un **point rapide (10-15 min)** pour synchroniser le groupe.  
- Utiliser des branches Git individuelles pour chaque membre et merge quotidien pour éviter conflits.  
- Commencer par un **prototype console minimal** avant de passer à l’interface graphique et à la journalisation complète.
