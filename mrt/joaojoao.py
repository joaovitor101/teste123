def main():
    nums = list(map(int, input().split()))
    # se a linha puder vir quebrada em várias linhas, use:
    # import sys
    # nums = list(map(int, sys.stdin.read().split()))
    distinct = set(nums)
    missing = 4 - len(distinct)
    print(missing)

if __name__ == "__main__":
    main()
