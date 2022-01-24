def get_sum(arr,n):     #n --> length of array
    sum = 0
    for i in range(n):
        sum += arr[i]
        i += i
    return sum

print(get_sum([1,2,3,4],4))