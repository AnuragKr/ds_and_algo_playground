def knapsackProblem(items, capacity):
    knapsackValues = [[0 for x in range(0,capacity+1)] for y in range(0,len(items)+1)]
    for i in range(1,len(items)+1):
        currentValue = items[i-1][0]
        currentWeight = items[i-1][0]
        for j in range(0,capacity+1):
            if currentWeight <= j:
                knapsackValues[i][j] = max(currentValue + knapsackValues[i-1][j-currentWeight],
                                            knapsackValues[i-1][j])
            else:
                knapsackValues[i][j] = knapsackValues[i-1][j]
    return [knapsackValues[-1][-1], getSequence(knapsackValues,items)]

def getSequence(knapsackValues,items):
    i = len(knapsackValues)-1
    c = len(knapsackValues[0])-1
    sequence = []
    while i>0 and c>0:
        if knapsackValues[i][c] == knapsackValues[i-1][c]:
            i -= 1
        else:
            sequence.append(i-1)
            c -= items[i-1][1]
            i -= 1
        
    return list(reversed(sequence))


items = [[1,2],[4,3],[5,6],[6,7]]
capacity = 10
print(knapsackProblem(items,capacity))