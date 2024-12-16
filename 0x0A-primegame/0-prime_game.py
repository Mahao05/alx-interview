#!/usr/bin/python38
def isWinner(x, nums):
    """
    Determine the winner of the prime number game.
    
    Args:
        x (int): Number of rounds.
        nums (list of int): Array where each element is n for a given round.
    
    Returns:
        str: Name of the player that won the most rounds ("Maria" or "Ben").
             If the winner cannot be determined, return None.
    """

    def sieve_of_eratosthenes(max_n):
        """Generate a list of primes up to max_n using the Sieve of Eratosthenes."""
        is_prime = [True] * (max_n + 1)
        is_prime[0] = is_prime[1] = False
        for i in range(2, int(max_n**0.5) + 1):
            if is_prime[i]:
                for multiple in range(i * i, max_n + 1, i):
                    is_prime[multiple] = False
        return is_prime

    def count_moves(n, primes):
        """Count the number of valid prime moves for a given n."""
        used = [False] * (n + 1)
        moves = 0
        for i in range(2, n + 1):
            if primes[i] and not used[i]:
                moves += 1
                for multiple in range(i, n + 1, i):
                    used[multiple] = True
        return moves

    if x < 1 or not nums:
        return None

    max_n = max(nums)
    primes = sieve_of_eratosthenes(max_n)

    maria_wins = 0
    ben_wins = 0

    for n in nums:
        if n == 1:
            ben_wins += 1
        else:
            moves = count_moves(n, primes)
            if moves % 2 == 0:
                ben_wins += 1
            else:
                maria_wins += 1

    if maria_wins > ben_wins:
        return "Maria"
    elif ben_wins > maria_wins:
        return "Ben"
    return None
