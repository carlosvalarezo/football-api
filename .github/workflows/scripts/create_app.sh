#!/bin/bash

git config --global user.email "${GITHUB_EMAIL}"
git config --global user.name "${GITHUB_ACTOR}"
cat << EOF > ~/.netrc
  machine cv-football-api
    login "$HEROKU_USERNAME"
    password "$HEROKU_API_KEY"
  EOF
heroku create -a cv-football-api