def checker(num):
   if num > 0:
      return True
   elif num < 0:
      return False
def alternate():
  t = int(input())
  for _ in range(t):
    n = int(input())
    arr = list(map(int, input().split()))
    sum = 0
    i = 0

    while i < n:
      j = i
      cur = arr[i]
      while j < n and checker(arr[i]) == checker(arr[j]):
          cur = max(cur, arr[j])
          j += 1
      sum += cur
      i = j
    print(sum)

alternate()
