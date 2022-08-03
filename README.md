# football-api

This football API fetches football leagues from `football-data.org`. On fetching data the request includes: leagues,
teams & players.

Once the data has been fetched from the API, it is stored in a DB in order to use that data as source for other
endpoints.

## Stack
- `docker-compose` to connect the DB and the API services
- `docker` to manage the containerization of the API
- `flask` framework to develop the API
- `postgresql` data base engine to store the league data
- `sqlalchemy` ORM to map the models to the DB tables
- `gunicorn` is a Python Web Server Gateway Interface HTTP server

## Start

`export API_KEY_FOOTBALL=<API_KEY_FOOTBALL>`<br/>
`export FOOTBALL_URI=http://api.football-data.org`<br/>
`export COMPETITIONS_ENDPOINT=/v4/competitions/`<br/>
`sh start`

## Tests

`sh test`

## Endpoints

`health/status` checks if the API is up and running
`setup/league/<league_code>` fetches the data from the `football-data.org` and stores the fetched data in the DB
`api/players/<league_code>[?team=<team_code>]` returns the list of players that belong to a particular `<league_code>`
with the option to filter them by `team_code`

## Data to try

`league_code` = PL, PD, SA<br/>
`team_code` = for PL/66,65 

### Solution

Since one of the endpoints is going to fetch data from a remote service and the other endpoint needs to store the data
in a local DB, the approach considered isolating the app from the sources of the data was Repository pattern
In this way if the source changes the app will never know about the change. In the same way if the DB changes the app
does not need to change. The only place that changes is the ORM connection (SQLAlchemy). It also implements the
`open-close` principle. Furthermore, since the app does not about the DB, nor the ORM, it also implements the
`Dependency Inversion` principle.
The ORM know about the model but not the other way around. Also, all the packages, methods, endpoints,
blueprints apply the `Single resposibility` principle.
Postgres was chosen because of the data model to manage. It does not need data redundancy nor repeated data as it would
be in a NoSQL approach.
It implements the blueprints for Flask in order to apply the `separation of coancerns` principle.
The solution also comes with an initial script. This feature opens the possibility to use `alembic` in the future
in case the DB schema needs changes


### Troubleshooting
If either of the both automated scripts fails it is because the permissions need to be updated.
The execution permissions get lost since the repo is brand new in the directory.
To sort this out execute `chmod +x start.sh` & `chmod +x test.sh` and execute them.


### TODO
- Extend the test coverage
- Deploy to Heroku through a GitHub actions pipeline
- Push the docker image to a registry (public or private)
- Include Auth0 authentication (user & password for instance) to generate/validate JWT token for consecutive calls
