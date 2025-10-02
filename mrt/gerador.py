def solve():
    n = int(input())
    c = input().strip()
    
    # Converter string para lista de inteiros, validando os caracteres
    target = []
    for bit in c:
        if bit in '01':
            target.append(int(bit))
        else:
            # Ignorar caracteres inválidos ou considerar como erro
            continue
    
    # Ajustar n se necessário
    if len(target) != n:
        n = len(target)
    
    def solve_with_pattern(base_pattern):
        # Simular o processo de aplicação do padrão usando algoritmo guloso
        current = [0] * n
        operations = 0
        max_operations = n * 2  # limite de segurança
        
        while current != target and operations < max_operations:
            best_pos = None
            best_improvement = -1
            
            # Testar todas as posições possíveis (-7 a n-1)
            for pos in range(-7, n):
                improvement = 0
                
                # Calcular melhoria se aplicarmos o padrão nesta posição
                for j in range(8):
                    bit_pos = pos + j
                    if 0 <= bit_pos < n:
                        # Estado atual vs estado desejado
                        current_bit = current[bit_pos]
                        target_bit = target[bit_pos]
                        new_bit = current_bit ^ base_pattern[j]
                        
                        # Se ficará mais próximo do target
                        if current_bit != target_bit and new_bit == target_bit:
                            improvement += 1
                        # Se ficará mais longe do target  
                        elif current_bit == target_bit and new_bit != target_bit:
                            improvement -= 1
                
                if improvement > best_improvement:
                    best_improvement = improvement
                    best_pos = pos
            
            # Se não há melhoria possível, não é possível gerar o target
            if best_improvement <= 0:
                return float('inf')
            
            # Aplicar a operação na melhor posição
            for j in range(8):
                bit_pos = best_pos + j
                if 0 <= bit_pos < n:
                    current[bit_pos] ^= base_pattern[j]
            
            operations += 1
        
        # Verificar se conseguiu gerar o target
        if current == target:
            return operations
        else:
            return float('inf')
    
    # Testar todos os padrões possíveis
    best_pattern = None
    min_operations = float('inf')
    
    for pattern_int in range(256):
        # Converter inteiro para padrão de 8 bits
        pattern = []
        for i in range(8):
            pattern.append((pattern_int >> (7 - i)) & 1)
        
        ops = solve_with_pattern(pattern)
        
        # Atualizar melhor padrão
        if ops < min_operations:
            min_operations = ops
            best_pattern = pattern
        elif ops == min_operations and best_pattern is not None:
            if pattern_int < int(''.join(map(str, best_pattern)), 2):
                best_pattern = pattern
    
    # Imprimir resultado
    print(''.join(map(str, best_pattern)), min_operations)

if __name__ == "__main__":
    solve()
