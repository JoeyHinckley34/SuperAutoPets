


class Pet():
    def __init__(self,
                Tier = None,
                Name = 'pet-none',
                Attack = None,
                Health = None,
                Trigger_1 = None,
                Trigger_2 = None,
                Trigger_3 = None,
                Ability = None,
                LEVEL_1 = None,
                LEVEL_2 = None,
                LEVEL_3 = None,
                Standard_Pack = None,
                Expansion_Pack_1 = None,
                Expansion_Pack_2 = None,
                ID = None,
                team=None):
                
        
        
        
        self.Tier = Tier
        self.Name = Name
        self.Attack = Attack
        self.Health = Health
        self.Trigger_1 = Trigger_1
        self.Trigger_2 = Trigger_2
        self.Trigger_3 = Trigger_3
        self.Ability = Ability
        self.LEVEL_1 = LEVEL_1
        self.LEVEL_2 = LEVEL_2
        self.LEVEL_3 = LEVEL_3
        self.Standard_Pack = Standard_Pack
        self.Expansion_Pack_1 = Expansion_Pack_1
        self.Expansion_Pack_2 = Expansion_Pack_2
        
        
        self.ID = bin(ID)[2:].zfill(9)
        
        self.team=team
        
        self.eaten = False
        self.level = 1
        self.experience = 0
        
        
        self.TopString = f'LVL:{self.level} {self.experience}/{self.level+1}'
        self.bottomString = f'A:{self.Attack} H:{self.Health}'
        
        #CREATE SHAPE BASED ON ID
        self.topShape = f'{self.ID[:3].replace("0",".").replace("1","*")}'
        self.middleShape = f'{self.ID[3:6].replace("0",".").replace("1","*")}'
        self.bottomShape =f'{self.ID[6:].replace("0",".").replace("1","*")}'
        self.shape = f'{self.topShape}\n{self.middleShape}\n{self.bottomShape}'
        
        
    
    def __str__(self):
        return f'{self.TopString}\n{self.shape}\n{self.Name}\n{self.bottomString}\n'
  
        
