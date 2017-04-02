import os
import psycopg2
import json

from overwatch_api.get_bt_stats import getStats

pgUser = os.environ['PGUSER']
pgPass = os.environ['PGPASS']
pgHost = os.environ['PGHOST']
pgPort = os.environ['PGPORT']
pgDbName = os.environ['PGDBNAME']

def snapshot_comp(battleTag):
  conn = psycopg2.connect(dbname=pgDbName, user=pgUser, password=pgPass, host=pgHost, port=pgPort)
  cur = conn.cursor()
  stats = getStats(battleTag)
  cur.execute("INSERT INTO snapshots (battleTag, data) VALUES (%s, %s)", (battleTag, json.dumps(stats, ensure_ascii=False)))
  conn.commit()
  cur.close()
  conn.close()
  return stats
