# I considered implementing an alternate constructor that doesn't take a list
# of players.
class Team:
    name = ''
    # Creating the list that will hold the player objects
    teamList = []

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
        indexOfPlayer = list.index(Player)
        list.pop(indexOfPlayer)
    # the fireOwner method fires the owner of the team and replaces him with
    # a new owner
    def fireOwner(self,nO):
        self.




