MOD = 10**9 + 7

def minimo_jogadores(A, B):
    # vamos calcular o expoente mínimo E tal que N = 2^E funciona
    
    # E será o máximo, sobre todos os estados possíveis (v,d),
    # de (rodadas até aqui) - v2(binomial)   <-- (Kummer)
    
    E = 0
    for k in range(A+B-1):  # rodada k (0 até A+B-2)
        # intervalo de vitórias possíveis até aqui
        L = max(0, k - (B - 1))
        R = min(k, A - 1)
        if L > R:
            continue

        # checamos o mínimo expoente 2-adic de C(k,v) para v no intervalo
        v2min = None
        for v in range(L, R+1):
            # Kummer: v2(C(k,v)) = nº de carries ao somar v e k-v em base 2
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
