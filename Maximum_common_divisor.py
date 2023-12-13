def solution(n, m):
    answer = []
    a=0
    b=n*m
    while(1):
        if n<m:
            if m%n==0:
                answer.append(n)
                break
            else:
                m=m-n
                
        elif m<n:
            if n%m==0:
                answer.append(m)
                break
            else:
                n=n-m
                
        else:
            answer.append(n)
    a=answer[0]
    answer.append(b/a)
    return answer