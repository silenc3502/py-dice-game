from player.entity.Player import Player
from player.repository.PlayerRepository import PlayerRepository


class PlayerRepositoryImpl(PlayerRepository):
    __instance = None

    def __new__(cls):
        if cls.__instance is None:
            cls.__instance = super().__new__(cls)
            cls.__instance.__playerList = []

        return cls.__instance

    @classmethod
    def getInstance(cls):
        if cls.__instance is None:
            cls.__instance = cls()
        return cls.__instance

    def createPlayer(self, nickname):
        player = Player(nickname)
        self.__playerList.append(player)

    def getPlayerList(self):
        return self.__playerList

    def findPlayerIdByPlayerNickname(self, nickname):
        for player in self.__playerList:
            if player.getPlayerNickname() == nickname:
                return player.getPlayerId()
        return None



