import unittest
from dice.entity.DiceNumber import DiceNumber
from dice.service.DiceServiceImpl import DiceServiceImpl
from initializer.DomainInitiailizer import DomainInitializer

DomainInitializer.initEachDomain()


class TestDice(unittest.TestCase):
    def setUp(self):
        self.diceService = DiceServiceImpl.getInstance()

    def test_singleton_instance(self):
        diceService = DiceServiceImpl()
        self.assertIs(self.diceService, diceService, "DiceServiceImpl should be a singleton")

    def test_roll_dice(self):
        self.diceService.rollDice()
        rolled_number = self.diceService.getDiceNumber()
        self.assertGreaterEqual(rolled_number, DiceNumber.ONE.value, "Rolled number should be >= 1")
        self.assertLessEqual(rolled_number, DiceNumber.SIX.value, "Rolled number should be <= 6")

    def test_dice_number_range(self):
        for _ in range(100):
            self.diceService.rollDice()
            rolled_number = self.diceService.getDiceNumber()
            self.assertGreaterEqual(rolled_number, DiceNumber.ONE.value, "Rolled number should be >= 1")
            self.assertLessEqual(rolled_number, DiceNumber.SIX.value, "Rolled number should be <= 6")


if __name__ == "__main__":
    unittest.main()
