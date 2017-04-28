import os
import psycopg2
import json

pgUser = os.environ['PGUSER']
pgPass = os.environ['PGPASS']
pgHost = os.environ['PGHOST']
pgPort = os.environ['PGPORT']
pgDbName = os.environ['PGDBNAME']

def get_last_2_snapshots(battleTag):
  '''Get last 2 snapshots of battleTag by date'''
  conn = psycopg2.connect(dbname=pgDbName, user=pgUser, password=pgPass, host=pgHost, port=pgPort)
  cur = conn.cursor()
  cur.execute('SELECT data FROM snapshots WHERE battletag=%s ORDER BY datetaken DESC LIMIT 2', (battleTag,))
  results = cur.fetchall()
  cur.close()
  conn.close()
  return results

def get_last_snapshots(battleTag):
  '''Get last snapshots of battleTag by date'''
  conn = psycopg2.connect(dbname=pgDbName, user=pgUser, password=pgPass, host=pgHost, port=pgPort)
  cur = conn.cursor()
  cur.execute('SELECT data FROM snapshots WHERE battletag=%s ORDER BY datetaken DESC LIMIT 1', (battleTag,))
  results = cur.fetchall()
  cur.close()
  conn.close()
  return results