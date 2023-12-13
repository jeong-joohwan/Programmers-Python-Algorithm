import heapq
def solution(scoville, K):
    answer=0
    heapq.heapify(scoville)
    while(True):
        if scoville[0]>K:
            break
        elif len(scoville)==1:
            return -1
        else:
            a=heapq.heappop(scoville)
            b=heapq.heappop(scoville)
            c=a+(b*2)
            heapq.heappush(scoville,c)
            
            answer+=1
            
    
    
    return answer