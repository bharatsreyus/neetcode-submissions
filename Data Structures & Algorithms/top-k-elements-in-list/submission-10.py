class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # nums.size 1 to 10000
        # nums[i] from -1000 to 1000
        # distinct elements range: 1(maxfreq = 10000) to 2000 (maxfreq = 5)
        # list[k] = num where k is the freq

        freq = [[] for i in range(len(nums) + 1)]

        numVsFreq = defaultdict(int)

        for num in nums:
            numVsFreq[num] += 1

        maxIdx = -1
        for num, cnt in numVsFreq.items():
            freq[cnt].append(num)

        output = []
        for i in range(len(freq)-1, -1, -1):
            for num in freq[i]:
                output.append(num)
                if len(output) == k:
                    return output
            
            

