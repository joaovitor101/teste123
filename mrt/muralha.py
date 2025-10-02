import sys
from typing import List


def read_input() -> (int, int, List[int]):
    while True:
        line = sys.stdin.readline()
        if line.strip():
            n, k = map(int, line.split())
            break
    heights: List[int] = []
    while len(heights) < n:
        parts = sys.stdin.readline().split()
        if not parts:
            continue
        heights.extend(map(int, parts))
    return n, k, heights[:n]


def can_reach_minimum(heights: List[int], k: int, target: int) -> bool:
    n = len(heights)
    need = [max(0, target - h) for h in heights]
    l = 0
    while l < n and need[l] == 0:
        l += 1
    if l == n:
        return True
    r = n - 1
    while r >= 0 and need[r] == 0:
        r -= 1
    if r - l + 1 > k:
        return False
    for j in range(l, r + 1):
        if need[j] + (r - j) > k:
            return False
    return True


def solve() -> None:
    n, k, heights = read_input()
    low = min(heights)
    high = max(heights) + k
    ans = low
    while low <= high:
        mid = (low + high) // 2
        if can_reach_minimum(heights, k, mid):
            ans = mid
            low = mid + 1
        else:
            high = mid - 1
    print(ans)


if __name__ == "__main__":
    solve()


