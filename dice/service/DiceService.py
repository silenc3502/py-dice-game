from abc import ABC, abstractmethod


class DiceService(ABC):
    @abstractmethod
    def rollDice(self):
        pass

    @abstractmethod
    def getDiceNumber(self):
        pass
