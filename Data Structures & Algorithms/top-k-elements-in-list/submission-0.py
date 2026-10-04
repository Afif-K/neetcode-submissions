class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        counts = {}
        result = []

        for num in nums:
            counts[num] = counts.get(num, 0) + 1
        
        buckets = [[] for _ in range(len(nums) + 1)]
        for num, count in counts.items():
            buckets[count].append(num)
        
        for i in range(len(buckets) - 1, 0 , -1):
            for num in buckets[i]:
                result.append(num)
                if len(result) == k:
                    return result



           

    

            

            
        