# Flask Boilerplate

**La consigne du projet se trouve dans [ASSIGNMENT.md](ASSIGNMENT.md).**

Un projet Flask simple avec une structure de base.

## Installation

Installez [uv](https://docs.astral.sh/uv/getting-started/installation/) avec la commande correspondant à votre système.

Sous Windows, dans PowerShell, exécutez la commande suivante.

```powershell
powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/install.ps1 | iex"
```

Sous macOS, Linux ou WSL, utilisez le terminal de votre environnement.

```sh
curl -LsSf https://astral.sh/uv/install.sh | sh
```

Fermez et rouvrez le terminal, puis vérifiez l'installation avec `uv --version`.

Ouvrez le dossier du projet dans VS Code. Depuis le terminal de ce dossier, préparez l'environnement.

```sh
uv sync
```

Le projet requiert Python 3.12 ou une version ultérieure. Le fichier `.python-version` sélectionne Python 3.12 par défaut. Uv installe si nécessaire Python et crée l'environnement `.venv` à partir de `pyproject.toml` et `uv.lock`.

Sous WSL, installez uv et exécutez ces commandes dans le terminal Linux. Pour ouvrir le projet dans VS Code connecté à WSL, utilisez `code .` avec l'extension WSL installée.

Dans VS Code, utilisez **Python: Select Interpreter** pour sélectionner le Python de `.venv` si nécessaire.

## Lancement

Depuis le dossier du projet, lancez le serveur de développement.

```sh
uv run flask --app app run --debug
```

Ouvrez http://127.0.0.1:5000/ dans votre navigateur. Le mode debug relance le serveur après une modification du code Python. Actualisez la page pour observer les changements.

Pour arrêter le serveur, utilisez `Ctrl + C` dans le terminal.

Toutes les dépendances nécessaires au boilerplate sont déclarées dans `pyproject.toml` et verrouillées dans `uv.lock`. La commande `uv sync` prépare le projet.

## Aides

### Structure du Projet

L'architecture du projet reprend le modèle MVC (Modèle-Vue-Contrôleur) de base :
- Modèle:
  - `models/` : Contient les modèles de données.
- Vue:
  - `templates/` : Contient les templates HTML pour le rendu des pages.
  - `static/` : Contient les fichiers statiques comme le CSS, JavaScript et les images.
- Contrôleur:
  - `app.py` : Point d'entrée de l'application Flask.
    - Ce fichier gère les routes et la logique de l'application.
  - `database.sql` : Script SQL pour initialiser la base de données.
  - `controllers/` : Contient l'intéraction avec la base de données et la logique métier.


La structure finale du projet sera :
```
.
├── controllers/
│   └── user_controller.py
├── models/
│   └── user.py
├── static/
│   └── styles.css
├── templates/
│   ├── layout.html
│   └── index.html
├── .gitignore
├── app.py
├── README.md
├── database.sql
├── .python-version
├── pyproject.toml
├── uv.lock
└── sql.py
```

### Base de Données

La base de données est initialisée à partir du fichier `database.sql` lors du premier lancement de l'application. Ce fichier contient les instructions SQL nécessaires pour créer les tables requises.

Dans le cas où la base de données n'existe pas, elle est créée automatiquement et le script SQL est exécuté pour configurer les tables.

Après une modification de `database.sql`, une base existante conserve son ancien schéma. Pendant le développement, pour repartir des données initiales, arrêtez le serveur, sauvegardez les données utiles, supprimez `database.db`, puis relancez l'application. Cette opération recrée la base et efface les données précédentes.

#### Compte administrateur

Lors de l'initialisation de la base de données, un compte de démonstration nommé `admin` est créé avec les informations suivantes.
- **Nom d'utilisateur** : `admin`
- **Mot de passe** : `adminpassword`

Le compte `admin` doit disposer du rôle administrateur dans votre application. Complétez le schéma et l'initialisation pour lui attribuer ce rôle, puis protégez les routes d'administration. Conservez les identifiants ci-dessus pour permettre l'évaluation du projet.

Le code correspondant se trouve dans `app.py` et utilise la fonction `generate_password_hash` de `werkzeug.security` pour stocker le mot de passe de manière sécurisée.

```python
admin_user = User("admin", generate_password_hash("adminpassword"))
db.execute("INSERT INTO users (username, password_hash) VALUES (?, ?)", admin_user.login, admin_user.password_hash)
```

Il est bon de s'en inspirer pour créer d'autres utilisateurs ou d'autres tables dans la base de données.
