# takes 0/100 points

MOD = 998244353

def calculate_probability(n, k):
    dp = [[0] * (n + 1) for _ in range(k + 1)]
    dp[0][0] = 1
    for i in range(1, k + 1):
        for j in range(1, n + 1):
            for x in range(1, 7):
                if j - x >= 0:
                    dp[i][j] += dp[i - 1][j - x]
                    dp[i][j] %= MOD
    ways = dp[k][n]
    total_outcomes = 6**k
    probability = (ways * pow(total_outcomes, -1, MOD)) % MOD
    return probability

n, k = map(int, input().split())
result = calculate_probability(n, k)
print(result)




# from math import gcd

# def sommatoria(k):
#     a = 6
#     r = 6
#     n = k
#     somma = a * (1 - r**n) / (1 - r)
#     return somma

# print(sommatoria(3**6))

# MOD = 998244353

# common_divisor = gcd(7, 108)
# result = (7 // common_divisor, 108 // common_divisor)

# # Calculate the modular inverse of the denominator
# def mod_inverse(x, m):
#     return pow(x, -1, m)

# # Calculate P * Q^-1 mod 998244353
# result = (result[0] * mod_inverse(result[1], MOD)) % MOD

# print(result)