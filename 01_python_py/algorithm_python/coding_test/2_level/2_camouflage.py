def solution(clothes):
    my_dict = dict()
    for c in clothes:
        if c[-1] in my_dict:
            my_dict[c[-1]] += 1
        elif c[-1] not in my_dict:
            my_dict[c[-1]] = 1

    answer = 1
    for value in my_dict.values():
        answer *= (value+1)

    answer -= 1

    return answer

