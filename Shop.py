from createPets import getAllShopPets
from Teams import Team
import random

class Shop:
    def __init__(self,
                ShopLevel = 1):
                
        self.ShopPets = Team()
        self.ShopLevel = ShopLevel
        
        
    def __str__(self):
        if self.ShopPets.size == 0:
            return '\nEMPTY SHOP\n'
            
        return f'{self.ShopPets}'

    def rollShop(self):
        #TO DO ADD freeze
        AllShopPets = getAllShopPets(self.ShopLevel)
        self.ShopPets.addPets(random.sample(AllShopPets,3))
        
        
