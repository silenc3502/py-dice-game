class Dice:
    def __init__(self):
        self.__diceNumber = 0
        self.__rollingPlayerId = None

    def setDiceNumber(self, number):
        self.__diceNumber = number

    def getDiceNumber(self):
        return self.__diceNumber

    def setRollingPlayerId(self, playerId):
        self.__rollingPlayerId = playerId

    def getRollingPlayerId(self):
        return self.__rollingPlayerId
