from dice.service.DiceServiceImpl import DiceServiceImpl
from player.repository.PlayerRepositoryImpl import PlayerRepositoryImpl


class DomainInitializer:
    @staticmethod
    def initDiceDomain():
        DiceServiceImpl.getInstance()

    @staticmethod
    def initPlayerDomain():
        PlayerRepositoryImpl.getInstance()

    @staticmethod
    def initEachDomain():
        # Dice Domain
        DomainInitializer.initDiceDomain()
        DomainInitializer.initPlayerDomain()
