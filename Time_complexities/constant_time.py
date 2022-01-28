'''
Constant Time — O(1)

An algorithm is said to have a constant time when it is not dependent on the input data (n).

example:

if a > b:
    return True
else:
    return False
'''

def get_first(data):
    return data[0]
    
if __name__ == '__main__':
    data = [1, 2, 9, 8, 3, 4, 7, 6, 5]
    print(get_first(data))

