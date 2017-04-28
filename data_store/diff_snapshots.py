def diff_snapshots (snapNew, snapOld):
  resultSnap = {}
  for hero in snapNew:
    if snapNew[hero]['Games Played'] != snapOld[hero]['Games Played']:
      resultSnap[hero] = {}
      for stat in snapNew[hero]:
        try:
          if snapNew[hero][stat] != snapOld[hero][stat]:
            try:
              try:
                stat1Int = int(snapNew[hero][stat])
                stat2Int = int(snapOld[hero][stat])
                resultSnap[hero][stat] = stat1Int - stat2Int
              except:
                stat1Int = float(snapNew[hero][stat])
                stat2Int = float(snapOld[hero][stat])
                resultSnap[hero][stat] = stat1Int - stat2Int
            except:
              resultSnap[hero][stat] = 'New: ' + snapNew[hero][stat] + ', Old: ' + snapOld[hero][stat]
        except:
          pass
  return resultSnap