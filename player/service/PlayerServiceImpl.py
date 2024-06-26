from player.repository.PlayerRepositoryImpl import PlayerRepositoryImpl
from player.service.PlayerService import PlayerService


class PlayerServiceImpl(PlayerService):
    __instance = None

    def __new__(cls):
        if cls.__instance is None:
            cls.__instance = super().__new__(cls)
            cls.__instance.__playerRepository = PlayerRepositoryImpl.getInstance()

        return cls.__instance

    @classmethod
    def getInstance(cls):
        if cls.__instance is None:
            cls.__instance = cls()
        return cls.__instance

    def createPlayer(self, nickname):
        self.__playerRepository.createPlayer(nickname)

    def findPlayerIdByPlayerNickname(self, nickname):
        return self.__playerRepository.findPlayerIdByPlayerNickname(nickname)
