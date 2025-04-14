# 괄호가 포함된 수식이 있을 때 계산 순서 정하기
# 각 괄호가 몇번째로 계산되어야 하는 괄호인지 공백으로 구분한 결과를 리스트로 담아 반환합니다.

def find_order(expr):
    stack = []
    orders = {}
    order = 1

    for i, char in enumerate(expr):
        if char == '(':
            stack.append(i)
        elif char == ')':
            open_idx = stack.pop()
            orders[open_idx] = order
            orders[i] = order
            order += 1

    return [orders[i] for i in range(len(expr)) if i in orders]

def main():
    p = input()
    print(*find_order(p))

if __name__ == "__main__":
    main()
