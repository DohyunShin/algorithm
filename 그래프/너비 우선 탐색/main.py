# 옵션: 이동거리 출력
def bfs_admtrx(admtrx, start_node, end_node):
	bfs_queue = []
	visited_check_list = [False] * len(admtrx)
	distance_list = [0] * len(admtrx) # 출발 노드 부터 각 노드까지의 이동거리(가중치의 합, 최단 경로의 거리)

	# 첫 노드 방문
	bfs_queue.append(start_node)
	visited_check_list[start_node] = True
	# distance_list[start_node] = distance_list[start_node] + admtrx[start_node][start_node] # 필요없는 코드(방문 시 이동거리를 축적한다는 의미로..)

	while bfs_queue: # queue가 비워질 때까지 반복
		selected_node = bfs_queue.pop(0) # queue FIFO
		print("node: {0}, weight: {1}".format(selected_node, distance_list[selected_node]))

		# 도착 노드까지만 탐색
		if end_node == selected_node:
			break

		# 선택된(꺼낸) 노드의 방문하지 않은 모든 자식 노드 방문
		for i in range(0, len(admtrx[0])):
			if admtrx[selected_node][i] != 0 and visited_check_list[i] != True:
				bfs_queue.append(i)
				visited_check_list[i] = True # 방문노드 체크
				distance_list[i] = distance_list[selected_node] + admtrx[selected_node][i] # 이동거리 축적

	return


def bfs_adlist(adlist, start_node, end_node):
	bfs_queue = []
	visited_check_list = [False] * len(adlist)
	distance_list = [0] * len(adlist)  # 출발 노드 부터 각 노드까지의 이동거리(가중치의 합, 최단 경로의 거리)

	# 첫 노드 방문
	bfs_queue.append(start_node)
	visited_check_list[start_node] = True
	# distance_list[start_node] = distance_list[start_node] + 0 # 필요없는 코드(방문 시 이동거리를 축적한다는 의미로..)

	while bfs_queue: # queue가 비워질 때까지 반복
		selected_node = bfs_queue.pop(0) # queue FIFO
		print("node: {0}, weight: {1}".format(selected_node, distance_list[selected_node]))

		# 도착 노드까지만 탐색
		if end_node == selected_node:
			break

		# 선택된(꺼낸) 노드의 방문하지 않은 모든 자식 노드 방문
		for child_node in adlist[selected_node].keys():
			if adlist[selected_node][child_node] != 0 and visited_check_list[child_node] != True:
				bfs_queue.append(child_node)
				visited_check_list[child_node] = True  # 방문노드 체크
				distance_list[child_node] = distance_list[selected_node] + adlist[selected_node][child_node]  # 이동거리 축적

	return


def main():
	node_cnt = int(input("node count(int): "))
	edge_cnt = int(input("edge count(int): "))
	is_direction = bool(int(input("direction graph(int, 0: False, 1: True): ")))

	admtrx = [[0] * node_cnt for _ in range(node_cnt)]
	adlist = [{} for _ in range(node_cnt)]

	print("[start node] [end node] [weight]")
	for i in range(edge_cnt):
		start_node, end_node, weight = list(map(int, input(str(i + 1)+")").split()))

		admtrx[start_node][end_node] = weight
		adlist[start_node][end_node] = weight

		if not is_direction:
			admtrx[end_node][start_node] = weight
			adlist[end_node][start_node] = weight

	print("< adjacency matrix dfs result >")
	bfs_admtrx(admtrx, 0, len(admtrx) - 1)
	print("< adjacency list dfs result >")
	bfs_adlist(adlist, 0, len(adlist) - 1)

	return


if __name__ == "__main__":
	main()