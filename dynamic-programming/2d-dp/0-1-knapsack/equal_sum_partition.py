#Recursive Solution

def equal_sum_partition_rec(arr):
    if sum(arr) % 2 != 0:
        return False
    return equal_sum_partition_util_rec(arr,sum(arr),len(arr))

def equal_sum_partition_util_rec(arr,sum,n):
    if(sum == 0):
        return True
    if(n == 0 and sum > 0):
        return False
    
    if arr[n-1] <= sum:
        return equal_sum_partition_util_rec(arr,sum-arr[n-1],n-1) or equal_sum_partition_util_rec(arr,sum,n-1)
    else:
        return equal_sum_partition_util_rec(arr,sum,n-1)

#Memoization Solution
def equal_sum_partition_mem(arr):
    if sum(arr) % 2 != 0:
        return False
    row,col = len(arr)+1,sum(arr)+1
    dp = [[-1 for x in range(0,col)] for y in range(0,row)]
    return equal_sum_partition_util_mem(arr,sum(arr),len(arr),dp)

def equal_sum_partition_util_mem(arr,sum,n,dp):
    if(sum == 0):
        return True
    if(n == 0 and sum > 0):
        return False
    if dp[n][sum] != -1:
        return dp[n][sum]
    
    if arr[n-1] <= sum:
        dp[n][sum] = equal_sum_partition_util_mem(arr,sum-arr[n-1],n-1,dp) or equal_sum_partition_util_mem(arr,sum,n-1,dp)
    else:
        dp[n][sum] = equal_sum_partition_util_mem(arr,sum,n-1,dp)
    return dp[n][sum]

#Tabular Solution
def equal_sum_partition_tabular(arr):
    if sum(arr) % 2 != 0:
        return False
    row,col = len(arr)+1,sum(arr)+1
    dp = [[False for x in range(0,col)] for y in range(0,row)]
    # First col initialization 
    for i in range(row):
      dp[i][0] = True
    
    return equal_sum_partition_util_tabular(arr,sum(arr),len(arr),dp)


def equal_sum_partition_util_tabular(arr,sum,n,dp):
    for i in range(n+1):
        for j in range(sum+1):
            if arr[i-1] <= j:
                dp[i][j] = dp[i-1][j-arr[i-1]] or dp[i-1][j]
            else:
                dp[i][j] = dp[i-1][j]
    return dp[-1][-1]
    
if __name__ == "__main__":
    arr = [1,5,11,5]
    #print(equal_sum_partition_rec(arr))
    #print(equal_sum_partition_mem(arr))
    print(equal_sum_partition_tabular(arr))