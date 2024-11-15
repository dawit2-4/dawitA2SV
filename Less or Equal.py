import heapq
n, k = map(int, input().split())
a = list(map(int, input().split()))
 
def less(n,k,a):
  if k == 0:
    min_element = min(a)
    if min_element > 1:
      return 1
    else:
      return -1
  
  heapq.heapify(a)
 
  for _ in range(k):
    x = heapq.heappop(a)
  
  if a and a[0] == x:
    return -1
  
  return x
 
print(less(n,k,a))
