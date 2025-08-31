#Recursive Solution

def subset_sum_rec(arr,sum):
    return subset_sum_util_rec(arr,sum,len(arr))

def subset_sum_util_rec(arr,sum,n):
    if(sum == 0):
        return True
    if(n == 0 and sum > 0):
        return False
    
    if arr[n-1] <= sum:
        return subset_sum_util_rec(arr,sum-arr[n-1],n-1) or subset_sum_util_rec(arr,sum,n-1)
    else:
        return subset_sum_util_rec(arr,sum,n-1)

#Memoization Solution
def subset_sum_mem(arr,sum):
    row,col = len(arr)+1,sum+1
    dp = [[-1 for x in range(0,col)] for y in range(0,row)]
    return subset_sum_util_mem(arr,sum,len(arr),dp)

def subset_sum_util_mem(arr,sum,n,dp):
    if(sum == 0):
        return True
    if(n == 0 and sum > 0):
        return False
    if dp[n][sum] != -1:
        return dp[n][sum]
    
    if arr[n-1] <= sum:
        dp[n][sum] = subset_sum_util_mem(arr,sum-arr[n-1],n-1,dp) or subset_sum_util_mem(arr,sum,n-1,dp)
    else:
        dp[n][sum] = subset_sum_util_mem(arr,sum,n-1,dp)
    return dp[n][sum]

#Tabular Solution
def subset_sum_tabular(arr,sum):
    row,col = len(arr)+1,sum+1
    dp = [[False for x in range(0,col)] for y in range(0,row)]
    # First col initialization 
    for i in range(row):
      dp[i][0] = True

    return subset_sum_util_tabular(arr,sum,len(arr),dp)


def subset_sum_util_tabular(arr,sum,n,dp):
    for i in range(1,n+1):
        for j in range(1,sum+1):
            if arr[i-1] <= j:
                dp[i][j] = dp[i-1][j-arr[i-1]] or dp[i-1][j]
            else:
                dp[i][j] = dp[i-1][j]
    return dp[-1][-1]
    
if __name__ == "__main__":
    arr = [2,3,7,8,10]
    sum = 15
    #print(subset_sum_rec(arr,sum))
    #print(subset_sum_mem(arr,sum))
    print(subset_sum_tabular(arr,sum))