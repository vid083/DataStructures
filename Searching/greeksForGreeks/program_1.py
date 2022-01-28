# https://practice.geeksforgeeks.org/problems/search-an-element-in-an-array-1587115621/1/?track=DSASP-Searching&batchId=154#

'''
Input:
n = 4
arr[] = {1,2,3,4}
x = 3
Output: 2
Explanation: There is one test case 
with array as {1, 2, 3 4} and element 
to be searched as 3.  Since 3 is 
present at index 2, output is 2.

Expected Time Complexity: O(n).
Expected Auxiliary Space: O(1). 
'''
def search(self,arr, N, X):
        for i in range(N):
            if (arr[i] == X):
                return i
        return -1