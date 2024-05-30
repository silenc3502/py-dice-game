import unittest
from unittest.mock import patch

from player.repository.PlayerRepositoryImpl import PlayerRepositoryImpl


class TestPlayerRepositoryImpl(unittest.TestCase):

    def test_realCreatePlayer(self):
        repo = PlayerRepositoryImpl.getInstance()
        repo.createPlayer('MockPlayer')

        player = repo._PlayerRepositoryImpl__player

        self.assertEqual(player.getPlayerNickname(), 'MockPlayer')

    @patch('player.repository.PlayerRepositoryImpl.Player')
    def test_mockCreatePlayer(self, MockPlayer):
        mock_player_instance = MockPlayer.return_value
        mock_player_instance.getPlayerNickname.return_value = 'MockPlayer'

        repo = PlayerRepositoryImpl.getInstance()
        repo.createPlayer('MockPlayer')

        player = repo._PlayerRepositoryImpl__player
        self.assertEqual(player.getPlayerNickname(), 'MockPlayer')


if __name__ == "__main__":
    unittest.main()
