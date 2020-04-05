import unittest
from Team import Team
from Player import Player
from Owner import Owner


class Test_Player(unittest.TestCase):
    def setUp(self) -> None:
        self.newPlayer = Player("nick", "patriots", 12)

    def test_PlayerName(self):
        print("Entering test_PlayerName in Test_Player")
        self.assertEqual(self.newPlayer.name, "nick")
        self.newPlayer.changeName("brandon")
        self.assertEqual(self.newPlayer.name, "brandon")
        self.assertEqual(self.newPlayer.getName(), self.newPlayer.name)

    def test_PlayerTeam(self):
        print("Entering test_PlayerTeam in Test_Player")
        self.assertEqual(self.newPlayer.team, "patriots")
        self.newPlayer.changeTeam("bills")
        self.assertEqual(self.newPlayer.team, "bills")
        self.assertEqual(self.newPlayer.getTeam(), self.newPlayer.team)

    def test_PlayerJerseyNumber(self):
        print("Entering test_PlayerJerseyNumber in Test_Player")
        self.assertEqual(self.newPlayer.jerseyNumber, 12)
        self.newPlayer.changeJerseyNumber(55)
        self.assertEqual(self.newPlayer.getJerseyNumber(), self.newPlayer.jerseyNumber)

    def test_isTeammate(self):
        print("Entering test_isTeammate in Test_Player")
        testPlayer = Player("Brandon", "Ravens", 8)
        self.assertFalse(testPlayer.isTeammate(self.newPlayer))


    def tearDown(self) -> None:
        print("Teardown Player")
        self.newPlayer = None
        print()


class Test_Owner(unittest.TestCase):
    def setUp(self) -> None:
        print("Entering owner setup")
        self.newOwner = Owner("jason hibbeler", "eagles")

    def test_OwnerName(self):
        print("Entering test_OwnerName in Test_Owner")
        self.assertEqual(self.newOwner.name, "jason hibbeler")
        self.newOwner.changeName("jim eddy")
        self.assertEqual(self.newOwner.name, "jim eddy")
        self.assertEqual(self.newOwner.getName(), self.newOwner.name)

    def test_OwnerTeam(self):
        print("Entering test_OwnerTeam in Test_Owner")
        self.assertEqual(self.newOwner.team, "eagles")
        self.newOwner.changeTeam("bears")
        self.assertEqual(self.newOwner.team, "bears")
        self.assertEqual(self.newOwner.getName(), self.newOwner.name)

    def tearDown(self) -> None:
        print("Teardown Owner")
        self.newOwner = None
        print()


# Still need to go through and make sure all of these test cases work.
class Test_Team(unittest.TestCase):
    def setUp(self) -> None:
        print("Entering team setup")
        self.brandon = Player("Brandon", "Ravens", 8)
        self.nick = Player("Nick", "Ravens", 9)
        self.hunter = Player("Hunter", "Ravens", 10)
        self.teamMates = [self.brandon, self.nick, self.hunter]
        self.owner = Owner("Jason hibbeler", "Ravens")
        self.newTeam = Team(self.teamMates, "Ravens", self.owner)
        self.newTeam.printTeam()

    def tearDown(self) -> None:
        print("TearDown Team")
        self.newTeam = None
        print()

    def test_players(self):
        self.assertRaises(NameError, Team, [], "Blues", self.owner)
        print("Entering test_players in Test_Team")
        self.assertEqual(self.newTeam.teamList[0], self.brandon)
        self.assertEqual(self.newTeam.teamList[1], self.nick)
        self.assertEqual(self.newTeam.teamList[2], self.hunter)
        self.assertEqual(self.newTeam.teamList[0].team, "Ravens")
        self.assertEqual(self.newTeam.teamList[1].team, "Ravens")
        self.assertEqual(self.newTeam.teamList[2].team, "Ravens")
        self.assertEqual(self.newTeam.teamList, self.newTeam.getPlayers())

    def test_getters(self):
        self.assertEqual(self.newTeam.teamList, self.newTeam.getPlayers())
        self.assertEqual(self.newTeam.name, self.newTeam.getName())



    def test_newPlayer(self):
        print("Entering test_newPlayer in Test_Team")
        maxx = Player("Maxx", "Ravens", 98)
        self.newTeam.newPlayer(maxx)
        self.assertEqual(self.newTeam.teamList[3].name, "Maxx")
        self.assertEqual(self.newTeam.teamList[3].team, "Ravens")
        self.newTeam.printTeam()


    def test_firePlayer(self):
        print("Entering test_firePlayer in Test_Team")
        self.assertEqual(self.newTeam.teamList, self.teamMates)
        test_list2 = [self.brandon, self.nick]
        self.newTeam.firePlayer(self.hunter)
        self.assertEqual(self.newTeam.teamList, test_list2)
        diffPlayer = Player("Bernie Sanders", "Bills", 99)
        self.assertRaises(ValueError, self.newTeam.firePlayer, diffPlayer)


    def test_owner(self):
        print("Entering test_owner in Test_Team")
        self.assertEqual(self.newTeam.teamOwner, self.owner)
        self.assertEqual(self.newTeam.teamOwner.name, "Jason hibbeler")
        self.assertEqual(self.newTeam.teamOwner.team, "Ravens")

    def test_newOwner(self):
        print("Entering test_newOwner in Test_Team")
        newOwner = Owner("Tome Hanks", "Ravens")
        newOwnerDiffTeam = Owner("Bill Gates", "Colts")
        self.newTeam.newOwner(newOwner)
        self.assertEqual(self.newTeam.teamOwner, newOwner)
        self.assertRaises(ValueError, self.newTeam.newOwner, newOwnerDiffTeam)


    def test_fireOwner(self):
        print("Entering test_fireOwner in Test_Team")
        self.newTeam.fireOwner()
        self.assertEqual(self.newTeam.teamOwner, None)

    def test_findPlayer(self):
        test_player = Player("Howard", "Bears", 43)
        self.assertEqual(self.newTeam.findPlayer(self.nick), 0)
        self.assertEqual(self.newTeam.findPlayer(test_player), -1)




if __name__ == '__main__':
    unittest.main()
