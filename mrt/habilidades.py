def solve():
    n, k = map(int, input().split())
    
    students = []
    for i in range(n):
        skills_str = input().strip()
        skills_mask = 0
        for j, bit in enumerate(skills_str):
            if bit == '1':
                skills_mask |= (1 << j)
        students.append(skills_mask)
    
    from collections import defaultdict
    skill_groups = defaultdict(list)
    for i, mask in enumerate(students):
        skill_groups[mask].append(i)
    
    m = int(input())
    
    special_queries = []
    for _ in range(m):
        special_str = input().strip()
        special_mask = 0
        for j, bit in enumerate(special_str):
            if bit == '1':
                special_mask |= (1 << j)
        special_queries.append(special_mask)
    
    results = []
    for special_mask in special_queries:
        count = 0
        
        valid_students = []
        for i, student_mask in enumerate(students):
            if (student_mask & special_mask) == student_mask:
                valid_students.append(i)
        
        for i in range(len(valid_students)):
            for j in range(i + 1, len(valid_students)):
                for k in range(j + 1, len(valid_students)):
                    student_i = valid_students[i]
                    student_j = valid_students[j]
                    student_k = valid_students[k]
                    
                    team_skills = students[student_i] | students[student_j] | students[student_k]
                    
                    if team_skills == special_mask:
                        count += 1
        
        results.append(count)
    
    for result in results:
        print(result)

if __name__ == "__main__":
    solve()
