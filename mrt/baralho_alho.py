from math import gcd
from functools import reduce

# Algoritmo para resolver congruências pelo Teorema Chinês do Resto
def crt(remainders, moduli):
    x, lcm = 0, 1
    for r, m in zip(remainders, moduli):
        g = gcd(lcm, m)
        if (r - x) % g != 0:
            return None  # Sem solução
        # Atualizar usando expansão da congruência
        p, q = lcm // g, m // g
        inv = pow(p, -1, q)
        x += (r - x) // g * inv % q * lcm
        lcm *= q
        x %= lcm
    return x

def main():
    N = int(input().strip())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    P = [p-1 for p in map(int, input().split())]  # zero-indexado
    
    visited = [False] * N
    remainders, moduli = [], []
    
    for i in range(N):
        if not visited[i]:
            cycle = []
            j = i
            while not visited[j]:
                visited[j] = True
                cycle.append(j)
                j = P[j]
            
            # extrair valores
            a_vals = [A[idx] for idx in cycle]
            b_vals = [B[idx] for idx in cycle]
            m = len(cycle)
            
            # tentar alinhar com deslocamento
            found = False
            for shift in range(m):
                if all(a_vals[(t - shift) % m] == b_vals[t] for t in range(m)):
                    remainders.append(shift % m)
                    moduli.append(m)
                    found = True
                    break
            if not found:
                print("IMPOSSIVEL")
                return
    
    k = crt(remainders, moduli)
    if k is None:
        print("IMPOSSIVEL")
    elif k > 10**9:
        print("DEMAIS")
    else:
        print(k)

if __name__ == "__main__":
    main()
