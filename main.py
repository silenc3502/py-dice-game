from dice.repository.DiceRepositoryImpl import DiceRepositoryImpl
from dice.service.DiceServiceImpl import DiceServiceImpl
from initializer.DomainInitiailizer import DomainInitializer
from player.service.PlayerServiceImpl import PlayerServiceImpl

DomainInitializer.initEachDomain()


def main():
    playerService = PlayerServiceImpl.getInstance()
    playerService.createPlayer("first-player")
    playerService.createPlayer("second-player")

    diceService = DiceServiceImpl.getInstance()
    diceService.rollDice(playerService.findPlayerByNickName("first-player"))

if __name__ == "__main__":
    main()
