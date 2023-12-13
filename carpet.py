def solution(brown, yellow):
    answer = []
    result=brown+yellow
    s=0
    g=result//s
    
    while(g>=s):
        if (g-2)*(s-2)==yellow:
            answer=[g,s]
            break
        g-=1
        s=result//g                                                                                                                                              
    return answer