#!/bin/bash

git config --global user.email "$GITHUB_EMAIL"
git config --global user.name "$GITHUB_ACTOR"
# shellcheck disable=SC1073
cat << EOF > ~/.netrc
  machine cv-football-api
    login "$HEROKU_USERNAME"
    password "$HEROKU_API_KEY"
  # shellcheck disable=SC1039
EOF
heroku create -a cv-football-api