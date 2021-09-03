## 틀린 풀이 ##
# 알파벳 순으로 방문하면 모든 곳을 방문하지 못할 수 있음 -> BFS
def solution(tickets):
    # start, end 리스트
    start = [t[0] for t in tickets]
    end = [t[1] for t in tickets]
    answer = ['ICN']; visited = [False] * len(tickets)
    for _ in range(len(tickets)):
        # (이전 방문 = start인 공항) & (아직 방문하지 않은 곳)
        index = [i for i,v in enumerate(start) if (v == answer[-1]) & (visited[i] == False)]
        value = sorted([end[i] for i in index])[0] # 알파벳 순
        answer.append(value)
        visited[[i for i in index if end[i]==value][0]] = True # 방문
    return answer
