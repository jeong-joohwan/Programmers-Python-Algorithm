from itertools import permutations

def solution(numbers):
    answer = 0
    cnt=[]
    for i in range(1,len(numbers)+1):
        result=permutations(numbers,i)
        for j in result:
            cnt.append(int("".join(j)))
    cnt=list(set(cnt))
    for i in cnt:
        if i < 2:
            pass
        elif i == 2:
            answer += 1
           
        else:
            for j in range(2, i):
                if i % j == 0:
                    break
                elif j ==i-1:
                    answer += 1
                    
    return answer