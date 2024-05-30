from dice.repository.DiceRepositoryImpl import DiceRepositoryImpl
from dice.service.DiceServiceImpl import DiceServiceImpl
from initializer.DomainInitiailizer import DomainInitializer
from player.service.PlayerServiceImpl import PlayerServiceImpl

DomainInitializer.initEachDomain()


def main():
    playerService = PlayerServiceImpl.getInstance()
    playerService.createPlayer("first-player")
    playerService.createPlayer("second-player")

    firstPlayerId = playerService.findPlayerIdByPlayerNickname("first-player")

    diceService = DiceServiceImpl.getInstance()
    diceService.rollDice(firstPlayerId)

    firstPlayerDice = diceService.checkDice(firstPlayerId)
    print(f"첫 번째 플레이어의 주사위 눈금: {firstPlayerDice.getDiceNumber()}")
    print(f"이 주사위를 굴린 사람은 ? {firstPlayerDice.getRollingPlayerId()}")

if __name__ == "__main__":
    main()
