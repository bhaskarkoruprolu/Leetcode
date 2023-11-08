class Solution:
    def twoSum(self, nums, target):
        # Create a dictionary to store the indices of elements we've seen
        num_indices = {}
        
        for index, num in enumerate(nums):
            # Calculate the complement (the number we need to reach the target)
            complement = target - num
            
            # If the complement is in our dictionary, we found the pair
            if complement in num_indices:
                return [num_indices[complement], index]
            
            # Otherwise, add the current number and its index to the dictionary
            num_indices[num] = index
        