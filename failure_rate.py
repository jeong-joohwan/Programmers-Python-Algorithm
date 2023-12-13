def solution(N, stages):
    answer = {}
    total_len=len(stages)
    for i in range(1,N+1):
        if total_len!=0:
            answer[i]=stages.count(i)/total_len
            total_len-=stages.count(i)
        else:
            answer[i]=0
    answer= sorted(answer, key=lambda x : answer[x], reverse=True)      
    return answer