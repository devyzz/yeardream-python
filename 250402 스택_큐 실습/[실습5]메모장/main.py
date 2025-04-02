from notepad import notepad


def main():
    s = input()

    n = int(input())

    commands = []

    for i in range(n):
        commands.append(input())

    print(notepad(s, commands))


if __name__ == "__main__":
    main()


