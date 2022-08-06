import time
import copy
from os import system
from pet import Pet
from createPets import getPets
from Teams import Team, Match
from Player import Player

def main():
    system('clear')
    
    PetList = getPets()
#
#    for a in PetList:
#        print(a)

    Player1 = Player()
    Player1.Roll()
    print(Player1)

    Player1.BuyPet(0)
    print(Player1)

    Player1.BuyPet(0)
    print(Player1)

    Player1.BuyPet(0)
    print(Player1)

#    Team1 = Team()
#    Team1.addPet(PetList[0])
#    print(Team1)
#
#    Team2 = Team()
#    Team2.addPet(PetList[100])
#    print(Team2)
#    
#    Team1.addPet(Team2.petList[0])
#
#    Team2.removePet(0)
#    print(Team1)
#    print(Team2)




#    Team1 = Team(petList=[copy.copy(PetList[1]),copy.copy(PetList[1]),copy.copy(PetList[1]),copy.copy(PetList[1]),copy.copy(PetList[1])])
#    Team2 = Team(petList=[copy.copy(PetList[2]),copy.copy(PetList[3]),copy.copy(PetList[4]),copy.copy(PetList[5]),copy.copy(PetList[6])])
#
#    match1 = Match(Team1,Team2)
#    match1.startMatch()

    
    


if __name__ == '__main__':
    start = time.perf_counter()
    main()
    end = time.perf_counter()
    print('Execution time: ' + str(round(end - start,2)))
