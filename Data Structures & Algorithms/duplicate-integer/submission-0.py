class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        dups = []
        for num in nums:
            if num not in dups:
                dups.append(num)
            else:
                return True
        return False
        