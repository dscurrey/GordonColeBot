# Gordon Cole Bot (Discord)

[![CodeFactor](https://www.codefactor.io/repository/github/dscurrey/gordoncolebot/badge)](https://www.codefactor.io/repository/github/dscurrey/gordoncolebot)

A Gordon Cole Discord bot, based on the David Lynch character from Twin Peaks

## Installation

### With Docker

This method requires [Docker]("https://www.docker.com/").

To run the bot in a docker container, do the following:
```
docker run -d -e DISCORD_TOKEN=DISCORDTOKEN \
 -e DISCORD_GUILD=GUILDID \
 dcurrey/gordoncole
```
Replacing "DISCORDTOKEN" and "GUILDID" with their respective developer values.

This will pull the latest image from docker, and run it with the above environment variables.

To build the image from source:
```
docker build .
```

### With Docker Compose (and Watchtower)

This method requires [Docker]("https://www.docker.com/") and docker-compose.

First, clone the repository - the compose file builds from source, though it can be easily changed to pull from the repository:

In [docker-compose.yml](./docker-compose.yml), change:
```
build: .
```
To:
```
image: dcurrey/gordoncole
```

Then run:
```
docker-compose up
```

This will build the docker image and create two containers: one containing the bot, the other running [Watchtower](https://github.com/containrrr/watchtower), which will keep the bot updated.
