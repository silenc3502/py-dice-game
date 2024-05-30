from dice.repository.DiceRepositoryImpl import DiceRepositoryImpl
from dice.service.DiceService import DiceService


class DiceServiceImpl(DiceService):
    __instance = None

    def __new__(cls):
        if cls.__instance is None:
            cls.__instance = super().__new__(cls)
            cls.__instance.__diceRepository = DiceRepositoryImpl.getInstance()
        return cls.__instance

    @classmethod
    def getInstance(cls):
        if cls.__instance is None:
            cls.__instance = cls()
        return cls.__instance

    def rollDice(self, playerId):
        self.__diceRepository.rollDice(playerId)

    def getDiceNumber(self, playerId):
        return self.__diceRepository.getDiceNumber(playerId)

