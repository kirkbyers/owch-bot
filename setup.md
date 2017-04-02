# Setup

## Requirements

It is recommended that you use [Virtualenv](https://pypi.python.org/pypi/virtualenv).

This project is currently useing Python 3.6.0 and PostgreSQL 9.3.6. 

## Dependencies

Run `pip install -r requirements.txt` to get the required dependencies.

## PostgreSQL Config

As of right now there are no pgSQL scripts to config (TODO).

Create a table named 'snapshots'.

### 'snapshots' Schema

- battletag: string
  - user's battleTag used to look up
- datetaken: timestamp (no timezone)
  - date-time snapshot taken
  - default value: current_datetime
- data: json
  - data returned from snapshot

## Enviornment Variables

### Bash

```
export {var}={value}
```

### Virtualenv

In `./bin/activate` add the bash command at the bottom of the file.

### Used variables

Set the following variables using a method listed above.

- PGUSER: Postgres User
- PGPASS: Postgres password
- PGHOST: Postgres host
- PGPORT: Postgres port
- PGDBNAME: Postgres dbname
- DISCORD_TOKEN: Discord token for identifying your bot

## Discord Permisions

If you haven't already, vist the [discord docs](https://discordapp.com/developers/applications/me) to create an authorized app and then add a bot.

After you have an authorized appliction visit `https://discordapp.com/oauth2/authorize?client_id=CLIENT_ID&scope=bot` where `CLIENT_ID` is your application Client ID.

Upon successful configuration, your bot will appear online when running `./main`.