n, m = map(int, input().split())
nums1 = list(map(int, input().split()))
nums2 = list(map(int, input().split()))
i, j = 0, 0
ans = []
sum = 0
while j < m:
  if i < n and nums1[i] < nums2[j]:
    sum += 1
    i += 1
  else:
      ans.append(sum)
      j += 1
print(' '.join(map(str, ans)))
