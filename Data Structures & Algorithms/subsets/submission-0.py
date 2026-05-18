class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        # out = [[]]
        # if not nums:
        #     return out
        # elif len(nums) == 1:
        #     out.append([nums[0]])
        #     return out
        #ex: [1, 2, 3]
        out = []

        cur_subset = []

        def dfs(idx):
            #base case when we reach too far beyond the length of nums and thus run out of anything to explore
            if idx > len(nums) - 1:
                out.append(cur_subset.copy())
                return
            #consider adding another elem
            cur_subset.append(nums[idx])
            dfs(idx + 1)

            #consider not adding another elem, meaning remove the one you added a few lines above
            cur_subset.pop()
            dfs(idx + 1)

        dfs(0)

        return out
            
        