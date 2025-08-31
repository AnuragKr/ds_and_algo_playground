"""
Probelm Statement -> Consider you are a thief planning to rob a store. However we can only carry a knapsack with a 
Weight W only. Each item (i) in the store has a weight (weights[i]) and a value (values[i]).
Find the maximum total value of items we can carry in knapsack

I/P -> W = 7, weights = [5,3,4,1], values = [70, 50, 40,10]
O/P -> 90
"""

def knapsack_top_down(wt,profits,w):
    row,col = len(profits)+1,w+1
    dp = [[-1 for x in range(0,col)] for y in range(0,row)]
    return knapsack_top_down_util(wt,profits,w,len(profits),dp)

def knapsack_top_down_util(wt,profits,w,n,dp):
    if n==0 or w == 0:
        return 0
    
    if dp[n][w] != -1:
        return dp[n][w]
    
    if(wt[n-1] <= w):
        dp[n][w] = max(profits[n-1] + knapsack_top_down_util(wt,profits,w-wt[n-1],n-1,dp),
                        knapsack_top_down_util(wt,profits,w,n-1,dp))
    elif(wt[n-1]>w):
        dp[n][w] = knapsack_top_down_util(wt,profits,w,n-1,dp)
    
    return dp[n][w]

def knapsack_bottom_up(wt,profits,w):
    row,col = len(profits)+1,w+1
    dp = [[-1 for x in range(0,col)] for y in range(0,row)]
    # First col initialization 
    for i in range(row):
      dp[i][0] = 0
    # First row initialization
    for j in range(col):
      dp[0][j] = 0
    return knapsack_bottom_up_util(wt,profits,w,len(profits),dp)

def knapsack_bottom_up_util(wt,profits,w,n,dp):
  for i in range(1,n+1):
    for j in range(1,w+1):
      if(wt[i-1] <= j):
        dp[i][j] = max(profits[i-1] + dp[i-1][j-wt[i-1]],dp[i-1][j])
      else:
        dp[i][j] = dp[i-1][j]
    
  return dp[n][w]

if __name__ == "__main__":
    values = [70, 50, 40,10]
    weights = [5,3,4,1]
    W = 7
    #max_profit = knapsack_top_down(weights,values,W)
    max_profit = knapsack_bottom_up(weights,values,W)
    print(f"Max Profit possible - {max_profit}")