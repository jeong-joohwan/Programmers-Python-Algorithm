def solution(clothes):
    answer = 1
    result={}
    for i in range(len(clothes)):
        if clothes[i][1] not in result:
            result[clothes[i][1]]=1
        else:
            result[clothes[i][1]]+=1
    for j in result.values():
        answer=answer*(j+1)
        
    return answer-1