def search(list,n):
    i=0
    while i<len(list):
        if list[i] == n:    
            return True
        i = i+1
    return False

list = [5,8,4,6,9,2]
n = 10

if search(list,n):
    print("Found")
else:
    print("Not Found")

'''
i= 0,   0<6,    list[0]=5,  5 != 10
i= 1,   0<6,    list[1]=8,  8 != 10
i= 2,   0<6,    list[2]=4,  4 != 10
i= 3,   0<6,    list[3]=6,  6 != 10
i= 4,   0<6,    list[4]=9,  9 != 10
i= 5,   0<6,    list[5]=2,  12 != 10
i= 6,   6<6, return false
'''