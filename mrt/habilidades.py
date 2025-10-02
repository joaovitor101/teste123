def solve():
    # Ler entrada
    n, k = map(int, input().split())
    
    # Converter habilidades dos alunos para bitmasks
    students = []
    for i in range(n):
        skills_str = input().strip()
        # Converter string binária para inteiro
        skills_mask = 0
        for j, bit in enumerate(skills_str):
            if bit == '1':
                skills_mask |= (1 << j)
        students.append(skills_mask)
    
    # Agrupar alunos por suas habilidades para otimização
    from collections import defaultdict
    skill_groups = defaultdict(list)
    for i, mask in enumerate(students):
        skill_groups[mask].append(i)
    
    m = int(input())
    
    # Ler todos os subconjuntos especiais
    special_queries = []
    for _ in range(m):
        special_str = input().strip()
        # Converter string binária para inteiro
        special_mask = 0
        for j, bit in enumerate(special_str):
            if bit == '1':
                special_mask |= (1 << j)
        special_queries.append(special_mask)
    
    # Processar cada subconjunto especial e armazenar resultados
    results = []
    for special_mask in special_queries:
        # Contar equipes que formam exatamente este subconjunto
        count = 0
        
        # Otimização: só considerar alunos cujas habilidades são subconjuntos do especial
        valid_students = []
        for i, student_mask in enumerate(students):
            # Se o aluno tem habilidades que não estão no especial, pular
            if (student_mask & special_mask) == student_mask:
                valid_students.append(i)
        
        # Iterar sobre combinações dos alunos válidos
        for i in range(len(valid_students)):
            for j in range(i + 1, len(valid_students)):
                for k in range(j + 1, len(valid_students)):
                    student_i = valid_students[i]
                    student_j = valid_students[j]
                    student_k = valid_students[k]
                    
                    # União das habilidades dos 3 alunos
                    team_skills = students[student_i] | students[student_j] | students[student_k]
                    
                    # Verificar se é exatamente igual ao subconjunto especial
                    if team_skills == special_mask:
                        count += 1
        
        results.append(count)
    
    # Imprimir todos os resultados no final
    for result in results:
        print(result)

if __name__ == "__main__":
    solve()
