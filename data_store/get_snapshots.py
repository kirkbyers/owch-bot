import os
import psycopg2
import json

pgUser = os.environ['PGUSER']
pgPass = os.environ['PGPASS']
pgHost = os.environ['PGHOST']
pgPort = os.environ['PGPORT']
pgDbName = os.environ['PGDBNAME']