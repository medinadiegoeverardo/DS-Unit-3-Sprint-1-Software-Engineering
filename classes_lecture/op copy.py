"""
Classes to represent games
"""

from random import random

class Game:
    # fun_level = 5
    
    def __init__(self, player1, player2, rounds=0):
        self.rounds = rounds
        self.player1 = player1
        self.player2 = player2
        
    def print_players(self):
        return ('{} is playing {}'.format(self.player1,self.player2))
        
    def add_round(self):
        pass
    
    def winner(self):
        return self.player1 if random() > 0.5 else self.player2


class Wrestling(Game):
    """Subclass of Game called Wrestling!"""

    number_of_wrestlers = 0
    
    def __init__(self, rounds, player1, player2): # replacing __init__ method of Game. As a result,
        # the child class is not called automatically. we have to call it explicitly.
        super().__init__(player1, player2, rounds) # super() gets defintion of parent class and 
        # __init__ calls the Game __init__ (what lol)

        Wrestling.number_of_wrestlers += 1
        
    def print_players(self):
        fight_between_both = '{} is fighting {}'.format(self.player1, self.player2)
        return fight_between_both

    def set_player_one_height(self, height):
        self.player1_height = height
        return height

    def set_player_two_height(self, height):
        self.player2_height = height
        return height

    def set_player_one_weight(self, weight):
        self.player1_weight = weight
        return weight

    def set_player_two_weight(self, weight):
        self.player2_weight = weight
        return weight

    def set_player_one_grade(self, grade):
        self.player1_grade = grade
        return grade

    def set_player_two_grade(self, grade):
        self.player2_grade = grade
        return grade

    def get_two_weights(self):
        weights_of_both = '{} weighs {}, and {} weighs {}'.format(self.player1, self.player1_weight, self.player2, self.player1_weight)
        return weights_of_both

# players = Tic('Brandon', 'Other')
# print(players.print_players())

match = Wrestling(3, 'Diego', 'Nick')
match.set_player_one_weight(148.4)
match.set_player_two_weight(147.4)
print(match.print_players())
print(match.get_two_weights())

#weights_of_both_players = Wrestling()
#rounds, player1, player2, grade, weight, height

