def snapshot_diff(snap1, snap2):
  snap1Data = snap1[data]
  snap2Data = snap2[data]
  resultData = {}
  for hero in snap1Data:
    if snap1Data[hero]['Games Played'] != snap2Data[hero]['Games Played']:
      