from abc import ABC, abstractmethod


class PlayerRepository(ABC):
    @abstractmethod
    def createPlayer(self, nickname):
        pass

    @abstractmethod
    def findPlayerIdByPlayerNickname(self, nickname):
        pass
