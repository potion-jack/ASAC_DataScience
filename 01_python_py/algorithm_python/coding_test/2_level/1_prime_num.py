def convert_k_system(n,k):
    ans = ''
    while n // k != 0:
        ans = ans + str(n%k)
        n = n // k
    ans = ans + str(n%k)
    return ans[::-1]

def is_prime(num):
    if num == 1:
        return False
    elif num == 2:
        return True

    _list=[i for i in range(3,int(num**0.5)+1) if i%2 !=0]
    for i in _list[::-1]:
        if num%i == 0:
            return False
    return True

import collections

def solution(n, k):
    by_k = convert_k_system(n,k)
    by_k_li = by_k.split('0')
    my_col = collections.Counter([i for i in by_k_li if len(i)>0])
    tot =0
    for i in my_col:
        if is_prime(int(i)):
            tot += my_col[i]

        else:
            pass
    answer = tot
    return answer
