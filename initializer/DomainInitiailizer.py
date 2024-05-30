from dice.service.DiceServiceImpl import DiceServiceImpl


class DomainInitializer:
    @staticmethod
    def initDiceDomain():
        DiceServiceImpl.getInstance()

    @staticmethod
    def initEachDomain():
        # Dice Domain
        DomainInitializer.initDiceDomain()
