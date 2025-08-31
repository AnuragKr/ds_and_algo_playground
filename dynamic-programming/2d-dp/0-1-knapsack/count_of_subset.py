#Recursive Solution

def count_of_subset_sum_rec(arr,sum):
    return count_of_subset_sum_util_rec(arr,sum,len(arr))

def count_of_subset_sum_util_rec(arr,sum,n):
    if(n == 0 and sum == 0):
        return 1
    if(n == 0 and sum > 0):
        return 0
    
    if arr[n-1] <= sum:
        return count_of_subset_sum_util_rec(arr,sum-arr[n-1],n-1) + count_of_subset_sum_util_rec(arr,sum,n-1)
    else:
        return count_of_subset_sum_util_rec(arr,sum,n-1)

#Memoization Solution
def count_of_subset_sum_mem(arr,sum):
    row,col = len(arr)+1,sum+1
    dp = [[-1 for x in range(0,col)] for y in range(0,row)]
    return count_of_subset_sum_util_mem(arr,sum,len(arr),dp)

def count_of_subset_sum_util_mem(arr,sum,n,dp):
    if(n == 0 and sum == 0 ):
        return 1
    if(n == 0 and sum > 0):
        return 0
    if dp[n][sum] != -1:
        return dp[n][sum]
    
    if arr[n-1] <= sum:
        dp[n][sum] = count_of_subset_sum_util_mem(arr,sum-arr[n-1],n-1,dp) + count_of_subset_sum_util_mem(arr,sum,n-1,dp)
    else:
        dp[n][sum] = count_of_subset_sum_util_mem(arr,sum,n-1,dp)
    return dp[n][sum]

#Tabular Solution
def count_of_subset_sum_tabular(arr,sum):
    row,col = len(arr)+1,sum+1
    dp = [[0]*(col) for _ in range(0,row)]

    dp[0][0] = 1
    return count_of_subset_sum_util_tabular(arr,sum,len(arr),dp)


def count_of_subset_sum_util_tabular(arr,sum,n,dp):
    for i in range(1,n+1):
        for j in range(sum+1):
            if arr[i-1] <= j:
                dp[i][j] = dp[i-1][j-arr[i-1]] + dp[i-1][j]
            else:
                dp[i][j] = dp[i-1][j]
    return dp[n][sum]
    
if __name__ == "__main__":
    arr = [1,1,1,1,1]
    sum = 3
    print(count_of_subset_sum_rec(arr,sum))
    #print(count_of_subset_sum_mem(arr,sum))
    #print(count_of_subset_sum_tabular(arr,sum))