from math import sqrt

def sieve(n): 
  list = [True] * n
  list[0] = list[1] = False
  sqrtN = int(sqrt(n)) + 1
  for i in range (2, sqrtN):
    for j in range (i*2, n, i):
      list[j] = False
  list = sieveValues(list)
  return list

def sieveValues(list):
  valsList = []
  for i, j in enumerate(list):
    if j == True:
      valsList.append(i)
  return valsList
  

def binarySearch(n, list, indexLow, indexHigh):
  indexMid = int((indexLow+indexHigh)/2)
  if list[indexMid] == n:
    return indexMid
  elif list[indexMid] < n:
    return binarySearch(n, list, indexMid, indexHigh)
  else:
    return binarySearch(n, list, indexLow, indexMid)


if __name__ == "__main__":
  list = sieve(1000000)
  print(list)
  
  index = (binarySearch(97, list, 0, len(list)+1))
  print(f"index: {index}")