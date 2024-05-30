import unittest
from unittest.mock import patch
from dice.entity.DiceNumber import DiceNumber
from dice.repository.DiceRepositoryImpl import DiceRepositoryImpl
from initializer.DomainInitiailizer import DomainInitializer

DomainInitializer.initEachDomain()

class TestDice(unittest.TestCase):
    def setUp(self):
        self.diceRepository = DiceRepositoryImpl.getInstance()
        self.diceRepository._DiceRepositoryImpl__diceList.clear()

    @patch('dice.repository.DiceRepositoryImpl.randint')
    def test_rollDice(self, mock_randint):
        mock_randint.return_value = DiceNumber.THREE.value
        self.diceRepository.rollDice(playerId=1)  # playerId 추가

        dice_numbers = self.diceRepository.getDiceNumber(playerId=1)  # playerId 추가

        self.assertEqual(len(dice_numbers), 1)
        self.assertEqual(dice_numbers[0], DiceNumber.THREE.value)

    def test_getDiceNumber_empty(self):
        dice_numbers = self.diceRepository.getDiceNumber(playerId=1)  # playerId 추가

        self.assertEqual(len(dice_numbers), 0)

    def test_singleton_instance(self):
        dice_repo_2 = DiceRepositoryImpl()
        self.assertIs(self.diceRepository, dice_repo_2, "DiceRepositoryImpl should be a singleton")

    def test_roll_dice(self):
        self.diceRepository.rollDice(playerId=1)  # playerId 추가
        rolled_numbers = self.diceRepository.getDiceNumber(playerId=1)  # playerId 추가
        self.assertEqual(len(rolled_numbers), 1, "There should be exactly one rolled number")
        rolled_number = rolled_numbers[0]
        self.assertGreaterEqual(rolled_number, DiceNumber.ONE.value, "Rolled number should be >= 1")
        self.assertLessEqual(rolled_number, DiceNumber.SIX.value, "Rolled number should be <= 6")

    def test_dice_number_range(self):
        for _ in range(100):
            self.diceRepository.rollDice(playerId=1)  # playerId 추가
        rolled_numbers = self.diceRepository.getDiceNumber(playerId=1)  # playerId 추가
        self.assertEqual(len(rolled_numbers), 100, "There should be exactly 100 rolled numbers")
        for rolled_number in rolled_numbers:
            self.assertGreaterEqual(rolled_number, DiceNumber.ONE.value, "Rolled number should be >= 1")
            self.assertLessEqual(rolled_number, DiceNumber.SIX.value, "Rolled number should be <= 6")

if __name__ == "__main__":
    unittest.main()
