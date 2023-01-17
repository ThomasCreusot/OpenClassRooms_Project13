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
- Un compte Heroku
- Heroku CLI installée
- Un compte circleCI

### Étapes nécessaires au déploiement d'une nouvelle application heroku

Avec le terminal, placez vous dans le dossier du projet (commande `cd`), puis executez les commandes suivantes :
- Créez une image Docker (n'oubliez pas le point en fin de commande) :
>`docker build -t NOM_IMAGE .`

- optionnel : vous pouvez tester le bon fonctionnement de l'image en local avec la commande suivante; l'adresse à visiter devrait s'afficher dans votre terminal. Vous pouvez ensuite arreter le conteneur correspondant (avec Docker Desktop par exemple):
>`docker run --publish 8000:8000 NOM_IMAGE:latest`

- Pensez à mettre à jour la variable d'environnement DJANGO_APP_DOCKER_IMAGE_NAME dans les parametres du projet sur circleCI si vous l'avez déja créé

- Authentifiez vous (en remplaçant $DOCKERHUB_USERNAME et $DOCKERHUB_PASSWORD par leurs valeurs respectives) :
>`docker login --username $DOCKERHUB_USERNAME --password $DOCKERHUB_PASSWORD`
- Taguez l'image et poussez la vers DockerHub :
>`docker tag $DJANGO_APP_DOCKER_IMAGE_NAME:latest $DOCKERHUB_USERNAME/$DJANGO_APP_DOCKER_IMAGE_NAME:latest`
>`docker push $DOCKERHUB_USERNAME/$DJANGO_APP_DOCKER_IMAGE_NAME:latest`

- Authentifiez vous 
>`heroku container:login`
- Créez une application heroku (vous obtiendrez un nom généré aléatoirement pour cette application; la notation NOM_APP_HEROKU sera utilisée par la suite)
>`heroku create`
- Assurez vous d'être sur le bon "git remote" (les git remotes sont des versions de votre repository sur d'autres serveurs)
>`heroku git:remote -a NOM_APP_HEROKU`

- Vous pouvez désormais ajouter vos variables d’environnement sur heroku (partie settings/config vars de votre application) : ajoutez les variables SECRET_KEY et SENTRY_DSN :
- clé SECRET_KEY : demandez la au responsable de l'application
- clé SENTRY_DSN : voir partie "Journalisation sentry"  du présent document

- Renommez l'application :
>`heroku apps:rename NOUVEAU_NOM_APP_HEROKU --app ANCIEN_NOM_APP_HEROKU`
>`git remote rm heroku`
>`heroku git:remote -a NOUVEAU_NOM_APP_HEROKU`
- Si vous choisissez un autre nom d'application que celui prévu par le dévelopeur originel, pensez à mettre à jour ALLOWED_HOST dans settings.py, ainsi que variable d’environnement HEROKU_APP_NAME sur circleCI si vous avez déja associé votre projet à cette plateforme

- Authentifiez vous 
>`docker login --username=_ --password=${YOUR_TOKEN} registry.heroku.com`
- Procédez à la finalisation du déploiement :
>`heroku container:push web --app NOM_APP_HEROKU`
>`heroku container:release web -a NOM_APP_HEROKU`
- Vous pouvez vérifier le bon fonctionnement de l'application avec la commande (l'application nécéssite que des "dynos" heroku soient disponible sur votre compte) : 
>`heroku open`

### Étapes nécessaires au déploiement d'une mise à jour d'une application heroku

#### Déploiement mannuel

- Pour le déploiement d'une mise à jour mannuel :
> `docker build -t registry.heroku.com/NOM_APP_HEROKU/web .` (n'oubliez pas le point en fin de commande)
> `docker push registry.heroku.com/NOM_APP_HEROKU/web`
> `heroku container:release web -a NOM_APP_HEROKU`
- Vous pouvez vérifier le bon fonctionnement de l'application avec la commande (l'application nécéssite que des "dynos" heroku soient disponible sur votre compte) : 
>`heroku open`

#### Déploiement automatique avec un pipeline circleCI

Si votre code est poussé sur GitHub et que votre compte circleCI est associé à votre compte GitHub, vous devriez trouver votre projet sur le tableau de bord de circleCI et avoir la possibilité de cliquer un bouton "Set Up Project" à côté du nom de votre projet. Vous pouvez suivre la documentation pour initier votre pipeline (choix de l'option 'Fastest')

- Dans les parametres du projet circleCI, configurez les variables d'envionnement (project settings/environment variables) suivantes:
  - $DOCKERHUB_USERNAME : le nom d'utilisateur de votre compte DockerHub
  - $DOCKERHUB_PASSWORD : votre mot de passe DockerHub
  - $HEROKU_USERNAME : le nom d'utilisateur de votre compte Heroku
  - $HEROKU_API_KEY : votre token Heroku, vous pouvez en obtenir un nouveau avec la commande `heroku auth:token`
  - $HEROKU_APP_NAME : le nom de votre application Heroku
  - $DJANGO_APP_DOCKER_IMAGE_NAME : le nom que vous avez donné à votre image Docker
  - clé SECRET_KEY : demandez la au responsable de l'application
  - clé SENTRY_DSN : voir partie "Journalisation sentry"  du présent document

Une fois votre mise à jour réalisée :
>`git add .`
- Ajoutez un descriptif à votre commit
>`commit -m "DESCRIPTIF_DE_VOTRE_COMMIT" `
- Note: en l'état actuel, le piple circleCI sera executé indépendamment de la branche concernée pour la première étape (linting et tests); néanmoins, la construction de l'image Docker, sa poussée vers DockerHub et le déploiement ne se feront que si la branche concernée par le push est la branche "master"
>`git push -u origin NOM_BRANCHE`

### Journalisation sentry

La journalisation a été mise en place avec la documentation sentry appropriée pour un projet Django et disponible à l'adresse suivante : https://docs.sentry.io/platforms/python/guides/django/ .

Les étapes à suivre sont : 
- créer un compte [sentry](https://sentry.io/signup/)
- sentry-sdk est déja installé dans l'environnement virtuel du projet
- créer un projet sentry, selectionner le framework Django
- le DSN vous est fourni, vous pouvez ajouter ce dsn comme variable d'environnement sur dans les settings de votre application sur le site heroku, ainsi que dans les settings de votre projet sur le site circleCI (voir partie "Étapes nécessaires au déploiement" du présent document)
- vous avez accès aux services de sentry pour le présent projet, pour vérifier cela, rendez vous à l'url NOM_APPLICATION_HEROKU.herokuapp.com/sentry-debug/
- une nouvelle erreur (division par zéro) devrait vous etre signalée au niveau du tableau de bord sentry (sentry.io).
