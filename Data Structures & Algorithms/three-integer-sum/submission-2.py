class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:

        new_nums = sorted(nums)
        res = []

        for i in range(len(new_nums)):
            if i > 0 and new_nums[i] == new_nums[i - 1]:
                continue
            j = i + 1
            k = len(new_nums) - 1

            while j < k:
                if new_nums[i] + new_nums[j] + new_nums[k] > 0:
                    k -= 1
                elif new_nums[i] + new_nums[j] + new_nums[k] < 0:
                    j += 1
                else:
                    res.append([new_nums[i], new_nums[j], new_nums[k]])
                    j += 1
                    k -= 1
                    while j < k and new_nums[j] == new_nums[j - 1]:
                        j += 1
            
        return res
            





        



            
        
                


