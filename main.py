import time
from pet import Pet
from createPets import getPets
from Teams import Team

def main():
    
    PetList = getPets()

    for a in PetList:
        if a.Tier == 1:
            print(a)
    
    Team1 = Team()
    
    Team1.addPet(PetList[22])
    Team1.addPet(PetList[87])
    Team1.addPet(PetList[150])
    print(Team1)



if __name__ == '__main__':
    start = time.perf_counter()
    main()
    end = time.perf_counter()
    print('Execution time: ' + str(round(end - start,2)))
