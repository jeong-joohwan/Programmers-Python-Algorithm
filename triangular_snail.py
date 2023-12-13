def solution(n):
    result=[]
    for i in range(n):
        result.append([0]*(i+1)) ## 삼각형모양의 행렬 만들기
    #print(result)
    x=0
    y=-1
    cnt = 1
    for i in range(n):
        for j in range(i,n):
            if i%3 == 0 :
                y +=1
            elif i%3 == 1:
                x +=1
            else:
                x -=1
                y -=1
            result[y][x] = cnt
            cnt +=1
            #print(result)
    answer = []
    for i in range(n):
        answer += result[i]
    return answer