#!/bin/bash

if [ ! -n "$1" ];then
  echo "Specify Django project name to prepare"
  exit 3
fi

DIR="$( cd -P "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"
PROJECT_PATH="$DIR/projects/$1"

if [ ! -d "$PROJECT_PATH" ];then
  echo "not a directory: $1"
  exit 2
fi

MNT_PATH="$DIR/mnt/$1"

if [ ! -d "$MNT_PATH" ];then
  echo "not a directory: $1"
  exit 2
fi

USER_NAME=$(logname)     #original username, even after sudo or su
GROUP_NAME=www-data

#Create directory for files upload
mkdir -p "$MNT_PATH/media/"

#Create directory for thumbnail files
mkdir -p "$MNT_PATH/thumbs/"

#Create directory to collect static files (js, CSS, etc.)
mkdir -p "$MNT_PATH/static/"

#Activate virtual env
VENV_PATH="$DIR/venv/$1"
source $VENV_PATH/bin/activate

#Extract all static files
cd $PROJECT_PATH
python ./manage.py collectstatic

#Deactivate virtual env
deactivate

#Change owner and access rights to project directory
chown -R "$USER_NAME.$GROUP_NAME" "$MNT_PATH"
chmod -R u=rwx,g=rx,o= "$MNT_PATH"

#Grant write permission to the Web server for files in upload directory
chmod -R g+w "$MNT_PATH/media/"

#Grant write permission to the Web server for files in thumbnail directory
chmod -R g+w "$MNT_PATH/thumbs/"
