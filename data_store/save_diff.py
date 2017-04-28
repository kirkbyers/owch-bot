import os
import psycopg2
import json

from overwatch_api.get_bt_stats import getStats

pgUser = os.environ['PGUSER']
pgPass = os.environ['PGPASS']
pgHost = os.environ['PGHOST']
pgPort = os.environ['PGPORT']
pgDbName = os.environ['PGDBNAME']

def save_diff(battleTag, diff):
  '''Save a previously calculated diff in db'''
  if len(diff) > 0:
    conn = psycopg2.connect(dbname=pgDbName, user=pgUser, password=pgPass, host=pgHost, port=pgPort)
    cur = conn.cursor()
    cur.execute("INSERT INTO diffs (battleTag, data) VALUES (%s, %s)", (battleTag, json.dumps(diff, ensure_ascii=False)))
    conn.commit()
    cur.close()
    conn.close()
  return diff
