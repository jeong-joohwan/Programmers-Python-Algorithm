def solution(s, n):
    lower = "abcdefghijklmnopqrstuvwxyz"
    upper = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    answer = ''
    for i in s:
        if i in lower:
            a=lower.find(i)+n
            if a>=26:
                a-=26
            answer+=lower[a]
        elif i in upper:
            a=upper.find(i)+n
            if a>=26:
                a-=26
            answer+=upper[a]
        else:
            answer+=" "
        
            
            
    return answer