import math

def solve():
    n = int(input())
    stars = [tuple(map(int, input().split())) for _ in range(n)]

    # Calcular distâncias entre estrelas consecutivas
    distances = [math.hypot(stars[i+1][0] - stars[i][0], stars[i+1][1] - stars[i][1]) for i in range(n-1)]

    # Verificar se existe alguma chance (se alguma distância < 2, já dá ruim)
    for d in distances:
        if d < 2:
            print(-1)
            return

    def can_achieve_r1(r1_val):
        r = r1_val
        for i in range(len(distances)):
            d = distances[i]

            # limite superior do próximo raio
            if i + 1 < len(distances):
                max_next = distances[i+1] - 1
            else:
                max_next = float("inf")  # último raio sem restrição futura

            # intervalo válido para Ri+1
            lo = 1
            hi = min(d - r, max_next)

            if hi < lo:  # intervalo vazio
                return False

            # escolhe valor viável (não precisa ser o maior)
            r = lo  

        return True

    # Busca binária para o maior R1 possível
    left = 1
    right = math.floor(distances[0] - 1)
    result = -1
    while left <= right:
        mid = (left + right) // 2
        if can_achieve_r1(mid):
            result = mid
            left = mid + 1
        else:
            right = mid - 1

    print(result)


if __name__ == "__main__":
    solve()
