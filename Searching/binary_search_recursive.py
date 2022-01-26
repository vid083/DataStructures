# recursive
'''
Approach:-

1. Compare x with the middle element.
2. If x matches with the middle element, we return the mid index.
3. Else If x is greater than the mid element, then x can only lie in the right half subarray after the mid element. So we recur for the right half.
4. Else (x is smaller) recur for the left half.

'''

def binarySearch(arr, left, right, x):
    l=left  #0
    r=right #len(arr)-1
    if r >= l:
        mid = l + (r - l) // 2
        print("mid-",mid)

        if arr[mid] == x:
            return mid

        elif x < arr[mid]:
            print(mid-1,"left subarray")
            return binarySearch(arr, l, mid-1, x)

        else:
            print(mid+1,"right subarray")
            return binarySearch(arr, mid + 1, r, x)

    return -1


# Driver Code
arr = [2, 3, 4, 10, 40]
x = 50

# Function call
result = binarySearch(arr, 0, len(arr)-1, x)

if result != -1:
    print("Element is present at index", result)
else:
    print("Element is not present in array")

'''

l=0,    r=4,    4>=0
mid = (0+4)/2 = 2
mid=2,  arr[mid] = 4,   50 > 4,     l = mid+1 = 3

l=3,    r=4,    4>=3
mid=(3+(4-3))/2=1,  arr[mid] = 3,  50 > 3,     l = mid+1 = 4

l=4,    r=4,    4>=4
mid=(4+(4-4))/2=2,  arr[mid] = 2,  50 > 3,     l = mid+1 = 5

l=5,    r=4,    4>=5    return -1

'''