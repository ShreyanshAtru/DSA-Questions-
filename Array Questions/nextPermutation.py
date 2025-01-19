class Solution:

    def nextPermutation(self, arr:list):
        """first we need to find a indx or a pivot 
        pivot/indx is a break point where from the right sie of list is have incrementing order of the number
        """

        pivot = -1

        for i in range(len(arr)-2, -1, -1):
            if arr[i]<arr[i+1]:
                pivot = i
                break
        
        if pivot != -1:
            # now we will swap the pivot value with the just next greater value of it
            for s in range(len(arr)-1, pivot, -1):
                if arr[s]> arr[pivot]:
                    arr[s], arr[pivot] = arr[pivot], arr[s]
                    break
        
        if pivot == -1:
            return arr.reverse()
        
        # after the pivot swapping, from the next number we will reverse it to get next permuation
        arr[pivot+1:] = reversed(arr[pivot+1:])


a = Solution
arr= [2, 4, 1, 7, 5, 0]

obj = a.nextPermutation(arr)
print(obj)