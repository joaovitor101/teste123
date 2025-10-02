def main():
    N = int(input().strip())
    coeffs = list(map(int, input().split()))
    
    # Representar polinômio como inteiro em binário
    poly = 0
    for c in coeffs:
        poly = (poly << 1) | c
    
    target = 1  # polinômio final
    steps = 0
    
    while poly != target:
        if poly & 1:  # se tem termo constante
            # P(x)*(x+1) + 1  → (P << 1) ^ P ^ 1
            poly = (poly << 1) ^ poly ^ 1
        else:
            # divide por x  → shift para direita
            poly >>= 1
        steps += 1
    
    print(steps)

if __name__ == "__main__":
    main()
