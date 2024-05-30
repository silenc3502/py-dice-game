import unittest
from unittest.mock import patch, MagicMock
from player.service.PlayerServiceImpl import PlayerServiceImpl
from player.repository.PlayerRepositoryImpl import PlayerRepositoryImpl


class TestPlayerServiceImpl(unittest.TestCase):

    def test_createPlayer(self):
        mock_repository_instance = MagicMock()
        service = PlayerServiceImpl.getInstance()
        service._PlayerServiceImpl__playerRepository = mock_repository_instance

        mock_player = MagicMock()
        mock_player.getPlayerId.return_value = 1

        mock_repository_instance.createPlayer.return_value = mock_player

        service.createPlayer('MockPlayer')

        mock_repository_instance.createPlayer.assert_called_once_with('MockPlayer')

        created_player = mock_repository_instance.createPlayer.return_value
        self.assertEqual(created_player.getPlayerId(), 1)


if __name__ == "__main__":
    unittest.main()
