#Tabular Solution
def minimum_subset_sum_diff_tabular(arr):
    row,col = len(arr)+1,sum(arr)+1
    dp = [[False for x in range(0,col)] for y in range(0,row)]
    # First col initialization 
    for i in range(row):
      dp[i][0] = True

    subset_sum_util_tabular(arr,sum(arr),len(arr),dp)
    mn = float('inf')
    arr_sum = sum(arr)
    #Traversing Last Col
    for i in range(col//2+1):
        diff = arr_sum - 2*i
        if dp[-1][i] and diff >= 0:
            mn = min(mn,diff)
    return mn

def subset_sum_util_tabular(arr,sum,n,dp):
    for i in range(1,n+1):
        for j in range(1,sum+1):
            if arr[i-1] <= j:
                dp[i][j] = dp[i-1][j-arr[i-1]] or dp[i-1][j]
            else:
                dp[i][j] = dp[i-1][j]
    return dp
    
if __name__ == "__main__":
    arr = [1,5,11,5]
    diff = 1
    print(minimum_subset_sum_diff_tabular(arr))