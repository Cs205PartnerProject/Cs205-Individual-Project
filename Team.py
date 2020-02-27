# I considered implementing an alternate constructor that doesn't take a list
# of players.
class Team:
    name = ''
    # Creating the list that will hold the player objects
    teamList = []
    # ToDo figure out how to implement an Owner object as a part of this class

    # ToDo implement error handling to the constructor
    def __init__(self,listOfTeammates,n):
        self.name = n
        # Populating the list of players with the objects in the parameter list
        for i in listOfTeammates:
            self.teamList.append(i)
    # the getPlayers method will return all players found in the list
    def getPlayer(self):
        return self.teamList
    # the getName method will return the name of the team
    def getName(self):
        return self.name
    # the newPlayer method will add a new player to the teamlist
    def newPlayer(self,Player):
        self.teamList.append(Player)
    # fire player searches the list for the parameter player and removes them
    # Todo implement error handling if the Player is not on the team
    def firePlayer(self,Player):
        indexOfPlayer = self.teamList.index(Player)
        self.teamList.pop(indexOfPlayer)
    # the fireOwner method fires the owner of the team and replaces him with
    # a new owner
    # ToDo implement the below method when i figure out a solution to the above problem.
    #def fireOwner(self,nO):

    # the printTeam method prints out all information on the team
    def printTeam(self):
        # Todo implement the printing of the owner information

        # Printing of Team name
        print("Name of team:",self.name,'\n')
        # Printing the team players
        for i in self.teamList:
            print("Player:",i,"is",self.teamList[i],'\n')






