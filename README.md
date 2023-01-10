Note: The present project is the thirteenth one of the training course *Python Application Developer*, offered by OpenClassRooms and aims to *Scale a Django application using a modular architecture*.
The main goals of the project are to:
- Reduce various technical liabilities on the project;
- Redesign the modular architecture
- Add a CI/CD pipeline using CircleCI and Heroku
- Monitor the application and track errors via Sentry
The present README was originally writen by the OpenClassRooms school; only the "Deployment" section was written by the student.

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

## Déploiement

### Récapitulatif haut niveau du fonctionnement du déploiement

Le déploiement du code et de son environnement (sous forme d'une image Docker) sur Heroku est automatisé via le pipeline circleCI, décrit dans le fichier config.yml.
Ce déploiement automatique se fait lorsque le code modifié est "push" vers github (branche master, uniquement)

Le déploiement peut également se faire manuellement (voir texte ci-dessous)

### Configuration requise pour le déploiement

Pour un déploiement manuel :
- Un compte Docker
- docker CLI installée
- Un compte heroku et une application Heroku
- heroku CLI installée (sinon remplacez la commande `heroku container:login` par `docker login --username=$HEROKU_USERNAME --password=$($HEROKU_API_KEY) registry.heroku.com`) lors de l'authentification pour le déploiement
- Un compte circleCI

### Étapes nécessaires au déploiement

- Dans les parametres du projet circleCI, configurez les variables d'envionnement (project settings/environment variables) suivantes:
  - $DOCKERHUB_USERNAME : le nom d'utilisateur de votre compte dockerhub
  - $DOCKERHUB_PASSWORD : votre mot de passe DockerHub
  - $HEROKU_USERNAME : le nom d'utilisateur de votre compte heroku
  - $HEROKU_API_KEY : votre token Heroku, vous pouvez l'obtenir avec la commande `heroku auth:token`
  - $HEROKU_APP_NAME : le nom de votre application heroku
  - $DJANGO_APP_DOCKER_IMAGE_NAME : le nom que vous souhaitez donner à votre image docker

Dans le terminal, executez les commandes suivantes :
- Créez une image Docker avec la commande `docker build -t NOM_IMAGE .` (n'oubliez pas le point en fin de commande)
- optionnel : vous pouvez tester le bon fonctionnement de l'application en local avec la commande `docker run --publish 8000:8000 NOM_IMAGE:latest`, l'adresse à visiter devrait s'afficher dans votre terminal
- Authentifiez vous avec `heroku container:login`
- `docker build -t registry.heroku.com/NOM_APPLICATION_HEROKU/web .` (n'oubliez pas le point en fin de commande)
- `docker push registry.heroku.com/NOM_APPLICATION_HEROKU/web`
- `heroku container:release web -a NOM_APPLICATION_HEROKU`
- optionnel : vous pouvez tester le bon fonctionnement de l'application déployée avec : `heroku open`
