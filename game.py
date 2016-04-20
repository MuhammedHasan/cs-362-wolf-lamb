import itertools
import copy


class GameState():

    def __init__(self, previous_move=None, number_of_animal=3):
        self.number_of_animal = number_of_animal
        self.sheepDown = self.number_of_animal
        self.wolfDown = self.number_of_animal
        self.sheepUp = 0
        self.wolfUp = 0
        self.previous_move = previous_move

    def cross(self, animal):
        if animal == 'w':
            self.wolfDown -= 1
            self.wolfUp += 1
        elif animal == 's':
            self.sheepDown -= 1
            self.sheepUp += 1
        else:
            raise ValueError('animal must be w or s')

    def bring_back(self, animal):
        if animal == 'w':
            self.wolfDown += 1
            self.wolfUp -= 1
        elif animal == 's':
            self.sheepDown += 1
            self.sheepUp -= 1
        else:
            raise ValueError('animal must be w or s')

    def game_over(self):
        sides = [False, False]
        if(self.wolfDown > self.sheepDown) and self.sheepDown != 0:
            sides[0] = True
        elif(self.wolfUp > self.sheepUp) and self.sheepUp != 0:
            sides[1] = True
        return sides

    def ship(self, animals):
        self.previous_move = animals
        if len(animals) == 1:
            self.cross(animals[0])
            return False
        self.cross(animals[0])
        self.cross(animals[1])
        if self.game_over()[0]:
            return True
        self.bring_back(animals[1])
        return self.game_over()[1]

    def succeser(self):
        if self.wolfUp == self.number_of_animal:
            if self.sheepUp == self.number_of_animal:
                return True
        return False

    def possible_actions(self):
        animals_down = ['w' for i in range(self.wolfDown)]
        animals_down.extend(['s' for i in range(self.sheepDown)])
        if len(animals_down) == 1:
            return [animals_down]
        return set(itertools.permutations(animals_down, 2))

    def next_states(self):
        next_sts = list()
        for i in self.possible_actions():
            ns = copy.deepcopy(self)
            if not ns.ship(i):
                next_sts.append(ns)
        return next_sts

    def __str__(self):
        game_str = list()
        if self.previous_move:
            game_str.append('Cross with ')
            if self.previous_move[0] == 'w':
                game_str.append('wolf ')
            else:
                game_str.append('lamb ')
            if len(self.previous_move) == 2:
                game_str.append('and ')
                if self.previous_move[1] == 'w':
                    game_str.append('wolf\n')
                else:
                    game_str.append('lamb\n')
                game_str.append('come back with %s' % game_str[-1])
            else:
                game_str.append('\n')
        return ''.join(game_str)
