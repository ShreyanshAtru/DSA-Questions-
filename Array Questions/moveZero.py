# Move All Zeroes to End

class Solution():

    def moveZero(self, arr):
        # brute force method
        # 	for i in range(len(arr)):
        # 	    if arr[i] == 0:
        # 	        arr.append(arr[i])
        # 	        arr.remove(arr[i])
        # 	return arr
        
        # two pointer approach 

        non_zero = 0   # non zero values
        zero_ptr = 0   # zero numbers

        while len(arr) > zero_ptr:      
            if arr[zero_ptr] != 0:
                arr[zero_ptr], arr[non_zero] = arr[non_zero], arr[zero_ptr]    # swapping all the non zero numbers
                non_zero += 1  
            zero_ptr += 1
        return arr
    

for i in range(int(input())):
    arr = list(map(int, input().split()))
    obj = Solution()
    print(obj.moveZero(arr))
