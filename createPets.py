import time
import pandas as pd
from pet import Pet

#@returns PetList: List of all pets in game as Pet objects
def getPets():

    #Read in excel input file to a panads dataframe
    df = pd.read_excel('PetsInput.xlsx')
    
    #GET THE COLUMN NAMES AND NUMBER OF ROWS
    cols = list(df)
    rows_count = len(df.index)

    #LIST TO STORE ALL PETS
    PetList = []

    #Create new Pet object for each row in dataframe
    for j in range(rows_count):
        newpet = Pet(Tier = df[cols[0]][j],
                     Name = df[cols[1]][j],
                     Attack = df[cols[2]][j],
                     Health = df[cols[3]][j],
                     Trigger_1 = df[cols[4]][j],
                     Trigger_2 = df[cols[5]][j],
                     Trigger_3 = df[cols[6]][j],
                     Ability = df[cols[7]][j],
                     LEVEL_1 = df[cols[8]][j],
                     LEVEL_2 = df[cols[9]][j],
                     LEVEL_3 = df[cols[10]][j],
                     Standard_Pack= df[cols[11]][j],
                     Expansion_Pack_1 = df[cols[12]][j],
                     Expansion_Pack_2 = df[cols[13]][j],
                     ID = j+1)
        PetList.append(newpet)
        
    return PetList


def main():
    PetList = getPets()
#    for p in PetList:
#        print(p)
    
    
if __name__ == '__main__':
    start = time.perf_counter()
    main()
    end = time.perf_counter()
    print('Execution time: ' + str(round(end - start,2)))

