def solve():
    MOD = 10**9 + 7
    

    def mod_inverse(a, mod):
        return pow(a, mod - 2, mod)
    

    n, q = map(int, input().split())
    commands = list(map(int, input().split()))

    prob = [(0, 1) for _ in range(n + 1)]
    prob[1] = (1, 1)  
    

    expected = [(0, 1) for _ in range(n + 1)]
    

    def add_fractions(f1, f2):
        num1, den1 = f1
        num2, den2 = f2

        new_num = (num1 * den2 + num2 * den1) % MOD
        new_den = (den1 * den2) % MOD
        return (new_num, new_den)
    

    def mult_fractions(f1, f2):
        num1, den1 = f1
        num2, den2 = f2

        new_num = (num1 * num2) % MOD
        new_den = (den1 * den2) % MOD
        return (new_num, new_den)
    

    for x in commands:
        new_prob = [(0, 1) for _ in range(n + 1)]
        

        for mesa in range(1, n + 1):
            if prob[mesa][0] == 0:  
                continue
                
            current_prob = prob[mesa]

            prob_move = mult_fractions(current_prob, (1, 2))
            new_prob[x] = add_fractions(new_prob[x], prob_move)
            

            prob_order = mult_fractions(current_prob, (1, 2))
            new_prob[mesa] = add_fractions(new_prob[mesa], prob_order)
            
            # Adiciona x frangos esperados na mesa atual
            expected_addition = mult_fractions(prob_order, (x, 1))
            expected[mesa] = add_fractions(expected[mesa], expected_addition)
        
        prob = new_prob
    

    for i in range(1, n + 1):
        num, den = expected[i]
        if num == 0:
            print(0)
        else:

            inv_den = mod_inverse(den, MOD)
            result = (num * inv_den) % MOD
            print(result)

if __name__ == "__main__":
    solve()
