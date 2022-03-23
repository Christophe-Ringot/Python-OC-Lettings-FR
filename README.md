## Résumé

Site web d'Orange County Lettings

## Développement local

### Prérequis

- Compte GitHub avec accès en lecture à ce repository
- Git CLI
- SQLite3 CLI
- Interpréteur Python, version 3.6 ou supérieure

Dans le reste de la documentation sur le développement local, il est supposé que la commande `python` de votre OS shell exécute l'interpréteur Python ci-dessus (à moins qu'un environnement virtuel ne soit activé).

### macOS / Linux

#### Cloner le repository

- `cd /path/to/put/project/in`
- `git clone https://github.com/OpenClassrooms-Student-Center/Python-OC-Lettings-FR.git`

#### Créer l'environnement virtuel

- `cd /path/to/Python-OC-Lettings-FR`
- `python -m venv venv`
- `apt-get install python3-venv` (Si l'étape précédente comporte des erreurs avec un paquet non trouvé sur Ubuntu)
- Activer l'environnement `source venv/bin/activate`
- Confirmer que la commande `python` exécute l'interpréteur Python dans l'environnement virtuel
`which python`
- Confirmer que la version de l'interpréteur Python est la version 3.6 ou supérieure `python --version`
- Confirmer que la commande `pip` exécute l'exécutable pip dans l'environnement virtuel, `which pip`
- Pour désactiver l'environnement, `deactivate`

#### Exécuter le site

- `cd /path/to/Python-OC-Lettings-FR`
- `source venv/bin/activate`
- `pip install --requirement requirements.txt`
- `python manage.py runserver`
- Aller sur `http://localhost:8000` dans un navigateur.
- Confirmer que le site fonctionne et qu'il est possible de naviguer (vous devriez voir plusieurs profils et locations).

#### Linting

- `cd /path/to/Python-OC-Lettings-FR`
- `source venv/bin/activate`
- `flake8`

#### Tests unitaires

- `cd /path/to/Python-OC-Lettings-FR`
- `source venv/bin/activate`
- `pytest`

#### Base de données

- `cd /path/to/Python-OC-Lettings-FR`
- Ouvrir une session shell `sqlite3`
- Se connecter à la base de données `.open oc-lettings-site.sqlite3`
- Afficher les tables dans la base de données `.tables`
- Afficher les colonnes dans le tableau des profils, `pragma table_info(Python-OC-Lettings-FR_profile);`
- Lancer une requête sur la table des profils, `select user_id, favorite_city from
  Python-OC-Lettings-FR_profile where favorite_city like 'B%';`
- `.quit` pour quitter

#### Panel d'administration

- Aller sur `http://localhost:8000/admin`
- Connectez-vous avec l'utilisateur `admin`, mot de passe `Abc1234!`

### Windows

Utilisation de PowerShell, comme ci-dessus sauf :

- Pour activer l'environnement virtuel, `.\venv\Scripts\Activate.ps1` 
- Remplacer `which <my-command>` par `(Get-Command <my-command>).Path`

### comment deployer l'application :

1 - Dockerhub

    - Se connecter à Docker
    - créer un dépôt et lui donner un nom. (projet_13)

2 - Heroku

    - Se connecter à Heroku
    - créer une nouvelle application. (oc-lettings-cr)

3 - Sentry

    - Se connecter à Sentry
    - créer un nouveau projet avec la plateforme django

4 - CircleCI

    - Se connecter sur circleCI avec Github
    - Choisir notre projet et cliquer sur Set up Project
    - dans les option de notre projet, ajouter les variables d'environnement suivant:
    
      - DJANGO_SECRET_KEY -> Clef django
      
      - DJANGO_SETTINGS_MODULE -> Fichier de settings à utiliser
      
      - HEROKU_APP_NAME -> Nom de votre appli sous heroku
      
      - HEROKU_TOKEN -> Token d'identification Heroku
      
      - HUB_NAME -> Le nom de votre compte Dockerhub
      
      - HUB_PSWD -> Votre mot de passe ou token Dockerhub
      
      - SENTRY_NAME -> Token Sentry

### Exécuter l'image docker en local 

 - docker pull christopheringot/projet_13:"tag"
 - docker run --env-file .env -p 8000:8000 -e PORT=8000 -it christopheringot/projet_13:"tag"

tag = dernier tag affiché sur docker hub

il est nécessaire de créer un ficher .env contenant les variables d'environnement suivantes :
    - SECRET_KEY (votre clef django)
    - SENTRY_DSN (Le DSN de la config sentry)

vous pouvez désormais vous rendre sur l'adresse suivante : http://127.0.0.1:8000/
