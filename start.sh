#!/bin/bash

docker build . -t carlosvalarezo/football-api
docker run -itp 5000:5000 --rm --name football-api \
        -v "$PWD"/api:/api carlosvalarezo/football-api
