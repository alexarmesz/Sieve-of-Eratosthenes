from math import sqrt

def sieve(n): 
  list = [True] * n
  list[0] = list[1] = False
  sqrtN = int(sqrt(n)) + 1
  for i in range (2, sqrtN):
    for j in range (i*2, n, i):
      list[j] = False
  return [i for i, j in enumerate(list) if j]

def binary_search(arr, x):
    low = 0
    high = len(arr) - 1
    mid = 0
 
    while low <= high:
 
      mid = (high + low) // 2

      if arr[mid] < x:
        low = mid+1
      if arr[mid] > x:
        high = mid-1
      else:
        return mid
    return -1

if __name__ == "__main__":
  list = sieve(10000)
  print(list)
  
  index = (binary_search(list, 97))
  print(f"index: {index}")
