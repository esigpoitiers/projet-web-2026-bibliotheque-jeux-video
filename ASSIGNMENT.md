# Projet 2026 — Bibliothèque de jeux vidéo

Ce projet consiste en une application web permettant aux utilisateurs de gérer leur bibliothèque de jeux vidéo, de suivre leur progression et de donner leur avis sur les jeux.

L'application comporte un catalogue commun de jeux. Chaque utilisateur peut ajouter des jeux de ce catalogue à sa bibliothèque personnelle et renseigner un statut, une note et un commentaire.

## Fonctionnalités Requises

Ces fonctionnalités constituent le cœur de l'application et doivent être implémentées en priorité.

### Authentification

Les utilisateurs doivent pouvoir créer un compte et se connecter de manière sécurisée.

- Login/Logout avec sessions
- Inscription de nouveaux utilisateurs
- Page de profil utilisateur et consultation de sa bibliothèque
- Choix entre un profil public et un profil privé
- Consultation des profils publics des autres utilisateurs
- Support d’un rôle administrateur
- Protection des pages et des actions nécessitant une connexion

Chaque utilisateur peut modifier uniquement les informations de sa propre bibliothèque. Les autorisations doivent être vérifiées côté serveur. Un profil public permet de consulter la bibliothèque de son utilisateur. Un profil privé et sa bibliothèque sont accessibles uniquement à leur propriétaire.

### Catalogue de Jeux

Chaque jeu possède au minimum les informations suivantes.

- Titre
- Description
- Image renseignée par une URL
- Une plateforme principale choisie dans une liste fixe (PC, PlayStation, Xbox, Nintendo Switch)

Les utilisateurs peuvent consulter le catalogue et rechercher un jeu par son titre. Cliquer sur un jeu ouvre sa page de détail, qui présente ses informations et permet de l'ajouter à sa bibliothèque.

Un utilisateur connecté peut créer un jeu dans le catalogue avec un formulaire contenant le titre, la description, l'URL de l'image et la plateforme principale. Vous pouvez reprendre le fonctionnement du formulaire Birthdays pour la saisie, la validation et l'insertion en base. La liste des plateformes peut être définie directement dans l'application.

La page de détail du jeu affiche également les autres comptes publics qui ont ajouté ce jeu à leur bibliothèque, quel que soit son statut. Chaque compte affiché comporte un lien vers sa page de profil. Les comptes privés doivent être exclus de cette liste et des données renvoyées par les routes correspondantes.

Les images peuvent notamment provenir de [SteamGridDB](https://www.steamgriddb.com/). Renseignez l'URL directe de l'image et conservez un lien vers sa page source pour en identifier la provenance.

### Bibliothèque Personnelle

Un utilisateur connecté peut ajouter un jeu à sa bibliothèque, modifier son suivi et le retirer de sa bibliothèque.

L'application doit permettre de renseigner les informations suivantes pour chaque jeu ajouté. L'utilisateur peut laisser la note et le commentaire vides.

- Un statut parmi « Liste de souhaits », « Pas commencé », « En cours » et « Terminé »
- Une note facultative, sous la forme d'un entier de 1 à 5
- Un commentaire personnel facultatif

Un jeu apparaît au maximum une fois dans la bibliothèque d'un utilisateur. Deux utilisateurs peuvent avoir des statuts, notes et commentaires différents pour le même jeu.

L'utilisateur doit pouvoir filtrer sa bibliothèque par statut. La note et le commentaire peuvent être enregistrés avec un formulaire classique suivi d'une redirection.

### Administration du Catalogue

Le catalogue étant partagé entre les utilisateurs, un administrateur doit pouvoir corriger les informations des jeux.

Une page d'administration permet de consulter la liste des jeux et d'accéder à leur formulaire de modification. Celui-ci permet de modifier le titre, la description, l'URL de l'image et la plateforme. Vous pouvez réutiliser le formulaire de création en le préremplissant avec les informations du jeu.

L'accès à cette page et les opérations de modification sont réservés aux administrateurs. Les droits doivent être vérifiés côté serveur pour chaque route concernée.

Le compte `admin` doit disposer du rôle administrateur. Respectez les identifiants déjà fournis dans le README du boilerplate, avec le nom d'utilisateur `admin` et le mot de passe `adminpassword`. Ce compte doit être disponible après l'initialisation de la base.

### Interactivité

Le changement du statut d'un jeu dans sa bibliothèque doit fonctionner sans rechargement complet de la page, à l'aide d'une requête `fetch()` vers une route Flask.

Les échanges de données avec cette route utilisent JSON. Choisissez la méthode HTTP et les codes de réponse adaptés à cette opération.

L'interface doit afficher le résultat après confirmation du serveur et présenter un message compréhensible en cas d'erreur.

## Compétences Techniques à Démontrer

Durant ce projet, vous devrez démontrer votre maîtrise des composants suivants.

### HTML/Formulaires

- Création de formulaires statiques HTML (login, inscription, ajout de jeu)
- Validation native des champs (required, pattern, etc.)
- Structure sémantique des pages

### JavaScript/Interactivité

- Formulaires réagissant aux actions de l’utilisateur, notamment le changement de statut
- Mise à jour de la page après une réponse du serveur (statut, et éventuellement note et commentaire)
- Manipulation du DOM pour l'interface utilisateur
- Requêtes asynchrones avec `fetch()` (AJAX), avec échange de données JSON

### Python/Flask

- Gestion des routes et des contrôleurs
- Manipulation des sessions utilisateur
- Création d'API RESTful
- Intégration avec la base de données
- Protection des routes avec des décorateurs

### Base de Données

- Conception du schéma relationnel
- Création des tables et relations
- Requêtes SQL pour la manipulation des données
- Gestion des transactions

Le boilerplate fournit un fichier `database.sql` contenant la table des utilisateurs et crée automatiquement `database.db` au premier lancement. Complétez le script SQL avec les tables et relations nécessaires au projet, en distinguant les informations communes aux jeux et le suivi personnel de chaque utilisateur.

## Fonctionnalités Facultatives

Après avoir terminé les fonctionnalités requises, vous pouvez enrichir votre application.

- Suppression des jeux par un administrateur, en gérant leurs références dans les bibliothèques
- Gestion de plusieurs plateformes par jeu et choix de la plateforme dans sa bibliothèque
- Administration de la liste des plateformes
- Filtres par plateforme
- Modification de la note et du commentaire avec `fetch()` sans rechargement complet de la page
- Upload d'images avec validation des fichiers
- Import d'informations depuis une API de jeux vidéo
- Affichage d'une note moyenne par jeu
- Tri par titre, note ou date d'ajout
- Statistiques personnelles sur les jeux suivis et terminés
- Statut supplémentaire « Abandonné »
- Dates de début et de fin de jeu
- Images de profil personnalisées
- Préférences utilisateur (thème, paramètres de confidentialité)

## Rendu

Le projet doit être remis dans un dépôt GitHub privé. Ajoutez l'enseignant comme collaborateur et déposez l'URL du dépôt sur ENT.

Le dépôt contient les éléments nécessaires pour installer et lancer l'application.

- Code source et ressources
- Fichiers `pyproject.toml` et `uv.lock`
- Script d'initialisation de la base de données
- Données de démonstration permettant de tester les fonctionnalités
- Un fichier `README.md` décrivant l'installation, le lancement, les comptes de démonstration et les fonctionnalités réalisées

Le README doit notamment expliquer comment lancer le projet avec uv.

Les environnements virtuels, fichiers de session, caches et secrets doivent être exclus du dépôt.

L'historique Git doit permettre de suivre la progression du travail.
