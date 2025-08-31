#Recursive Solution

def count_of_subset_diff_rec(arr,diff_val):
    #Finding subset 
    s_one = ( sum(arr)+ diff_val)//2
    return count_of_subset_diff_util_rec(arr,s_one,len(arr))

def count_of_subset_diff_util_rec(arr,sum,n):
    if(n == 0 and sum == 0):
        return 1
    if(n == 0 and sum > 0):
        return 0
    
    if arr[n-1] <= sum:
        return count_of_subset_diff_util_rec(arr,sum-arr[n-1],n-1) + count_of_subset_diff_util_rec(arr,sum,n-1)
    else:
        return count_of_subset_diff_util_rec(arr,sum,n-1)

#Memoization Solution
def count_of_subset_diff_mem(arr,diff_val):
    #Finding subset 
    s_one = ( sum(arr)+ diff_val)//2
    row,col = len(arr)+1,s_one+1
    dp = [[-1 for x in range(0,col)] for y in range(0,row)]
    return count_of_subset_diff_util_mem(arr,s_one,len(arr),dp)

def count_of_subset_diff_util_mem(arr,sum,n,dp):
    if(n == 0 and sum == 0 ):
        return 1
    if(n == 0 and sum > 0):
        return 0
    if dp[n][sum] != -1:
        return dp[n][sum]
    
    if arr[n-1] <= sum:
        dp[n][sum] = count_of_subset_diff_util_mem(arr,sum-arr[n-1],n-1,dp) + count_of_subset_diff_util_mem(arr,sum,n-1,dp)
    else:
        dp[n][sum] = count_of_subset_diff_util_mem(arr,sum,n-1,dp)
    return dp[n][sum]

#Tabular Solution
def count_of_subset_diff_tabular(arr,diff_val):
    #Finding subset 
    s_one = ( sum(arr)+ diff_val)//2
    row,col = len(arr)+1,s_one+1
    dp = [[0]*(col) for _ in range(0,row)]

    dp[0][0] = 1
    return count_of_subset_diff_util_tabular(arr,s_one,len(arr),dp)


def count_of_subset_diff_util_tabular(arr,sum,n,dp):
    for i in range(1,n+1):
        for j in range(sum+1):
            if arr[i-1] <= j:
                dp[i][j] = dp[i-1][j-arr[i-1]] + dp[i-1][j]
            else:
                dp[i][j] = dp[i-1][j]
    return dp[n][sum]
    
if __name__ == "__main__":
    arr = [1,1,1,1,1]
    diff_val = 3
    #print(count_of_subset_diff_rec(arr,diff_val))
    #print(count_of_subset_diff_mem(arr,diff_val))
    print(count_of_subset_diff_tabular(arr,diff_val))