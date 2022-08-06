from pet import Pet
from os import system
import copy
from time import sleep
import itertools as it

class Team:
    def __init__(self):
        self.petList = []
        self.size = len(self.petList)
        
    def __str__(self):
    
        if self.size == 0:
            return '\n\nEMPTY TEAM\n\n'
    
        buf = ''
        buf += '+-------'+'--------------------'*self.size+'+\n'
        for i in range(6):
            buf += '|\t'
            for a in self.petList:
                if i == 0:
                    buf += '{:20}'.format(a.TopString)
                elif i == 1:
                    buf += '{:20}'.format(a.topShape)
                elif i == 2:
                    buf += '{:20}'.format(a.middleShape)
                elif i == 3:
                    buf += '{:20}'.format(a.bottomShape)
                elif i == 4:
                    buf += '{:20}'.format(a.Name)
                elif i == 5:
                    buf += '{:20}'.format(a.bottomString)

            buf += '|\n'
        
        buf += '+-------'+'--------------------'*self.size+'+\n'
        return buf
        
    def update(self):
        self.petList = [x for x in self.petList if x.Health > 0]
        self.size = len(self.petList)
    
    
    def removePet(self,i):
        self.petList.pop(i)
        self.size = len(self.petList)
        
    def addPet(self,p):
        self.petList.append(copy.copy(p))
        self.size = len(self.petList)
    
    def addPets(self,pets):
        for p in pets:
            self.petList.append(copy.copy(p))
        self.size = len(self.petList)
    
class Match:
    def __init__(self,Team1,Team2):
        self.Team1 = Team1
        self.Team2 = Team2
        self.TeamList = [Team1,Team2]
        
    def __str__(self):
        
        if self.Team1.size == 0 and self.Team2.size == 0 :
            return '\nDRAW\n'
        
        buf = ''
           
        if self.Team1.size == 0:
            return str(self.Team2) + '\nTEAM 2 WIN\n'
         
        if self.Team2.size == 0:
            return str(self.Team1) + '\nTEAM 1 WIN\n'
            
            
        flip = False
        for i in range(6):
            buf += '|\t'
            numTeam = 0
            for j in it.chain(range(self.Team1.size-1,-1,-1), range(0, self.Team2.size)):
                #print(i,j,numTeam)
                if i == 0:
                    buf += '{:15}'.format(self.TeamList[numTeam].petList[j].TopString)
                elif i == 1:
                    buf += '{:15}'.format(self.TeamList[numTeam].petList[j].topShape)
                elif i == 2:
                    buf += '{:15}'.format(self.TeamList[numTeam].petList[j].middleShape)
                elif i == 3:
                    buf += '{:15}'.format(self.TeamList[numTeam].petList[j].bottomShape)
                elif i == 4:
                    buf += '{:15}'.format(self.TeamList[numTeam].petList[j].Name)
                elif i == 5:
                    buf += '{:15}'.format(self.TeamList[numTeam].petList[j].bottomString)
                
                if j == 0 and flip == False:
                    numTeam += 1
                    numTeam = numTeam%2
                    flip = True
                    buf += '|\t'
                else:
                    flip = False
                    
            buf += '|\n'
            
        return buf


    
    
    
    
    #private method
    #Each teams first enemy attacks
    def __attack(self):
        #TO DO:
        #CHECK TEAMS FOR BEFORE ATTACK TRIGGERS
        
        self.Team2.petList[0].takeDamage(self.Team1.petList[0].Attack)
        self.Team1.petList[0].takeDamage(self.Team2.petList[0].Attack)
        
        print(self)
        # sleep for 1 seconds after printing output
        #sleep(1)
        system('clear')
        
        self.Team1.update()
        self.Team2.update()
        
        self.TeamList = [self.Team1,self.Team2]
        #TO DO:
        #CHECK TEAMS FOR AFTER ATTACK TRIGGERS
    
    

    def startMatch(self):
        #TO DO:
        #CHECK TEAMS FOR START OF MATCH TRIGGERS
        
        
        while(self.Team1.size > 0 and self.Team2.size > 0):
            system('clear')
            print(self)
            # sleep for 2 seconds after printing output
            #sleep(1)
            system('clear')
            self.__attack()
            print(self)
            # sleep for 2 seconds after printing output
            #sleep(1)
            system('clear')
            
            if self.Team1.size == 0:
                print( str(self.Team2) + '\nTEAM 2 WIN\n')
         
            if self.Team2.size == 0:
                print( str(self.Team1) + '\nTEAM 1 WIN\n')
            
        
        
        
