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

Le déploiement du code et de son environnement (Docker) sur Heroku est automatisé via le pipeline circleCI, qui est exécuté lors d'un push sur GitHub (branche master, uniquement). Le pipeline circleCI est décrit dans le fichier config.yml.

Le déploiement peut également se faire manuellement (voir texte ci-dessous)

### Configuration requise pour le déploiement

Pour un déploiement manuel :
- Un compte Docker
- Docker CLI installée
- Un compte heroku et une application Heroku
- Heroku CLI installée (sinon remplacez la commande `heroku container:login` par `docker login --username=$HEROKU_USERNAME --password=$($HEROKU_API_KEY) registry.heroku.com`) lors de l'authentification pour le déploiement
- Un compte circleCI

### Étapes nécessaires au déploiement

- Dans les parametres du projet circleCI, configurez les variables d'envionnement (project settings/environment variables) suivantes:
  - $DOCKERHUB_USERNAME : le nom d'utilisateur de votre compte DockerHub
  - $DOCKERHUB_PASSWORD : votre mot de passe DockerHub
  - $HEROKU_USERNAME : le nom d'utilisateur de votre compte Heroku
  - $HEROKU_API_KEY : votre token Heroku, vous pouvez l'obtenir avec la commande `heroku auth:token`
  - $HEROKU_APP_NAME : le nom de votre application Heroku (que vous pouvez créer avec `heroku create`)
  - $DJANGO_APP_DOCKER_IMAGE_NAME : le nom que vous souhaitez donner à votre image Docker

Avec le terminal, placez vous dans le dossier du projet (commande `cd`), puis executez les commandes suivantes :
- Créez une image Docker avec la commande `docker build -t NOM_IMAGE .` (n'oubliez pas le point en fin de commande)
- optionnel : vous pouvez tester le bon fonctionnement de l'application en local avec la commande `docker run --publish 8000:8000 NOM_IMAGE:latest`, l'adresse à visiter devrait s'afficher dans votre terminal
- Authentifiez vous avec `heroku container:login` (ou avec `heroku auth:token`, vous obtiendrez alors un TOKEN que vous pourrez utiliser avec la commande `docker login --username=YOUR_USERNAME --password=${YOUR_TOKEN} registry.heroku.com`)

- Pour un premier déploiement mannuel :
  - `heroku create` (si vous n'avez pas encore d'application Heroku)
  - `heroku container:push web –app ${YOUR_APP_NAME}`
  - `heroku container:release web -a nom_app_blooming_inlet_72637`

- Pour le déploiement d'une mise à jour mannuel :
  - `docker build -t registry.heroku.com/NOM_APPLICATION_HEROKU/web .` (n'oubliez pas le point en fin de commande)
  - `docker push registry.heroku.com/NOM_APPLICATION_HEROKU/web`
  - `heroku container:release web -a NOM_APPLICATION_HEROKU`
  - optionnel : vous pouvez tester le bon fonctionnement de l'application déployée avec : `heroku open`

Si l'authentification heroku pose problème : 
-Placez vous dans le dossier de l’application avec le terminal 
-`heroku login`
-vous obtenez un nouveau token heroku avec `heroku auth:token`, que vous pouvez utiliser comme variable d'environnement $HEROKU_API_KEY 

### Journalisation sentry

La journalisation a été mise en place avec la documentation sentry appropriée pour un projet Django et disponible à l'adresse suivante : https://docs.sentry.io/platforms/python/guides/django/ .

Les étapes à suivre sont : 
- créer un compte [sentry](https://sentry.io/signup/)
- sentry-sdk est déja installé dans l'environnement virtuel du projet
- créer un projet sentry, selectionner le framework Django
- le DSN vous est fourni, vous pouvez le communiquer dans le settings.py (sentry_sdk.init(dsn="NOUVEAU_DSN"))
- vous avez accès aux services de sentry pour le présent projet, pour vérifier cela, rendez vous à l'url NOM_APPLICATION_HEROKU.herokuapp.com/sentry-debug/
- une nouvelle erreur (division par zéro) devrait vous etre signalée au niveau du tableau de bord sentry (sentry.io)
