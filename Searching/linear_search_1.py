'''
Input : arr[] = {10, 20, 80, 30, 60, 50, 110, 100, 130, 170}
          x = 110;
Output : Element x is present at index 6

Input : arr[] = {10, 20, 80, 30, 60, 50, 110, 100, 130, 170}
           x = 175;
Output : Element x is not present in arr[]


Approach:-
1. Start from the leftmost element of arr[] and one by one compare x with each element of arr[]
2. If x matches with an element, return the index.
3. If x doesn’t match with any of elements, return-not present.

'''

def linear_search(arr,x):   
    for i in range(len(arr)):   
        if arr[i] == x:
            return f"Element {x} is present at index {i}"
    return f"Element {x} is not present in {arr}"


arr= [10, 20, 80, 30, 60, 50, 110, 100, 130, 170]
x = int(input("Enter a element to search in arr: "))    #130
print(linear_search(arr,x))

'''
i = 0, arr[0]=10, 10 != 130, returns - not present
i = 1, arr[1]=20, 20 != 130, returns - not present
i = 2, arr[2]=80, 80 != 130, returns - not present
i = 3, arr[3]=30, 30 != 130, returns - not present
i = 4, arr[4]=60, 60 != 130, returns - not present
i = 5, arr[5]=50, 50 != 130, returns - not present
i = 6, arr[6]=110, 110 != 130, returns - not present
i = 7, arr[7]=100, 100 != 130, returns - not present
i = 8, arr[8]=130, 130 == 130, returns - present at index 8

Time complexity:- if element Found at last  O(n) to O(1).

Linear search is rarely used practically because other search algorithms 
such as the binary search algorithm and hash tables allow significantly 
faster-searching comparison to Linear search
'''