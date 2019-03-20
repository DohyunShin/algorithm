'''
도착 노드까지만 탐색하는 기능, 이동거리 출력 기능은 옵션
'''
def bfs(admtrx, start, end):
	q = [] # queue
	chk = [False] * len(admtrx[0]) # 방문 노드 체크 리스트
	dstc = [0] * len(admtrx[0]) # 출발 노드 부터 각 노드까지의 이동거리(가중치의 합, 최단 경로의 거리)

	# 첫 노드 방문
	q.append(start)
	chk[start] = True
	# dstc[start] = dstc[start] + admtrx[start][start] # 필요없는 코드(방문 시 이동거리를 축적한다는 의미로..)

	while q: # queue가 비워질 때까지 반복
		sel = q.pop(0) # queue FIFO
		print(sel, dstc[sel])

		# 도착 노드까지만 탐색
		if end != -1 and end == sel:
			break

		# 방문하지 않은 모든 자식 노드 방문
		for c in range(0, len(admtrx[0])):
			if admtrx[sel][c] != 0 and chk[c] != True:
				q.append(c)
				chk[c] = True # 방문노드 체크
				dstc[c] = dstc[sel] + admtrx[sel][c] # 이동거리 축적


	return


def main():
	# 입력 및 인접 행렬 만들기
	print("input>node edge directed")
	n, e, d = list(map(int, input().split()))

	print("input>start end weight")
	admtrx = [[0] * n for i in range(n)]
	for i in range(e):
		start, end, w = list(map(int, input().split()))
		admtrx[start][end] = w
		if d == 0:
			admtrx[end][start] = w

	bfs(admtrx, 0, -1) # 전부 탐색

	return


if __name__ == "__main__":
	main()