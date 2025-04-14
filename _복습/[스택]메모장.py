# 메모장은 커서의 위치를 기준으로 단어를 삭제하거나 추가할 수 있습니다.
# L : 커서를 왼쪽으로 한 칸 이동, 커서가 맨 왼쪽인 경우는 변화 X
# R : 커서를 오른쪽으로 한 칸 이동, 커서가 맨 오른쪽인 경우 아무 변화 X
# D : 커서 왼쪽의 문자 삭제, 커서가 맨 왼쪾인 경우 아무 변화 X
# P s : 임의의 알파벳 s를 커서 왼쪾에 추가

def notepad(s, commands):

    left = []
    right = []

    for char in s:
        left.append(char)

    for command in commands:
        order = command.split()[0]
        if order == 'L':
            right.append(left.pop())
        elif order == 'R':
            left.append(right.pop())
        elif order == 'P':
            char = command.split()[1]
            left.append(char)
        elif order == 'D':
            left.pop()

    result = left + right
    return ''.join(result)
 


def main():
    s = input()

    n = int(input())

    commands = []

    for i in range(n):
        commands.append(input())

    print(notepad(s, commands))

if __name__ == "__main__":
    main()
