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


# Still need to go through and make sure all of these test cases work.
class Test_Team(unittest.TestCase):



    def setUp(self) -> None:
        print("Entering team setup")
        self.brandon = Player("Brandon", "Ravens", 8)
        self.nick = Player("Nick", "Ravens", 9)
        self.hunter = Player("Hunter", "Ravens", 10)
        self.teamMates = [self.brandon, self.nick, self.hunter]
        print(self.teamMates)
        self.owner = Owner("Jason hibbeler", "Ravens")
        self.newTeam = Team(self.teamMates, "Ravens", self.owner)
        print(self.newTeam.teamList)

    def tearDown(self) -> None:
        print("TearDown")
        self.newTeam.teamList = []
        print(self.newTeam.teamList)
        self.newTeam.teamOwner = None
        self.newTeam.name = None
        self.teamMates = []
        self.newTeam = None

    def test_players(self):
        print("Entering test_players in Test_Team")
        self.assertEqual(self.newTeam.teamList[0].name, "Brandon")
        self.assertEqual(self.newTeam.teamList[1].name, "Nick")
        self.assertEqual(self.newTeam.teamList[2].name, "Hunter")
        self.assertEqual(self.newTeam.teamList[0].team, "Ravens")
        self.assertEqual(self.newTeam.teamList[1].team, "Ravens")
        self.assertEqual(self.newTeam.teamList[2].team, "Ravens")

    def test_newPlayer(self):
        print("Entering test_newPlayer in Test_Team")
        maxx = Player("Maxx", "Ravens", 98)
        self.newTeam.newPlayer(maxx)
        self.assertEqual(self.newTeam.teamList[3].name, "Maxx")
        self.assertEqual(self.newTeam.teamList[3].team, "Ravens")


    def test_firePlayer(self):
        print("Entering test_firePlayer")
        # self.assertEqual(self.newTeam.teamList, self.teamMates)
        # test_list2 = [brandon,nick]
        # self.test_firePlayer(hunter)
        # self.assertEqual(self.newTeam.teamList,test_list2)

    # def test_owner(self):
    #     testOwner = Owner("Jason hibbeler", "Ravens")
    #     self.assertEqual(self.newTeam.teamOwner, testOwner)
    # Still need to test fireOwner and find Player



if __name__ == '__main__':
    unittest.main()
