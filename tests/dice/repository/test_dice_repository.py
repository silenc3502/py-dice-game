import unittest
from dice.entity.DiceNumber import DiceNumber
from dice.repository.DiceRepositoryImpl import DiceRepositoryImpl
from initializer.DomainInitiailizer import DomainInitializer

DomainInitializer.initEachDomain()


class TestDice(unittest.TestCase):
    def setUp(self):
        self.diceRepository = DiceRepositoryImpl.getInstance()

    def test_singleton_instance(self):
        dice_repo_2 = DiceRepositoryImpl()
        self.assertIs(self.diceRepository, dice_repo_2, "DiceRepositoryImpl should be a singleton")

    def test_roll_dice(self):
        self.diceRepository.rollDice()
        rolled_number = self.diceRepository.getDiceNumber()
        self.assertGreaterEqual(rolled_number, DiceNumber.ONE.value, "Rolled number should be >= 1")
        self.assertLessEqual(rolled_number, DiceNumber.SIX.value, "Rolled number should be <= 6")

    def test_dice_number_range(self):
        for _ in range(100):
            self.diceRepository.rollDice()
            rolled_number = self.diceRepository.getDiceNumber()
            self.assertGreaterEqual(rolled_number, DiceNumber.ONE.value, "Rolled number should be >= 1")
            self.assertLessEqual(rolled_number, DiceNumber.SIX.value, "Rolled number should be <= 6")


if __name__ == "__main__":
    unittest.main()
