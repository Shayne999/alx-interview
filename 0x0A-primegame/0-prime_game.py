#!/usr/bin/python3
"""Prime Game"""


def isWinner(x, nums):
    max_n = max(nums)

    # Generates all prime numbers up to max_n using Sieve of Eratosthenes
    is_prime = [True] * (max_n + 1)
    is_prime[0] = is_prime[1] = False

    p = 2
    while (p * p <= max_n):
        if is_prime[p]:
            for i in range(p * p, max_n + 1, p):
                is_prime[i] = False
        p += 1

    primes = [p for p in range(max_n + 1) if is_prime[p]]

    # Determines the game results for each n in nums
    results = []

    for n in nums:
        if n == 1:
            results.append('Ben')
            continue

        """can_win[i] will be True if the starting
        player can force a win starting with number i
        """
        can_win = [False] * (n + 1)

        for i in range(2, n + 1):
            for p in primes:
                if p > i:
                    break
                if not can_win[i - p]:
                    can_win[i] = True
                    break

        if can_win[n]:
            results.append('Maria')
        else:
            results.append('Ben')

    # Counts Maria and Ben's wins
    maria_wins = results.count('Maria')
    ben_wins = results.count('Ben')

    # Determines who won the most rounds
    if maria_wins > ben_wins:
        return 'Maria'
    elif ben_wins > maria_wins:
        return 'Ben'
    else:
        return None
