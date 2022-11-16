def mk_dict():
    my_dict = dict()
    count=1
    for row in range(4):
        for col in range(3):
                my_dict[count]=(row,col)
                count+=1
    return my_dict

def get_len(c_l,c_r,number,my_dict):

    left=my_dict[c_l]
    right=my_dict[c_r]
    t = my_dict[number]
    ll= abs(left[0]-t[0]) + abs(left[1]-t[1])
    rl= abs(right[0]-t[0]) + abs(right[1]-t[1])
    return ll,rl

def solution(numbers, hand):
    my_dict = mk_dict()
    c_l = 10
    c_r = 12
    li_ans = []
    for number in numbers:
        if number == 0 :
            number = 11
        if number in [1,4,7]:
            li_ans.append('L')
            c_l = number

        if number in [3,6,9]:
            li_ans.append('R')
            c_r = number

        elif number in [2,5,8,11]:
            ll,lr=get_len(c_l,c_r,number,my_dict)
            if ll < lr:
                li_ans.append('L')
                c_l = number
            elif ll > lr:
                li_ans.append('R')
                c_r = number
            elif (ll == lr) and (hand == 'left'):
                li_ans.append('L')
                c_l = number
            elif (ll == lr) and (hand == 'right'):
                li_ans.append('R')
                c_r = number


    answer = ''.join(li_ans)
    return answer
