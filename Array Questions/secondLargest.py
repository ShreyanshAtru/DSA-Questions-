# you have an array, need to print seconf largest element. 

class Solution:
    def secondLargest(self, arr):
        large = float('-inf')
        second = float('-inf')

        if len(arr)<2:
            return -1 

        for num in arr:
            if num > large:
                second = large
                large = num 

            if num > second and num != large:
                second = num 

        if second == float('-inf'):
            return -1 
        else:
            return second


for i in range(int(input())):
    arr = list(map(int, input().split()))
    obj = Solution()
    a = obj.secondLargest(arr)
    print(a)