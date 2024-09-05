#!/usr/bin/python3
"""
Prime Game: Maria and Ben take turns to pick prime numbers and their multiples
"""

def isWinner(x, nums):
    """Determine who the winner of each game is"""
    if x < 1 or not nums:
        return None

    # Precompute prime numbers up to the maximum value of n in nums
    max_num = max(nums)
    sieve = [True] * (max_num + 1)
    sieve[0] = sieve[1] = False
    for i in range(2, int(max_num**0.5) + 1):
        if sieve[i]:
            for multiple in range(i * i, max_num + 1, i):
                sieve[multiple] = False

    # Precompute the number of primes up to each index n
    primes_count = [0] * (max_num + 1)
    for i in range(1, max_num + 1):
        primes_count[i] = primes_count[i - 1] + (1 if sieve[i] else 0)

    maria_wins = 0
    ben_wins = 0

    for n in nums:
        # Maria wins if the number of primes up to n is odd, otherwise Ben wins
        if primes_count[n] % 2 == 1:
            maria_wins += 1
        else:
            ben_wins += 1

    if maria_wins > ben_wins:
        return "Maria"
    elif ben_wins > maria_wins:
        return "Ben"
    return None

