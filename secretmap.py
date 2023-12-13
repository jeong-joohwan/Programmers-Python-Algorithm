def solution(n, arr1, arr2):
    answer = []
    for i in range(n):
        bin_ans=bin(arr1[i] | arr2[i])[2:]
        ans='0'*(n-len(bin_ans))+bin_ans
        ans=ans.replace("1","#")
        ans=ans.replace("0"," ")
        answer.append(ans)
    return answer