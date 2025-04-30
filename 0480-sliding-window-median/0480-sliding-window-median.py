class Solution:
    def medianSlidingWindow(self, nums: List[int], k: int) -> List[float]:
        # mnhp = [(nums[i], i) for i in range(k)]
        # # print(mnhp)
        # heapify(mnhp)
        # # print(mnhp)

        # mxhp = []
        # mn, mx = 0, k
        # deleted = set()

        # def balance():
        #     nonlocal mn, mx
        #     while abs(mx - mn) > 1:
        #         while mnhp and mnhp[0][1] in deleted:
        #             heappop(mnhp)
        #         while mxhp and (mxhp[0][1]) in deleted:
        #             heappop(mxhp)
        #         if not mxhp:
        #             a, b = heappop(mnhp)
        #             heappush(mxhp, (-a, b))
        #             mn += 1
        #             mx -= 1
        #         elif not mnhp:
        #             a, b = heappop(mxhp)
        #             heappush(mnhp, (-a, b))
        #             mx += 1
        #             mn -= 1
        #         else:
        #             if mx > mn:
        #                 a, b = heappop(mnhp)
        #                 heappush(mxhp, (-a, b))
        #                 mx -= 1
        #                 mn += 1
        #             else:
        #                 a, b = heappop(mxhp)
        #                 heappush(mnhp, (-a, b))
        #                 mn -= 1
        #                 mx += 1
        # # print(mxhp, mnhp, mn, mx)       
        # balance()
        # print(mxhp, mnhp, mn, mx)
        # ans = []
        # for r in range(k, len(nums)):
        #     l = r - k
        #     deleted.add(l)
        #     heappush(mnhp, (nums[r], r))
        #     mx += 1
        #     mitefaw = nums[l]
        #     if mnhp[0][0] <= mitefaw:
        #         mx -= 1
        #     else:
        #         mn -= 1
        #     balance()
        #     print(mxhp, mnhp, mx, mn)
        #     if mx > mn:
        #         ans.append(mnhp[0])
        #     elif mn < mx:
        #         ans.append(-mxhp[0])
        #     else:
        #         ans.append((-mnhp[0] + mxhp[0]) / 2)
        #     print("-----")
            
        # return ans

        max_hp = []
        min_hp = []

        store = defaultdict(int)
        ans = []

        for i in range(k):
            heappush(max_hp, -nums[i])
            heappush(min_hp, -heappop(max_hp))

            if len(min_hp) > len(max_hp):
                heappush(max_hp, -heappop(min_hp))
        if k % 2 != 0:
            med = -max_hp[0]
        else:
            med = (-max_hp[0] + min_hp[0])/2
        ans.append(med)
        
        
        for i in range(k, len(nums)):
            prev = nums[i-k]
            store[prev] += 1

            balance = 0
            if prev <= med:
                balance = -1
            else:
                balance = 1
            
            if nums[i] <= med:
                balance += 1
                heappush(max_hp, -nums[i])
            else:
                balance -= 1
                heappush(min_hp, nums[i])
            
            if balance < 0:
                heappush(max_hp, -heappop(min_hp))
            elif balance > 0:
                heappush(min_hp, -heappop(max_hp))
            
            while max_hp and store[-max_hp[0]] > 0:
                store[-max_hp[0]] -=1
                heappop(max_hp)
            while min_hp and store[min_hp[0]] > 0:
                store[min_hp[0]] -= 1
                heappop(min_hp)
            
            if k % 2 != 0:
                med = -max_hp[0]
            else:
                med = (-max_hp[0] + min_hp[0])/2
            ans.append(med)
        return ans
