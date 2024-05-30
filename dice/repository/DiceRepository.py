from abc import ABC, abstractmethod


class DiceRepository(ABC):
    @abstractmethod
    def rollDice(self, playerId):
        pass

    @abstractmethod
    def getDiceNumber(self, playerId):
        pass
