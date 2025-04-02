'''
notepad 함수를 작성하세요.
'''

def notepad(s, commands) :
    chars = [*s]
    cursor = len(chars)

    for command in commands:
        direction = command.split(' ')[0]

        if direction == 'L':
            if cursor != 0:
                cursor -= 1
        elif direction == 'R':
            if cursor != len(chars):
                cursor += 1
        elif direction == 'D':
            if cursor != 0:
                chars.remove(cursor-1)
        elif direction == 'P':
            char = command.split(' ')[1]
            chars.insert(cursor,char)
            cursor += 1

    return ''.join(chars)

