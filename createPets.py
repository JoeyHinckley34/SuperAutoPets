import time

def main():
    
    
    trigTypes = ['Buy',
                 'Sell',
                 'Faint',
                 'Level-up',
                 'No effect',
                 'Friend Summoned',
                 'Start of Battle'
                 ]
    
    names = ['Ant',
             'Beaver',
             'Cricket',
             'Duck',
             'Fish',
             'Horse',
             'Mosquito',
             'Otter',
             'Pig']
             
    damages =  [2,3,1,2,2,2,2,1,4]
    healths =  [1,2,2,3,2,1,2,2,1]
    triggers = [2,1,2,1,3,5,6,0,1]


    for x in range(len(names)):
        print(f'{names[x]} {damages[x]} {healths[x]} {trigTypes[triggers[x]]}')


if __name__ == '__main__':
    start = time.perf_counter()
    main()
    end = time.perf_counter()
    print('Execution time: ' + str(round(end - start,2)))

