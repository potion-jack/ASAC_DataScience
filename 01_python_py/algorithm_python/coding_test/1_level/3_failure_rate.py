import collections
def solution(N, stages):
    rate = {}
    total_players = len(stages)
    for i in range(1,N+1):
        if total_players != 0:
            stage_players=stages.count(i)
            rate[i] = stage_players/total_players
            total_players -= stage_players
        elif total_players == 0:
            rate[i] = 0

    answer = sorted(rate,key=lambda x : rate[x],reverse=True)

    return answer
