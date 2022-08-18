inp = [4, 3, 1, 2]

def calcImbalance(sub):
    res = 0
    if len(sub) == 1:
        return res
    for i in range(1, len(sub)):
        if sub[i] - sub[i - 1] > 1:
            res += 1
    return res

def findTotalImbalance(rank):
    res = 0
    n = len(rank)
    for i in range(n - 1):
        for j in range(i + 2, n + 1):
            sub = rank[i:j]
            sub = sorted(sub)
            res += calcImbalance(sub)
    return res

print(findTotalImbalance(inp))