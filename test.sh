#!/bin/bash

docker build . -t carlosvalarezo/football_api_tests -f Dockerfile._dev
docker run -v "$PWD"/api/:/api carlosvalarezo/football_api_tests python -m pytest /api/tests
