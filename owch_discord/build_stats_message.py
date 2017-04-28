messageLimit = 2000

def printStats(statsDicty):
  if len(statsDicty) == 0:
    return ['No change since last snapshot']
  result = ''
  resultArray = []
  for key in statsDicty:
    temp = '***' + key + '***\n'
    if canAddString(result, temp):
      result += temp
    else:
      resultArray.append(result)
      result = ''
    for stat in statsDicty[key]:
      temp = stat + ': ' + statsDicty[key][stat] + '\n'
      if canAddString(result, temp):
        result += temp
      else:
        resultArray.append(result)
        result = ''
  resultArray.append(result)
  return resultArray

def canAddString(currentString, inpString):
  if len(currentString) + len(inpString) > messageLimit:
    return False
  else:
    return True