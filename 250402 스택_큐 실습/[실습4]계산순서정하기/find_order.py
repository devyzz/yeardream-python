
def find_order(p):
    '''
    괄호 p가 주어질 때, 각 괄호가 몇 번째로 계산되어야 하는 괄호인지를 list로 반환합니다.
    예를 들어, p='(()())' 일 경우, [3, 1, 1, 2, 2, 3] 을 반환합니다.
    '''
    idxs = []
    orders = {}
    stack = []
    order = 0

    for idx, char in enumerate(p):
        if char == '(':
            stack.append(char)
            idxs.append(idx)
        else:
            order += 1
            pair = idxs.pop()
            orders[idx] = order
            orders[pair] = order
            stack.pop()

    sorted_order = dict(sorted(orders.items()))  # 키 기준 정렬
    return list(sorted_order.values())

print(find_order('(()())'))

