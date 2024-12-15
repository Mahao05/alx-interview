#!/usr/bin/python38
def is_winner(x, nums):
    """Determines the winner of a game of prime number elimination.

    Args:
        x (int): The number of rounds.
        nums (list): A list of integers representing the `n` value for each round.

    Returns:
        str: The name of the winner ("Maria" or "Ben"), or "None" if there's no clear winner.
    """

    maria_wins = 0
    ben_wins = 0

    for n in nums:
        if n >= 2:
            maria_wins += 1 
        else:
            ben_wins += 1  

    if maria_wins > ben_wins:
        return "Maria"
    elif ben_wins > maria_wins:
        return "Ben"
    else:
        return None
