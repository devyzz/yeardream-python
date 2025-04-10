def inorder(node, depth, result=None):
    if result is None:
        result = []

    if node is None:
        return result

    inorder(node.left, depth + 1, result)  # 왼쪽 서브트리 탐색
    result.append(node)  # 현재 노드 저장
    node.depth = depth  # 노드에 깊이 정보 추가
    inorder(node.right, depth + 1, result)  # 오른쪽 서브트리 탐색

    return result

# 중위 순회를 통해 노드의 위치를 '열번호'처럼 간주
# 각 깊이별로 가장 왼쪽, 오른쪽에 있는 노드의 인덱스를 기록
# 너비 = (오른쪽 인덱스 - 왼쪽 인덱스 + 1)로 계산
# 가장 너비가 큰 레벨을 찾아 반환

def getWidth(myTree):
    result = inorder(myTree, 1)
    n = len(result)

    left = [1001] * 1000
    right = [-1] * 1000
    maxDepth = 0

    for i in range(n):          # 중위 순회의 인덱스(i)가 트리 상의 `열번호` 역할을 함.
        d = result[i].depth     # 해당 노드가 위치한 깊이

        left[d] = min(left[d], i)   # 각 깊이에서 가장 왼쪽에 등장한 인덱스와, 가장 오른쪽에 등장한 인덱스 갱신
        right[d] = max(right[d], i)
        maxDepth = max(maxDepth, d) # 동시에 최대 깊이도 갱신

    ansDepth = 0        # 너비가 가장 큰 레벨
    ansWidth = 0        # 그 레벨의 너비 값

    for i in range(1, maxDepth + 1):
        temp = right[i] - left[i] + 1

        if ansWidth < temp:
            ansDepth = i
            ansWidth = temp

    return (ansDepth, ansWidth)