#!/bin/bash

if [ ! -n "$1" ];then
  echo "Specify Django project name to manage"
  exit 3
fi

DIR="$( cd -P "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"
PROJECT_PATH="$DIR/projects/$1"

if [ ! -d "$PROJECT_PATH" ];then
  echo "not a directory: $1"
  exit 2
fi

#Activate virtual env
VENV_PATH="$DIR/venv/$1"
source $VENV_PATH/bin/activate

#Execute requested Django manage command for the specified project
cd $PROJECT_PATH
python ./manage.py $2 $3 $4 $5 $6 $7 $8 $9

#Deactivate virtual env
deactivate
