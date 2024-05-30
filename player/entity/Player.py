from xml.dom.minidom import Entity


class Player:
    __id_counter = 1

    def __init__(self, nickname=None):
        self.__playerId = Player.__id_counter
        Player.__id_counter += 1
        self.__playerNickname = nickname

    def getPlayerId(self):
        return self.__playerId

    def getPlayerNickname(self):
        return self.__playerNickname

    def setPlayerNickname(self, nickname):
        self.__playerNickname = nickname
