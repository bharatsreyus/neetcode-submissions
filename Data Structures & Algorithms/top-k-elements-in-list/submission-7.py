class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        countMap = defaultdict(int)
        for num in nums:
            countMap[num] += 1
        
        buckets = [[] for i in range(len(nums) + 1)]

        for num, freq in countMap.items():
            buckets[freq].append(num)

        output = []
        kCounter = 0
        for i in range(len(buckets)-1, 0, -1):
            for j in range(len(buckets[i])):
                output.append(buckets[i][j])
                kCounter += 1
                if kCounter == k:
                    return output