def search(arr,n,x):
    for i in range(n):
        if arr[i]==x:
            return i
    return -1

print(search([10,5,30,40,80],5,20))

# n --> length of array
# x --> element to search