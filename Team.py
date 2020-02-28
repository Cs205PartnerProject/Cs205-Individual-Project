import Owner
import Player
# I considered implementing an alternate constructor that doesn't take a list
# of players.
# Todo Test the see if the Team methods work as expected, particularly focus on the fireOwner, printTeam methods, as these use the teamOwner
# Todo variable.
class Team:
    name = ''
    # Creating the list that will hold the player objects
    teamList = []
    # I believe this is how we accomplish having an Owner object as a member of out Team class
    teamOwner = Owner
    # ToDo implement error handling to the constructor
    def __init__(self,listOfTeammates,n,O = Owner):
        self.name = n
        # Populating the list of players with the objects in the parameter list
        for i in listOfTeammates:
            self.teamList.append(i)
        # Taking information from the owner parameter to the Owner member of this class
        self.teamOwner.Owner(O.Owner.name,O.Owner.team)
    # the getPlayers method will return all players found in the list
    def getPlayer(self):
        return self.teamList
    # the getName method will return the name of the team
    def getName(self):
        return self.name
    # the newPlayer method will add a new player to the teamlist
    def newPlayer(self,Player = Player):
        self.teamList.append(Player)
    # fire player searches the list for the parameter player and removes them
    # Todo implement error handling if the Player is not on the team
    def firePlayer(self,Player = Player):
        indexOfPlayer = self.teamList.index(Player)
        self.teamList.pop(indexOfPlayer)
        # Change the team of the Player parameter to an empty string
        Player.Player.team = ''
    # the fireOwner method fires the owner of the team and replaces him with
    # a new owner
    def fireOwner(self,nO = Owner):
        # Change the Owners team name to the empty string
        self.teamOwner.Owner.team = ''
        # Setting self.teamOwner equal to the the new Owner parameter.
    # the printTeam method prints out all information on the team
    def printTeam(self):
        # having an Owner object be associated with the team.
        print("The owner of the team is:", self.teamOwner.Owner.name,'\n')
        # Printing of Team name
        print("Name of team:",self.name,'\n')
        # Printing the team players
        for i in self.teamList:
            print("Player:",i,"is",self.teamList[i],'\n')
    # The findPlayer method was implemented to better test our other methods
    # The findPlayer takes a Player as a parameter and returns a 0 if they are in the team list
    # and returns a -1 if the player is not in the team list
    def findPlayer(self,p):
        for i in self.teamList:
            if i == p:
                # Below print statement done as a test
                print("Player",p,"equals player",i)
                # return of 0 indicates player was found
                return 0
        # If code reaches here we know the player is not in the teamList, thus an exit
        # code of -1 signifies that the player p is in in self.teamList
        return -1





