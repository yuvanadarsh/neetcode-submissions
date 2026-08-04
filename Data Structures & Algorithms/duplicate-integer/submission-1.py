class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        my_set = set()

        for item in nums:
            if not item in my_set:
                my_set.add(item)
            else:
                return True

        return False
        