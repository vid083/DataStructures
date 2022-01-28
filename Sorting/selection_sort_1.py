def selection_sort(arr):
    for i in range(len(arr)-1):
        min_index = i   # Find the minimum element
        for j in range(i+1, len(arr)):
            print("i=",i,", j=",j,", arr[min_index]=",arr[min_index],", arr[j]=",arr[j],", arr=",arr)
            if arr[min_index] > arr[j]:
                min_index = j
               	
        arr[i], arr[min_index] = arr[min_index], arr[i] # Swap the found minimum element with the first element	

    return arr


arr = [64, 25, 12, 22, 11]
print("Sorted array is:",selection_sort(arr))

'''
i= 0 , j= 1 , arr[min_index]= 64 , arr[j]= 25 , arr= [64, 25, 12, 22, 11]
i= 0 , j= 2 , arr[min_index]= 25 , arr[j]= 12 , arr= [64, 25, 12, 22, 11]
i= 0 , j= 3 , arr[min_index]= 12 , arr[j]= 22 , arr= [64, 25, 12, 22, 11]
i= 0 , j= 4 , arr[min_index]= 12 , arr[j]= 11 , arr= [64, 25, 12, 22, 11]

i= 1 , j= 2 , arr[min_index]= 25 , arr[j]= 12 , arr= [11, 25, 12, 22, 64]
i= 1 , j= 3 , arr[min_index]= 12 , arr[j]= 22 , arr= [11, 25, 12, 22, 64]
i= 1 , j= 4 , arr[min_index]= 12 , arr[j]= 64 , arr= [11, 25, 12, 22, 64]

i= 2 , j= 3 , arr[min_index]= 25 , arr[j]= 22 , arr= [11, 12, 25, 22, 64]
i= 2 , j= 4 , arr[min_index]= 22 , arr[j]= 64 , arr= [11, 12, 25, 22, 64]

i= 3 , j= 4 , arr[min_index]= 25 , arr[j]= 64 , arr= [11, 12, 22, 25, 64]

'''
