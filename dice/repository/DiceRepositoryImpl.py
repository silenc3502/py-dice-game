from random import randint

from dice.entity.Dice import Dice
from dice.entity.DiceNumber import DiceNumber
from dice.repository.DiceRepository import DiceRepository


class DiceRepositoryImpl(DiceRepository):
    __instance = None

    def __new__(cls):
        if cls.__instance is None:
            cls.__instance = super().__new__(cls)
            cls.__instance.__diceList = []

        return cls.__instance

    @classmethod
    def getInstance(cls):
        if cls.__instance is None:
            cls.__instance = cls()
        return cls.__instance

    def rollDice(self, playerId):
        diceNumber = randint(DiceNumber.ONE.value, DiceNumber.SIX.value)
        dice = Dice()
        dice.setDiceNumber(diceNumber)
        dice.setRollingPlayerId(playerId)
        self.__diceList.append(dice)

    def getDiceNumber(self, playerId):
        return [dice.getDiceNumber() for dice in self.__diceList if dice.getRollingPlayerId() == playerId]
