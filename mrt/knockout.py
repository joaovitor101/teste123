MOD = 10**9 + 7

def minimo_jogadores(A, B):
    E = 0
    for k in range(A+B-1):
        L = max(0, k - (B - 1))
        R = min(k, A - 1)
        if L > R:
            continue

        v2min = None
        for v in range(L, R+1):
            carries = (v & (k - v)).bit_count()
            if v2min is None or carries < v2min:
                v2min = carries

        E = max(E, (k+1) - v2min)

    return pow(2, E, MOD)

def main():
    A, B = map(int, input().split())
    print(minimo_jogadores(A, B))

if __name__ == "__main__":
    main()
