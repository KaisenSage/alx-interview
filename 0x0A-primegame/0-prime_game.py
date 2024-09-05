def isWinner(x, nums):
    # Step 1: Precompute primes up to the maximum n in nums
    max_n = max(nums)
    is_prime = [True for _ in range(max_n + 1)]
    is_prime[0] = is_prime[1] = False
    for i in range(2, int(max_n ** 0.5) + 1):
        if is_prime[i]:
            for multiple in range(i*i, max_n + 1, i):
                is_prime[multiple] = False
                
    # Step 2: Compute cumulative prime counts
    prime_count = [0] * (max_n + 1)
    count = 0
    for i in range(len(is_prime)):
        if is_prime[i]:
            count += 1
        prime_count[i] = count

    # Step 3: Determine the winner for each round
    maria_wins = 0
    for n in nums:
        if prime_count[n] % 2 == 1:
            maria_wins += 1  # Maria wins this round
        else:
            maria_wins -= 1  # Ben wins this round

    # Step 4: Determine the overall winner
    if maria_wins > 0:
        return "Maria"
    elif maria_wins < 0:
        return "Ben"
    else:
        return None

