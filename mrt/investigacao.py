import math

def solve():
    n = int(input())
    stars = [tuple(map(int, input().split())) for _ in range(n)]

    distances = [math.hypot(stars[i+1][0] - stars[i][0], stars[i+1][1] - stars[i][1]) for i in range(n-1)]

    for d in distances:
        if d < 2:
            print(-1)
            return

    def can_achieve_r1(r1_val):
        r = r1_val
        for i in range(len(distances)):
            d = distances[i]

            if i + 1 < len(distances):
                max_next = distances[i+1] - 1
            else:
                max_next = float("inf")

            lo = 1
            hi = min(d - r, max_next)

            if hi < lo:
                return False

            r = lo

        return True

    left = 1
    right = math.floor(distances[0] - 1)
    result = -1
    for r1 in range(right, left - 1, -1):
        if can_achieve_r1(r1):
            result = r1
            break

    print(result)

if __name__ == "__main__":
    solve()