def diff_snapshots (snap1, snap2):
  resultSnap = {}
  for hero in snap1:
    if snap1[hero]['Games Played'] != snap2[hero]['Games Played']:
      resultSnap[hero] = {}
      for stat in snap1[hero]:
        if snap1[hero][stat] != snap2[hero][stat]:
          try:
            stat1Int = snap1[hero][stat]
            stat2Int = snap2[hero][stat]
            resultSnap[hero][stat] = stat1Int - stat2Int
          except:
            resultSnap[hero][stat] = 'Old: ' + snap1[hero][stat] + ', New: ' + snap2[hero][stat]
  return resultSnap