import sys

def count_winnable_subsets(N, pieces):
    M = 1 << N
    par = [0] * M
    verts = [0] * M
    A = [p[0] for p in pieces]
    B = [p[1] for p in pieces]

    for mask in range(1, M):
        lsb = mask & -mask
        idx = lsb.bit_length() - 1
        prev = mask ^ lsb
        a, b = pieces[idx]
        par[mask] = par[prev] ^ (1 << a) ^ (1 << b)
        verts[mask] = verts[prev] | (1 << a) | (1 << b)

    ans = 0
    for mask in range(1, M):
        if par[mask].bit_count() > 2:
            continue
        vmask = verts[mask]
        if vmask == 0:
            continue
        start = (vmask & -vmask).bit_length() - 1
        visited = 0
        stack = [start]
        while stack:
            v = stack.pop()
            if (visited >> v) & 1:
                continue
            visited |= (1 << v)
            mm = mask
            while mm:
                l = mm & -mm
                i = l.bit_length() - 1
                mm ^= l
                u = A[i]; w = B[i]
                if u == v and ((visited >> w) & 1) == 0:
                    stack.append(w)
                elif w == v and ((visited >> u) & 1) == 0:
                    stack.append(u)
        if (visited & vmask) == vmask:
            ans += 1
    return ans

def main():
    try:
        T = int(input().strip())
    except Exception:
        return

    outputs = []
    for _ in range(T):
        line = input().strip()
        while line == "":
            line = input().strip()
        N = int(line)
        pieces = []
        for _ in range(N):
            a, b = map(int, input().split())
            pieces.append((a-1, b-1))
        outputs.append(str(count_winnable_subsets(N, pieces)))

    print("\n".join(outputs))

if __name__ == "__main__":
    main()
