class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        duplicates = set()
        for numbers in nums: 
            if numbers in duplicates:
                return True
            duplicates.add(numbers)

        return False
