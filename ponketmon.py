def solution(nums):
    answer = 0
    result=[]
    for i in nums:
        if len(nums)/2 != answer :
            if i not in result:
                result.append(i)
                answer+=1
                
    return answer