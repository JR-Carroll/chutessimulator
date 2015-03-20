#!/usr/bin python
#-*- coding: utf-8 -*-

import random


class Dice(object):
    def __init__(self, sides=6):
        self._min = 1
        self._max = sides
        self.allRoles = {}
        self._currentGameRoles = []
        self.startGameNum = 1

    def rollN(self, N=1):
        _currentRolls = []
        for roll in xrange(0, N, 1):
            _currentRoll = round(random.uniform(self._min, self._max))
            _currentRolls.append(_currentRoll)
        self._currentGameRoles.append(_currentRoll)
        return _currentRoll

    def gameOver(self):
        self.allRoles["Game_{0}".format(self.startGameNum)] = self._currentGameRoles
        self.startGameNum += 1
        self._reset()

    def _reset(self):
        self._currentGameRoles = []


class ChutesAndLaddersBoard(object):
    def __init__(self, players, gamesN, dice):
        self.maxGames = gamesN
        self.timesPlayed = 1
        # Number of players at least 1, max 4.
        self.numOfPlayers = players
        self.numOfDice = dice
        self.currentOrderOfWinners = {"first" : None,
                                      "second": None,
                                      "third" : None,
                                      "fourth": None}
        self.players = []
        self.dice = Dice()

        # Create the players!
        for player in xrange(0, self.numOfPlayers, 1):
            self.players.append(Player("Player{}".format(player)))

        self._availableWinnerSpots = ["first", "second", "third", "fourth"]

        self.grandOrderOfWinners = {}

        self._board = {0:{'space': 0, 'move': 0},
                       1:{'space': 1, 'move': 38},
                       2:{'space': 2, 'move': 0},
                       3:{'space': 3, 'move': 0},
                       4:{'space': 4, 'move': 14},
                       5:{'space': 5, 'move': 0},
                       6:{'space': 6, 'move': 0},
                       7:{'space': 7, 'move': 0},
                       8:{'space': 8, 'move': 0},
                       9:{'space': 9, 'move': 31},
                       10:{'space': 10, 'move': 0},
                       11:{'space': 11, 'move': 0},
                       12:{'space': 12, 'move': 0},
                       13:{'space': 13, 'move': 0},
                       14:{'space': 14, 'move': 0},
                       15:{'space': 15, 'move': 0},
                       16:{'space': 16, 'move': 6},
                       17:{'space': 17, 'move': 0},
                       18:{'space': 18, 'move': 0},
                       19:{'space': 19, 'move': 0},
                       20:{'space': 20, 'move': 0},
                       21:{'space': 21, 'move': 42},
                       22:{'space': 22, 'move': 0},
                       23:{'space': 23, 'move': 0},
                       24:{'space': 24, 'move': 0},
                       25:{'space': 25, 'move': 0},
                       26:{'space': 26, 'move': 0},
                       27:{'space': 27, 'move': 0},
                       28:{'space': 28, 'move': 84},
                       29:{'space': 29, 'move': 0},
                       30:{'space': 30, 'move': 0},
                       31:{'space': 31, 'move': 0},
                       32:{'space': 32, 'move': 0},
                       33:{'space': 33, 'move': 0},
                       34:{'space': 34, 'move': 0},
                       35:{'space': 35, 'move': 0},
                       36:{'space': 36, 'move': 44},
                       37:{'space': 37, 'move': 0},
                       38:{'space': 38, 'move': 0},
                       39:{'space': 39, 'move': 0},
                       40:{'space': 40, 'move': 0},
                       41:{'space': 41, 'move': 0},
                       42:{'space': 42, 'move': 0},
                       43:{'space': 43, 'move': 0},
                       44:{'space': 44, 'move': 0},
                       45:{'space': 45, 'move': 0},
                       46:{'space': 46, 'move': 0},
                       47:{'space': 47, 'move': 26},
                       48:{'space': 48, 'move': 0},
                       49:{'space': 49, 'move': 11},
                       50:{'space': 50, 'move': 0},
                       51:{'space': 51, 'move': 67},
                       52:{'space': 52, 'move': 0},
                       53:{'space': 53, 'move': 0},
                       54:{'space': 54, 'move': 0},
                       55:{'space': 55, 'move': 0},
                       56:{'space': 56, 'move': 53},
                       57:{'space': 57, 'move': 0},
                       58:{'space': 58, 'move': 0},
                       59:{'space': 59, 'move': 0},
                       60:{'space': 60, 'move': 0},
                       61:{'space': 61, 'move': 0},
                       62:{'space': 62, 'move': 19},
                       63:{'space': 63, 'move': 0},
                       64:{'space': 64, 'move': 60},
                       65:{'space': 65, 'move': 0},
                       66:{'space': 66, 'move': 0},
                       67:{'space': 67, 'move': 0},
                       68:{'space': 68, 'move': 0},
                       69:{'space': 69, 'move': 0},
                       70:{'space': 70, 'move': 0},
                       71:{'space': 71, 'move': 91},
                       72:{'space': 72, 'move': 0},
                       73:{'space': 73, 'move': 0},
                       74:{'space': 74, 'move': 0},
                       75:{'space': 75, 'move': 0},
                       76:{'space': 76, 'move': 0},
                       77:{'space': 77, 'move': 0},
                       78:{'space': 78, 'move': 0},
                       79:{'space': 79, 'move': 0},
                       80:{'space': 80, 'move': 100},
                       81:{'space': 81, 'move': 0},
                       82:{'space': 82, 'move': 0},
                       83:{'space': 83, 'move': 0},
                       84:{'space': 84, 'move': 0},
                       85:{'space': 85, 'move': 0},
                       86:{'space': 86, 'move': 0},
                       87:{'space': 87, 'move': 24},
                       88:{'space': 88, 'move': 0},
                       89:{'space': 89, 'move': 0},
                       90:{'space': 90, 'move': 0},
                       91:{'space': 91, 'move': 0},
                       92:{'space': 91, 'move': 0},
                       93:{'space': 91, 'move': 73},
                       94:{'space': 91, 'move': 0},
                       95:{'space': 91, 'move': 75},
                       96:{'space': 91, 'move': 0},
                       97:{'space': 91, 'move': 0},
                       98:{'space': 91, 'move': 78},
                       99:{'space': 91, 'move': 0},
                       100:{'space': 91, 'move': 0}}

    def played(self):
        self.timesPlayed += 1
        return True

    def playerWon(self, position, player):
        self.currentOrderOfWinners[position] = player

    def gameOver(self):
        self.grandOrderOfWinners[self.timesPlayed] = self.currentOrderOfWinners
        self.played()
        self._reset()
        return True

    def _reset(self):
        self.currentOrderOfWinners = {"first" : None,
                                      "second": None,
                                      "third" : None,
                                      "fourth": None}

        self._availableWinnerSpots = ["first", "second", "third", "fourth"]
        return True

    def playGames(self):
        while self.maxGames:
            players = list(self.players)
            # extra guard
            if gamesToPlay <= 0:
                break

            # initialize game variables
            gameOver = False

            while not gameOver:
                # start player roles!
                for player in players:
                    roll = self.dice.rollN(dice)
                    if self.numOfDice > 1:
                        rollTot = sum(roll)
                    else:
                        rollTot = roll
                    endOrElse = player.moveByDice(roll)
                    if endOrElse:
                        position = self._availableWinnerSpots.pop(0)
                        player.victory(position, self.numOfPlayers, self.timesPlayed, True)
                        self.currentOrderOfWinners[position] = player.name
                        players.remove(player)
                    if player.currentPosition > 100:
                        playerPosition = 100
                    else:
                        playerPosition = player.currentPosition
                    boardSays = self._board.get(playerPosition)
                    if boardSays.get("move") != 0:
                        player.moveByDamnORYay(boardSays.get("move"))

                    # check to see if it is end of game after each player turn.
                    _playerCnt = 0
                    for player in players:
                        if player.ready:
                            _playerCnt += 1
                    if _playerCnt <= 1:
                        position = self._availableWinnerSpots.pop(0)
                        player.victory(position, self.numOfPlayers, self.timesPlayed, False)
                        self.currentOrderOfWinners[position] = player.name
                        players.remove(player)
                        gameOver = True

            for player in self.players:
                player._reset()
            #print "Game Completed"
            #print "Winners : {}".format(self.currentOrderOfWinners)
            self.gameOver()
            # subtract one from available games to play
            # will break loop once it hits 0.
            self.maxGames -= 1

class Player(object):
    def __init__(self, name, *args, **kwargs):
        self.name = name
        self._dataStr = "{0:<10}{1:^6}{2:^6}{3:^6}{4:^6}{5:^6}{6:^6}{7:^6}{8:^6}{9:^7}"
        # resetable variables on each game
        self.startPosition = 0
        self.currentPosition = 0
        self.turn = 0
        self.ready = True
        self.finish = False

        # running stats
        self.gamesPlaceFirst = 0
        self.gamesPlaceLast = 0
        self.gamesPlayed = 0
        self.totalGamesComp = 0
        self.minimum = None
        self.maximum = None
        self.gamesAllData = []

    def moveByDice(self, rollTotal):
        self.turn += 1
        self.currentPosition += rollTotal
        _winning = self.checkWin()
        return _winning

    def moveByDamnORYay(self, position):
        self.currentPosition = position

    def checkWin(self):
        if self.currentPosition >= 100:
            _won = True
        else:
            _won = False
        return _won

    def victory(self, pos, totPlayers, gameNum, finish):
        self._recordData(pos, totPlayers, gameNum)
        self.ready = False
        if not self.maximum or self.turn > self.maximum:
            self.maximum = self.turn
        if not self.minimum or self.turn < self.minimum:
            self.minimum = self.turn
        if finish:
            self.totalGamesComp += 1
            self.finish = finish
        self.gamesPlayed += 1

    def _recordData(self, pos, totPlayers, gameNum):
        _posMap = {"first" : 1,
                   "second" : 2,
                   "third" : 3,
                   "fourth" : 4}

        if _posMap.get(pos) == 1:
            self.gamesPlaceFirst += 1
        elif _posMap.get(pos) == totPlayers:
            self.gamesPlaceLast += 1
        self.gamesAllData.append({"Game{}".format(gameNum): "{0}/{1}".format(pos, totPlayers)})
        self.gamesAllData[gameNum-1]["finished?"] = self.finish
        self.gamesAllData[gameNum-1]["turnsTook"] = self.turn

    def _reset(self):
        self.turn = 0
        self.startPosition = 0
        self.currentPosition = 0
        self.ready = True
        self.finish = False

    def _printHeader(self):
        print self._dataStr.format("Name",
                                   "X-Bar",
                                   "Min",
                                   "Max",
                                   "Std",
                                   "N-1st",
                                   "N-Last",
                                   "Tot",
                                   "Comp",
                                   "Finish%")
    def summarizeData(self):
        totalTurns = 0
        _std = 0
        _allTurns = []
        for turns in self.gamesAllData:
            _turn = turns.get("turnsTook")
            totalTurns += _turn
            _allTurns.append(_turn)

        _averageTurns = round(float(totalTurns)/float(self.gamesPlayed), 3)

        # calculate std
        _deviationSqrd = []

        for dev in _allTurns:
            _deviationSqrd.append((float(dev) - float(_averageTurns))**2)

        if self.gamesPlayed == 1:
            _std = "NA"
        else:
            _std = round(sum(_deviationSqrd)/(len(_deviationSqrd)-1), 2)

        _gamesCompPerc = round(float(self.totalGamesComp)/float(self.gamesPlayed), 4)

        print self._dataStr.format(self.name,
                                   _averageTurns,
                                   self.minimum,
                                   self.maximum,
                                   _std,
                                   self.gamesPlaceFirst,
                                   self.gamesPlaceLast,
                                   self.gamesPlayed,
                                   self.totalGamesComp,
                                   _gamesCompPerc)

if __name__ == '__main__':
    # SETUP SIMULATOR VARIABLES
    #
    # Number of times to play a game
    gamesToPlay = 1000
    #
    # Number of players (max 4)
    players = 3
    #
    # Number of dice roles (default is 2)
    dice = 1

    # Placeholders for game components
    board = ChutesAndLaddersBoard(gamesN=gamesToPlay, players=players, dice=dice)
    board.playGames()

    board.players[0]._printHeader()

    for player in board.players:
        player.summarizeData()


