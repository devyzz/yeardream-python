from collections import deque

def BFS(tree):
    q = deque()
    q.append(tree)
    print(tree)

    result = []

    while q:
        cur = q.popleft()   # 최초에 하나의 트리가 담겨있다가 뺐으므로 q가 비게 됨
        if cur is None:
            continue
        result.append(cur.index)

        q.append(cur.left)  # q에 다시 왼쪽, 오른쪽 트리를 넣는것
        q.append(cur.right)

    return result

# 루트 트리으 왼/오  > 루트의 왼쪽을 루트로 갖는 왼/오 > 순차적으로 밀려야 하므로 선입선출 구조가 필요.
# 그래서 큐로 구현 하는 것