def solve():
    n = int(input())
    c = input().strip()
    
    target = []
    for bit in c:
        if bit in '01':
            target.append(int(bit))
        else:
            continue
    
    if len(target) != n:
        n = len(target)
    
    def solve_with_pattern(base_pattern):
        current = [0] * n
        operations = 0
        max_operations = n * 2
        
        while current != target and operations < max_operations:
            best_pos = None
            best_improvement = -1
            
            for pos in range(-7, n):
                improvement = 0
                
                for j in range(8):
                    bit_pos = pos + j
                    if 0 <= bit_pos < n:
                        current_bit = current[bit_pos]
                        target_bit = target[bit_pos]
                        new_bit = current_bit ^ base_pattern[j]
                        
                        if current_bit != target_bit and new_bit == target_bit:
                            improvement += 1
                        elif current_bit == target_bit and new_bit != target_bit:
                            improvement -= 1
                
                if improvement > best_improvement:
                    best_improvement = improvement
                    best_pos = pos
            
            if best_improvement <= 0:
                return float('inf')
            
            for j in range(8):
                bit_pos = best_pos + j
                if 0 <= bit_pos < n:
                    current[bit_pos] ^= base_pattern[j]
            
            operations += 1
        
        if current == target:
            return operations
        else:
            return float('inf')
    
    best_pattern = None
    min_operations = float('inf')
    
    for pattern_int in range(256):
        pattern = []
        for i in range(8):
            pattern.append((pattern_int >> (7 - i)) & 1)
        
        ops = solve_with_pattern(pattern)
        
        if ops < min_operations:
            min_operations = ops
            best_pattern = pattern
        elif ops == min_operations and best_pattern is not None:
            if pattern_int < int(''.join(map(str, best_pattern)), 2):
                best_pattern = pattern
    
    print(''.join(map(str, best_pattern)), min_operations)

if __name__ == "__main__":
    solve()
