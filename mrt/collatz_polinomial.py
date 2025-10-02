def main():
    N = int(input().strip())
    coeffs = list(map(int, input().split()))
    
    poly = 0
    for c in coeffs:
        poly = (poly << 1) | c
    
    target = 1
    steps = 0
    
    while poly != target:
        if poly & 1:
            poly = (poly << 1) ^ poly ^ 1
        else:
            poly >>= 1
        steps += 1
    
    print(steps)

if __name__ == "__main__":
    main()
