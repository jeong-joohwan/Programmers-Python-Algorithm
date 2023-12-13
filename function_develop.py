def solution(progresses, speeds):
    answer = []
    while progresses:
        result=0
        for i in range(len(progresses)):
            progresses[i]+=speeds[i]
            
        while progresses and progresses[0]>=100:
            result+=1
            progresses.pop(0)
            speeds.pop(0)
        if result>0:
            answer.append(result)
        
    return answer