class Solution:

    def reverseArray(self, arr):
        s = 0
        end=len(arr) - 1

        while end>s:
            arr[s], arr[end] = arr[end], arr[s]
            end -= 1
            s += 1
        return arr
    

a = Solution()
arr = [1,2,3,4]
obj= a.reverseArray(arr)
print(obj)



"""
    we have arr and we need to reverse it on the place
    without using any extra space 
"""