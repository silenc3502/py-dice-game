import unittest
from unittest.mock import patch, MagicMock

from player.repository.PlayerRepositoryImpl import PlayerRepositoryImpl
from player.service.PlayerServiceImpl import PlayerServiceImpl


class TestPlayerRepositoryImpl(unittest.TestCase):

    def test_realCreatePlayer(self):
        repo = PlayerRepositoryImpl.getInstance()
        repo._PlayerRepositoryImpl__playerList.clear()
        repo.createPlayer('MockPlayer')

        players = repo.getPlayerList()
        self.assertEqual(len(players), 1)

        player = players[0]
        self.assertEqual(player.getPlayerNickname(), 'MockPlayer')

    @patch('player.repository.PlayerRepositoryImpl.Player')
    def test_mockCreatePlayer(self, MockPlayer):
        mock_repository_instance = MagicMock()
        mock_repository_instance.getPlayers.return_value = []

        service = PlayerServiceImpl.getInstance()
        service._PlayerServiceImpl__playerRepository = mock_repository_instance

        mock_player = MagicMock()
        mock_player.getPlayerId.return_value = 1
        mock_player.getPlayerNickname.return_value = 'MockPlayer'
        mock_repository_instance.createPlayer.return_value = mock_player

        service.createPlayer('MockPlayer')
        mock_repository_instance.createPlayer.assert_called_once_with('MockPlayer')
        created_player = mock_repository_instance.createPlayer.return_value

        self.assertEqual(created_player.getPlayerId(), 1)
        self.assertEqual(created_player.getPlayerNickname(), 'MockPlayer')

    def test_findPlayerIdByPlayerNickname(self):
        repo = PlayerRepositoryImpl.getInstance()
        repo._PlayerRepositoryImpl__playerList.clear()
        repo.createPlayer('MockPlayer1')
        repo.createPlayer('MockPlayer2')

        player_id1 = repo.findPlayerIdByPlayerNickname('MockPlayer1')
        player_id2 = repo.findPlayerIdByPlayerNickname('MockPlayer2')
        player_id_none = repo.findPlayerIdByPlayerNickname('NonExistentPlayer')

        self.assertIsNotNone(player_id1)
        self.assertIsNotNone(player_id2)
        self.assertNotEqual(player_id1, player_id2)
        self.assertIsNone(player_id_none)


if __name__ == "__main__":
    unittest.main()
