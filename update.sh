#!/bin/bash

# Project Specific settings
if test -f "projects/prb-math"; then
  :
else
  cp projects/prb-math/.env.example projects/prb-math/.env
fi

# Generate all documentations and then copy them to repository
cd projects
for PROJECT in ./*
do
  cd $PROJECT
  echo "Working on $PROJECT"
  if test -d "node_modules"; then
    :
  else
    yarn install
  fi
  PROJECT_DIR=$(pwd)
  (cd $PROJECT_DIR; ./docs.sh)
  cp -r docs-site/site ../../website
  cd ../../website
  NEW_NAME=$(basename $PROJECT)
  rm -r $NEW_NAME #removes old project
  mv site $NEW_NAME
  cd ../projects
done
