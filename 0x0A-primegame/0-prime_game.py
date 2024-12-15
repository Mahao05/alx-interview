#!/usr/bin/python3
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
        """Generate prime numbers up to max_n using the Sieve of Eratosthenes."""
        is_prime = [True] * (max_n + 1)
        is_prime[0] = is_prime[1] = False  
        for i in range(2, int(max_n**0.5) + 1):
            if is_prime[i]:
                for multiple in range(i * i, max_n + 1, i):
                    is_prime[multiple] = False
        return is_prime

    def prime_moves_count(n, is_prime):
        """
        Count the number of valid prime moves for a given n.
        
        Args:
            n (int): The upper limit of the range (1 to n).
            is_prime (list of bool): List marking prime numbers up to n.
        
        Returns:
            int: Total number of moves possible.
        """
        primes = [i for i in range(2, n + 1) if is_prime[i]]
        moves = 0
        used = [False] * (n + 1)
        for prime in primes:
            if not used[prime]:
                moves += 1
                for multiple in range(prime, n + 1, prime):
                    used[multiple] = True
        return moves

    if x < 1 or not nums:
        return None

    max_n = max(nums)
    is_prime = sieve_of_eratosthenes(max_n)

    maria_wins = 0
    ben_wins = 0

    for n in nums:
        if n == 1:
            ben_wins += 1  
            continue

        moves = prime_moves_count(n, is_prime)
        if moves % 2 == 0:
            ben_wins += 1
        else:
            maria_wins += 1

    if maria_wins > ben_wins:
        return "Maria"
    elif ben_wins > maria_wins:
        return "Ben"
    else:
        return None


