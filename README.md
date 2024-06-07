# Loki Discord Bot

A simple python discord bot, created for fun and to start learning about the discord.py library

## Contents

- [Version Control](#version-control)
- [Getting Started](#getting-started)
  - [Dependencies](#dependencies)
  - [Installation](#installation)
  - [Populating the env file](#populating-the-env-file)
- [Commands](#commands)
- [Resources & Thanks](#resources-&-thanks)
- [Issues](#issues)

## Version Control

v0.0.1 - 2024-06-01: Original version without commands

v0.1.1 - 2024-06-01: Addition of ping command

## Getting Started

### Dependencies

The following packages are required:

- discord.py==2.3.2
- python-dotenv==1.0.1

### Installation

As this bot currently is not being hosted, you will need to clone the repository and host it yourself via your prefered platform:

`git clone https://github.com/ichbinjade/loki-discord-bot`

### Populating the env file

Copy the `.env.example` file to `.env` and populate the relevant variables:

- `DISCORD_TOKEN=` : This will be your bot's token from the developer portal
- `COMMAND_PREFIX=""` : While slash commands are popular, I still prefer using "!" prefixes

## Commands

### Ping

`!ping` - returns 'Pong! 42ms'; where '42ms' is the relevant latency

## Resources & Thanks

[@Indently](https://www.youtube.com/@Indently) - YouTuber that has great tutorials

[GeeksForGeeks](https://www.geeksforgeeks.org/discord-bot-in-python/) - A great site and community with lots of programming resources and tutorials

[Real Python](https://realpython.com/how-to-make-a-discord-bot-python/) - Another great site with lots of resources and tutorials

## Issues

None
