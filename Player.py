# Contains all code for the Player object
class Player:
    name = ''
    team = ''
    jerseyNumber = 0

    def __init__(self, n, t, jN):
        self.name = n
        self.team = t
        self.jerseyNumber = jN
    # getName returns the name of the player
    def getName(self):
        return self.name

    # getTeam returns the team of the player
    def getTeam(self):
        return self.team

    # getJerseyNumber will return the jersey number of the player
    def getJerseyNumber(self):
        return self.jerseyNumber

    # changeName changes the name of the player to the parameter
    def changeName(self, n):
        self.name = n

    # changeTeam changes the team of the player to the parameter
    def changeTeam(self, t):
        self.team = t

    # Change jerseyNumber changes the jersey number to the parameter
    def changeJerseyNumber(self, jN):
        self.jerseyNumber = jN

    # isTeammate checks to see if the
    # parameter player and this team are on the same team
    # Todo implement error handling for the below function
    def isTeammate(self, otherPlayer):
        if otherPlayer.team == self.team:
            return True
        else:
            return False

