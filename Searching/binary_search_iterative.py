'''
An algorithm is said to have a logarithmic time complexity when it reduces the size of the input data in each step 

example:
for index in range(0, len(arr), 3):
    print(arr[index])
'''
#Iterative

def binary_search(arr, value):
    n = len(arr)
    left = 0
    right = n - 1
    while left <= right:
        middle = (left + right) // 2
        #print(middle,"middle")

        if value < arr[middle]:
            right = middle - 1
            #print(right,"right")

        elif value > arr[middle]:
            left = middle + 1
            #print(left,"left")
        else:
            return middle
    raise ValueError('Value is not in the list')
    
if __name__ == '__main__':
    arr = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    print(binary_search(arr, 8))

'''
n = 8
left = 0
right = 8

middle = (0+8)//2 = 4
arr[middle] = 5
8 > 5
left = 5

middle = (5+8)//2 = 6
arr[middle] = 7
8 > 7
left = 7

middle = (7+8)//2 = 7
arr[middle] = 8
8 = 8
return 7

'''