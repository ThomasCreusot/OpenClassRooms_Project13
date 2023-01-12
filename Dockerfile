# https://hub.docker.com/_/python / How to use this image
# https://docs.docker.com/language/python/build-images/

# OpenClassrooms courses : 
# FROM: defin the image source
# RUN: execute commandes in the container
# ADD: add files in the container
# WORKDIR: define the repository for working (equivalent to "cd" on the windows temrinal)
# EXPOSE: define the ports
# VOLUME: define usable volumes
# CMD: define the default command during Docker container execution


# https://hub.docker.com/_/python FROM python:3
# https://docs.docker.com/language/python/build-images/ FROM python:3.8-slim-buster
FROM python:3.10

#https://github.com/docker/awesome-compose/tree/master/official-documentation-samples/django/
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# https://hub.docker.com/_/python WORKDIR /usr/src/app
# https://docs.docker.com/language/python/build-images/ WORKDIR /app
# To make things easier when running the rest of our commands, let’s create a working directory.
# This instructs Docker to use this path as the default location for all subsequent commands.
# By doing this, we do not have to type out full file paths but can use relative paths based on the
# working directory.

WORKDIR /app

# https://hub.docker.com/_/python COPY requirements.txt ./
# https://docs.docker.com/language/python/build-images/ COPY requirements.txt requirements.txt
# Before we can run pip3 install, we need to get our requirements.txt file into our image. We’ll
# use the COPY command to do this. The COPY command takes two parameters [...]
#COPY requirements.txt ./
COPY ./requirements.txt /app/

# https://hub.docker.com/_/python RUN pip install --no-cache-dir -r requirements.txt
# https://docs.docker.com/language/python/build-images/ RUN pip3 install -r requirements.txt
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

# https://hub.docker.com/_/python COPY . .
# https://docs.docker.com/language/python/build-images/ COPY . .
# The next step is to add our source code into the image. We’ll use the COPY command just like we did with our requirements.txt file above.
# This COPY command takes all the files located in the current directory and copies them into the image
#COPY . .
COPY . /app

RUN python manage.py collectstatic --noinput

# https://hub.docker.com/_/python CMD [ "python", "./your-daemon-or-script.py" ]
# https://docs.docker.com/language/python/build-images/ CMD [ "python3", "-m" , "flask", "run", "--host=0.0.0.0"]
# Now, all we have to do is to tell Docker what command we want to run when our image is executed
# inside a container. We do this using the CMD command. Note that we need to make the application
# externally visible (i.e. from outside the container) by specifying --host=0.0.0.0.
#CMD ["python", "manage.py" , "runserver", "0.0.0.0:8000"]
#CMD python manage.py runserver 0.0.0.0:8000
#CMD python manage.py runserver 0.0.0.0:$PORT

# initial code for local
# CMD ["python", "manage.py" , "runserver", "0.0.0.0:8000"]
# first attempt for online deployment
# ENV PORT=8000
# CMD python manage.py runserver 0.0.0.0:$PORT
# second attempt for online deployment
ENV PORT=8000
CMD gunicorn oc_lettings_site.wsgi --bind 0.0.0.0:$PORT 

# https://hub.docker.com/_/python You can then build and run the Docker image:
# $ docker build -t my-python-app .
# $ docker run -it --rm --name my-running-app my-python-app

# https://docs.docker.com/language/python/build-images/ 
# docker build --tag python-docker .
# To list images, simply run the docker images command.


# docker build -t p13-django-app_image_221227_09h10 .
# docker images
# docker run --publish 8000:8000 p13-django-app_image_221227_09h10:latest
# curl localhost:8000
