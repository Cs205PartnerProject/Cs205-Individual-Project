import unittest
from Team import Team
from Player import Player
from Owner import Owner


class TestPlayer(unittest.TestCase):
    def setUp(self) -> None:
        self.newPlayer = Player("nick", "patriots", 12)

    def testPlayerName(self):
        self.assertEqual(self.newPlayer.name, "nick")
        self.newPlayer.changeName("brandon")
        self.assertEqual(self.newPlayer.name, "brandon")
        self.assertEqual(self.newPlayer.getName(), self.newPlayer.name)

    def testPlayerTeam(self):
        self.assertEqual(self.newPlayer.team, "patriots")
        self.newPlayer.changeTeam("bills")
        self.assertEqual(self.newPlayer.team, "bills")
        self.assertEqual(self.newPlayer.getTeam(), self.newPlayer.team)

    def testPlayerJerseyNumber(self):
        self.assertEqual(self.newPlayer.jerseyNumber, 12)
        self.newPlayer.changeJerseyNumber(55)
        self.assertEqual(self.newPlayer.getJerseyNumber(), self.newPlayer.jerseyNumber)

    ''' STILL NEED TO TEST IS TEAMMATE '''

    def tearDown(self) -> None:
        self.newPlayer = None


class TestOwner(unittest.TestCase):
    def setUp(self) -> None:
        self.newOwner = Owner("jason hibbeler", "eagles")

    def testOwnerName(self):
        self.assertEqual(self.newOwner.name, "jason hibbeler")
        self.newOwner.changeName("jim eddy")
        self.assertEqual(self.newOwner.name, "jim eddy")
        self.assertEqual(self.newOwner.getName(), self.newOwner.name)

    def testOwnerTeam(self):
        self.assertEqual(self.newOwner.team, "eagles")
        self.newOwner.changeTeam("bears")
        self.assertEqual(self.newOwner.team, "bears")
        self.assertEqual(self.newOwner.getName(), self.newOwner.name)

    def tearDown(self) -> None:
        self.newOwner = None


class TestTeam(unittest.TestCase):
    def setUp(self) -> None:
        self.player1 = Player("nick", "broncos", 11)
        self.player2 = Player("john", "broncos", 63)
        self.player3 = Player("tom", "broncos", 44)
        self.playerList = [self.player1, self.player2, self.player3]
        self.owner = Owner("jack", "broncos")
        self.newTeam = Team(self.playerList, "broncos", self.owner)

    def testPlayers(self):
        self.assertEqual(self.newTeam.getPlayers(), [self.player1, self.player2, self.player3])
        self.newTeam.firePlayer(self.player1)
        self.assertEqual(self.newTeam.getPlayers(), [self.player2, self.player3])
        self.assertEqual(self.newTeam.findPlayer(self.player2), 0)
        self.assertEqual(self.newTeam.findPlayer(self.player1), -1)
        self.newTeam.printTeam()
        self.assertEqual(self.newTeam.getPlayers(), self.playerList)

    # def testOwner(self):
    #     self.assertEqual(self.newTeam.getOwner(), "jack")
    #     self.newTeam.fireOwner()
    #     self.assertEqual(self.newTeam.getOwner(), None)
    #
    #






if __name__ == '__main__':
    unittest.main()
