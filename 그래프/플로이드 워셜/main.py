INF = 999999
v = int(input()) #정점 개수
e = int(input()) #간선 개수
ad = [[INF]*v for i in range(0, v)] #인접 행렬

for i in range(0, e):
    v1, v2, w = list(map(int, input().split()))
    ad[v1][v2] = w

for i in range(0, v):
    ad[i][i] = 0

#t: 경유지, s: 출발지, en: 도착지
for t in range(0, v):
    for s in range(0, v):
        for en in range(0, v):
            # 경유지를 거쳐가는 경로가 INF 보다 크거나 같으면 그냥 INF 값을 저장
            t_route = ad[s][t]+ad[t][en]
            if(t_route >= INF): t_route = INF

            ad[s][en] = min(ad[s][en], t_route)

for ad_item in ad:
    print(ad_item)