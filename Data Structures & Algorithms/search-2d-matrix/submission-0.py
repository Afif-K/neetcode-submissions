class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        
        flat = []

        for sub in matrix:
            for i in sub:
                flat.append(i)

        l = 0
        r = len(flat) - 1

        while l <= r:
            mid = (l + r) // 2

            if flat[mid] == target:
                return True
            elif flat[mid] < target:
                l = mid + 1
            else:
                r = mid - 1
        
        return False
            