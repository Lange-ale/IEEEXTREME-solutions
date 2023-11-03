MOD = 998244353

def compute_binomial_coefficients(n, mod):
    c = [0] * (n + 1)
    c[0] = 1
    for i in range(1, n + 1):
        c[i] = (c[i - 1] * (n - i + 1) * pow(i, mod - 2, mod)) % mod
    return c

def calculate_sequence_values(k, n, mod):
    due_alla_k = 2 ** k
    combs = compute_binomial_coefficients(n, mod)
    to_print = [0] * due_alla_k
    for i in range(n + 1):
        to_print[i % due_alla_k] = (to_print[i % due_alla_k] + combs[i]) % mod
    return to_print

def main():
    k, n = map(int, input().split())
    to_print = calculate_sequence_values(k, n, MOD)
    print(' '.join(map(str, to_print)))

if __name__ == "__main__":
    main()
