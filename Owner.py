# This file will contain all methods pertaining to the Owner class
class Owner:
    name = ''
    team = ''

    # Parameterized constructor
    def __init__(self, n, t):
        self.name = n
        self.team = t

    # getName will return the name of the owner
    def getName(self):
        return self.name

    # getTeam will return the name of the owner
    def getTeam(self):
        return self.team

    # changeName will change the name of the Owner to the parameter name
    def changeName(self, n):
        self.name = n

    # changeTeam will change the team of the Owner to the parameter team
    def changeTeam(self, t):
        self.team = t
    
