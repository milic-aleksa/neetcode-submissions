class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hashMap = {}
        bucket = [[] for _ in range(len(nums) + 1)]

        for num in nums:
            hashMap[num] = hashMap.get(num, 0) + 1
        
        for num, cnt in hashMap.items():
            bucket[cnt].append(num)
        
        res = []
        for item in range(len(bucket) - 1, 0, -1):
            for num in bucket[item]: 
                res.append(num)
                if len(res) == k:
                    return res
        

        
