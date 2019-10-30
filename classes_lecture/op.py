"""
Classes to represent games
"""

from random import random

# class Game:

#     """
#     representation of game
#     """

#     fun_level = 10

#     def __init__(self, player_1='Owen', player_2='Brandon'):
#         self.rounds = 2
#         self.steps = 5
#         self.player_1 = player_1
#         self.player_2 = player_2

#     def print_players(self):
#         print('{} is playing {}'.format(self.player_1, self.player_2))

#     def add_rounds(self):
#         self.rounds += 1

#     def winner(self):
#         """ 
#         Randomly select and return winner
#         """
#         return self.player_1 if random() > 0.5 else self.player_2

# class Tic(Game):
    
#     def __init__(self, rounds=10, steps=100, player_1='Diego', player_2='Robert'):
#         super().__init__(rounds, player_1, player_2)

#     def print_players(self):
#         print('{} is playing TicTacToe with {}'.format(self.player_1, self.player_2))



class Game:
    """
    General representation of an abstract game
    """
    fun_level = 5
    
    def __init__(self, rounds, steps, player1, player2):
        self.rounds = rounds
        self.steps = steps
        self.player1 = player1
        self.player2 = player2
        
    def print_players(self):
        """
        Print players
        """
        print('{} is playing {}'.format(self.player1,self.player2))
        
    def add_round(self):
        """
        increment number of rounds
        """
        self.rounds += 1
        
    def winner(self):
        """randomly pick and return winner"""
        return self.player1 if random() > 0.5 else self.player2


class Tic(Game):
    """Subclass of Game called Tictactoe"""
    
    def __init__(self, rounds, player1 = 'Riley', player2 = 'Amer'):
        super().__init__(player1, player2)
        
    def print_players(self):
        print('{} is playing TicTacToe with {}'.format(self.player1,self.player2))



