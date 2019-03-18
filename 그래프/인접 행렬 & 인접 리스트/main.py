#인접 행렬
print("인접 행렬")
isDirected = bool(int(input())) #True 이면 유향 그래프, False 이면 무향 그래프
vertexCnt = int(input())
edgeCnt = int(input())

adjacencyMatrix = [[0]*vertexCnt for i in range(0, vertexCnt)]

for edgeIndex in range(0, edgeCnt):
    v1, v2, w = list(map(int, input().split()))
    adjacencyMatrix[v1][v2] = w

    #무향 그래프인 경우 반대 방향도 똑같은 가중치 저장
    if not isDirected:
        adjacencyMatrix[v2][v1] = w

#행렬 형태로 출력
for row in adjacencyMatrix:
    print(row)




#인접 리스트
print("인접 리스트")
WEIGHT = False

isDirected = bool(int(input())) #True 이면 유향 그래프, False 이면 무향 그래프
vertexCnt = int(input())
edgeCnt = int(input())

if WEIGHT:
    adjacencyList = [{} for i in range(0, vertexCnt)]

    for edgeIndex in range(0, edgeCnt):
        v1, v2, w = list(map(int, input().split()))
        adjacencyList[v1][v2] = w

        # 무향 그래프인 경우 반대 방향도 똑같은 가중치 저장
        if not isDirected:
            adjacencyList[v2][v1] = w

    #행렬 형태로 출력
    for row in adjacencyList:
        print(row)
else:
    adjacencyList = [[] for i in range(0, vertexCnt)]

    for edgeIndex in range(0, edgeCnt):
        v1, v2 = list(map(int, input().split()))
        adjacencyList[v1].append(v2)

        # 무향 그래프인 경우 반대 방향도 똑같은 가중치 저장
        if not isDirected:
            adjacencyList[v2].append(v1)

    # 행렬 형태로 출력
    for row in adjacencyList:
        print(row)