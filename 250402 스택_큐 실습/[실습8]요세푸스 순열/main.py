from josephus import josephus_sequence


def main():
    '''
    이 부분은 수정하지 마세요.
    '''

    n, k = [int(v) for v in input().split()]

    print(josephus_sequence(n, k))

if __name__ == "__main__":
    main()


