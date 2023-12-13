def solution(numbers):
    answer = []
    numbers.sort()
    a=0
    for i in range(len(numbers)-1):
        for j in range(len(numbers)):
            if i<j:
                a=numbers[i]+numbers[j]
                answer.append(a)
                a=0
    answer=set(answer)
    answer=list(answer)
    answer.sort()
    return answer