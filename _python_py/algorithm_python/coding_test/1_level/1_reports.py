import collections
def solution(id_list, report, k):
    my_dict = dict()
    for __ in set(report):
        a = __.split()[0]
        b = __.split()[1]

        if a not in my_dict:
            my_dict[a] = [b]

        elif a in my_dict:
            my_dict[a].append(b)

    reports=sum(my_dict.values(),[])
    a=collections.Counter(reports)
    target = []

    for name,count in zip(a.keys(),a.values()):
        if count >= k:
            target.append(name)
    _dict = dict()
    for name in id_list:
        _dict[name] = 0
    for name,report in zip(my_dict.keys(),my_dict.values()):
        for t in target:
            if t in report:
                _dict[name] += 1
    answer = list(_dict.values())
    return answer
