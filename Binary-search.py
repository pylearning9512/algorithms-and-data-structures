target=input("what number are we looking for?: ")
arr=list(range(1,1000000))

guess=int(target)
nums=arr

def binary_search(guess,nums):

    left=0
    right=len(arr)-1

    while left<=right:
        mid= (left+right)// 2

        if nums[mid]==guess:
            return mid
        elif nums[mid]>guess:
             right= mid-1
        elif nums[mid]<guess:
            left= mid+1
    return -1
result= binary_search(guess,nums)

if result !=-1:
    print("target number is the ",result, "index number on the list")
else:
    print("this target number is not in our list :C")