import sys
n = int(input())
words = []
vectors = {}
for _ in range(n):
    parts = input().split()
    word = parts[0]
    x, y = int(parts[1]), int(parts[2])
    words.append(word)
    vectors[word] = (x, y)

m = int(input())
knowledge = input().split()
if m > len(knowledge):
    remaining = m - len(knowledge)
    knowledge.extend(input().split())

q, k = map(int, input().split())
for _ in range(q):
    parts = input().split()
    f = int(parts[0])
    query = parts[1:]

    predicted = "*"
    for window in range(k, 0, -1):
        if window > len(query):
            continue
        suffix = query[-window:]
        candidates = []
        for j in range(len(knowledge) - window):
            if knowledge[j:j+window] == suffix and knowledge[j+window] in vectors:
                candidates.append(knowledge[j+window])
        if candidates:
            sum_x = sum(vectors[c][0] for c in candidates)
            sum_y = sum(vectors[c][1] for c in candidates)
            best_word = ""
            best_score = float('-inf')
            for word in words:
                score = vectors[word][0] * sum_x + vectors[word][1] * sum_y
                if score > best_score:
                    best_score = score
                    best_word = word
            predicted = best_word
            break
    print(" ".join(query + [predicted]))

