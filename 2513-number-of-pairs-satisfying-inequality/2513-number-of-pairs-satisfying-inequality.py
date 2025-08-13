class Solution:
    def numberOfPairs(self, nums1: List[int], nums2: List[int], diff: int) -> int:
        a = [nums1[i] - nums2[i] for i in range(len(nums1))]
        temp = [0] * len(a)

        def merge_count(low, high):
            if high - low <= 1:
                return 0
            mid = (low + high) // 2
            count = merge_count(low, mid) + merge_count(mid, high)

            # Count cross pairs
            p = mid
            for i in range(low, mid):
                target = a[i] - diff
                while p < high and a[p] < target:
                    p += 1
                count += high - p

            # Merge step
            i, j, k = low, mid, low
            while i < mid and j < high:
                if a[i] <= a[j]:       
                    temp[k] = a[i]
                    i += 1
                else:
                    temp[k] = a[j]
                    j += 1
                k += 1
            while i < mid:
                temp[k] = a[i]
                i += 1
                k += 1
            while j < high:
                temp[k] = a[j]
                j += 1
                k += 1

            a[low:high] = temp[low:high]
            return count

        return merge_count(0, len(a))
