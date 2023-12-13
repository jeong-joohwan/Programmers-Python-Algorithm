def solution(d, budget):
    d.sort()
    sum=0
    for i in range(len(d)):
        sum+=d[i]
        if sum>budget:
            return i
        elif sum==budget:
            return i+1
    return i+1