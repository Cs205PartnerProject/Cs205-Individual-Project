from Owner import Owner
from Player import Player
# I considered implementing an alternate constructor that doesn't take a list
# of players.
# Todo Test the see if the Team methods work as expected,
#  particularly focus on the fireOwner, printTeam methods, as these use the teamOwner variable.
class Team:
    name = ''
    teamList = []  # Creating the list that will hold the player objects
    teamOwner = Owner  # I believe this is how we accomplish having an Owner object as a member of out Team class

    # ToDo implement error handling to the constructor
    def __init__(self, listOfTeammates, name, O=Owner):
        self.teamList = []
        if len(listOfTeammates) != 0:
            self.name = name
            # Populating the list of players with the objects in the parameter list
            for i in listOfTeammates:
                in_list = False
                for j in self.teamList:
                    if i.name == j.name:
                        in_list = True
                if not in_list:
                    self.teamList.append(i)

            # Taking information from the owner parameter to the Owner member of this class
            self.teamOwner = O

        if len(listOfTeammates) == 0:
            raise NameError("List of players must be populated with at least one player")

    # the getPlayers method will return all players found in the list
    def getPlayers(self):
        return self.teamList

    # the getName method will return the name of the team
    def getName(self):
        return self.name

    # the newPlayer method will add a new player to the teamlist
    def newPlayer(self, Player=Player):
        self.teamList.append(Player)

    def newOwner(self, owner=Owner):
        if owner.team == self.name:
            self.teamOwner = owner
        else:
            raise ValueError("Cannot issue owner of different team to this team.")


    # fire player searches the list for the parameter player and removes them
    def firePlayer(self, Player=Player):
        # If the below statement fails then no changes will be made to the player roster
        if Player in self.teamList:
            indexOfPlayer = self.teamList.index(Player)
            self.teamList.pop(indexOfPlayer)
            # Change the team of the Player parameter to an empty string
            Player.team = ''
        else:
            raise ValueError("Player must be on team in order to fire them")



    # the fireOwner method removes the owner of the team
    def fireOwner(self):
        self.teamOwner = None

    # the printTeam method prints out all information on the team
    def printTeam(self):
        # Printing of Team name
        print("Name of team:", self.name)
        # Printing the team players
        for i in self.teamList:
            print("Player:", i.name, "is on the", i.team, "owned by", self.teamOwner.name, sep=" ")

    # The findPlayer method was implemented to better test our other methods
    # The findPlayer takes a Player as a parameter and returns a 0 if they are in the team list
    # and returns a -1 if the player is not in the team list
    def findPlayer(self, p=Player):
        if p in self.teamList:
            # player is in list
            return 0

        # If code reaches here we know the player is not in the teamList, thus an exit
        # code of -1 signifies that the player p is in in self.teamList
        return -1








