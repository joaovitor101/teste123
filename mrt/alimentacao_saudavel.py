def main():
    N, M = map(int, input().split())
    frutas = [list(map(int, input().split())) for _ in range(N)]
    
    total = 0
    for j in range(M):  # cada turma é uma coluna
        max_col = max(frutas[i][j] for i in range(N))
        total += max_col
    
    print(total)

if __name__ == "__main__":
    main()
