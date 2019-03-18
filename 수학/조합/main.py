# n: 총 개수, k: 선택 개수
# 재귀 (Recursion)
def cb_recursion(n, k):
    """
    if k == 0 or k == n:
	    return 1
    else:
        return cb_recursion(n-1, k-1) + cb_recursion(n-1, k)
    """
    if k == 1:
        return n
    elif k == n:
        return 1
    else:
        return cb_recursion(n - 1, k - 1) + cb_recursion(n - 1, k)

# 동적 계획법 (Dynamic Programming, DP)
m = [[0] * 1000 for i in range(0, 1000)] # 메모이제이션(Memoization)

def cb_dp(n, k):
    if m[n][k] != 0:
        return m[n][k]

    """
    if k == 0 or k == n:
       m[n][k] = 1
       return m[n][k]
    """
    if k == 1:
        m[n][k] = n
        return m[n][k]
    elif k == n:
        m[n][k] = 1
        return m[n][k]
    else:
        m[n][k] = cb_dp(n-1, k-1) + cb_dp(n-1, k)
        return m[n][k]

# 출력
# d: 데이터 리스트, t: 데이터 리스트의 타겟 인덱스, s: 선택된 데이터 인덱스 저장 리스트, p: 리스트 s의 저장 위치(pos)
def cb_print(d, n, k, t, s, p):
    if k == 0:
        tmp = []
        # 출력 시 pos는 리스트 s의 출력 개수가 된다.
        for i in range(0, p):
            tmp.append(d[s[i]])
        print(tmp)
        return 1
    # 목표 만큼 선택하지 못하고 종료할 경우(모두 선택한 경우는 위에서 걸러진다.)
    elif t == n:
        return 0
    else:
        s[p] = t
        # t을 선택하는 경우와 선택하지 않는 경우
        # t를 선택하지 않는 경우 선택된 데이터의 저장 배열 pos를 증가시키지 않고 다음 대상으로 탐색을 진행한다.
        # 다음 시도에 같은 pos에 저장된다.
        return cb_print(d, n, k - 1, t + 1, s, p + 1) + cb_print(d, n, k, t + 1, s, p)


print("Combination_Recursion: ", cb_recursion(4, 2))
print("Combination_DP: ", cb_dp(4,2))
print("Combination_Print")
d = [1, 2, 3, 4]
s = [0] * len(d)
print(cb_print(d, len(d), 2, 0, s, 0))