def main():
    nums = list(map(int, input().split()))
    distinct = set(nums)
    missing = 4 - len(distinct)
    print(missing)

if __name__ == "__main__":
    main()
