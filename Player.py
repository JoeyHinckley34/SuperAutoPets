import copy
from Teams import Team
from Shop import Shop


class Player():
    def __init__(self,
                bank = 10,
                lives = 10,
                wins = 0,
                round = 1):
        
        self.team = Team()
        self.bank = bank
        self.lives = lives
        self.wins = wins
        self.round = round
        self.shop = Shop()
        #self.shop.rollShop()


    def __str__(self):
        buf = ''
        buf += '\n+-------------------------------------------------------+\n'
        buf += '|Bank: {:<7}'.format(self.bank)
        buf += 'Lives: {:<7}'.format(self.lives)
        buf += '\t'
        buf += 'Wins: {}/{:<7}'.format(self.wins,10)
        buf += '\t'
        buf += 'Round: {}'.format(self.round)
        buf += '|\n+-------------------------------------------------------+\n'
        buf += str(self.team)
        buf += '\n'
        buf += str(self.shop)
        buf += '\n'
    
        return buf



    def Roll(self):
        self.shop.rollShop()
        
    
    def EndTurn(self):
        pass

    #adds the pet in n position in the shop to the team and removes from shop
    def BuyPet(self,n):
        
        #print(type(self.shop.ShopPets.petList[n]))
        
        p = self.shop.ShopPets.petList[n]
    
        self.team.addPet(copy.copy(p))
    
        self.shop.ShopPets.removePet(n)

        self.bank -= 3
