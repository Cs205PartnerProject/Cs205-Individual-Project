import unittest
from Team import Team
from Player import Player
from Owner import Owner


class Test_Player(unittest.TestCase):
    def setUp(self) -> None:
        self.newPlayer = Player("nick", "patriots", 12)

    def test_PlayerName(self):
        self.assertEqual(self.newPlayer.name, "nick")
        self.newPlayer.changeName("brandon")
        self.assertEqual(self.newPlayer.name, "brandon")
        self.assertEqual(self.newPlayer.getName(), self.newPlayer.name)

    def test_PlayerTeam(self):
        self.assertEqual(self.newPlayer.team, "patriots")
        self.newPlayer.changeTeam("bills")
        self.assertEqual(self.newPlayer.team, "bills")
        self.assertEqual(self.newPlayer.getTeam(), self.newPlayer.team)

    def test_PlayerJerseyNumber(self):
        self.assertEqual(self.newPlayer.jerseyNumber, 12)
        self.newPlayer.changeJerseyNumber(55)
        self.assertEqual(self.newPlayer.getJerseyNumber(), self.newPlayer.jerseyNumber)

    ''' STILL NEED TO TEST IS TEAMMATE '''
    # I do not know if I implemented this correctly.
    def test_isTeammate(self):
        testPlayer = Player("Brandon", "Ravens", 8)
        # Test that the teams are not different
        if self.newPlayer.team == testPlayer.name:
            self.assertEqual(self.newPlayer.team, testPlayer.name)
    def tearDown(self) -> None:
        self.newPlayer = None


class Test_Owner(unittest.TestCase):
    def setUp(self) -> None:
        self.newOwner = Owner("jason hibbeler", "eagles")

    def test_OwnerName(self):
        self.assertEqual(self.newOwner.name, "jason hibbeler")
        self.newOwner.changeName("jim eddy")
        self.assertEqual(self.newOwner.name, "jim eddy")
        self.assertEqual(self.newOwner.getName(), self.newOwner.name)

    def test_OwnerTeam(self):
        self.assertEqual(self.newOwner.team, "eagles")
        self.newOwner.changeTeam("bears")
        self.assertEqual(self.newOwner.team, "bears")
        self.assertEqual(self.newOwner.getName(), self.newOwner.name)

    def tearDown(self) -> None:
        self.newOwner = None

class Test_Team(unittest.TestCase):
    def setUp(self) -> None:
        self.newTeam = Team



if __name__ == '__main__':
    unittest.main()
