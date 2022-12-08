def solution(nums):
    n = len(nums)/2
    var_n=len(set(nums))

    if n >= var_n:
        answer = var_n
    elif n <= var_n:
        answer = n

    return answer
