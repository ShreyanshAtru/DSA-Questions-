# https://leetcode.com/problems/special-array-i/description/

class Solution:
    def specialArray(self, arr):
        """
        A speical array is that each pair of arr have even-odd pairs
        we have to check even-odd sequence if its not return False
        1. By using modulo (%)
        2. By using AND (&) nitwise operation 
            e.g. 5&3 -> 5 = 101
                        3 = 011 
                      5&3 = 001
        """

        for i in range(1, len(arr)):
            if arr[i] & 1 == arr[i-1] & 1:   # nums[i]%2 == nums[i-1]%2
                return False
        return True


obj = Solution()
arr1=[1,2]
arr2 = [1]
arr3 = [4,3,1,6]

print(obj.specialArray(arr3))
