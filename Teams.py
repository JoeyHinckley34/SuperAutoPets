from pet import Pet

class Team:
    def __init__(self,
                 petList = []):
        self.petList = petList
        self.size = len(self.petList)
        
    def __str__(self):
        buf = ''
        for i in range(6):
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
                buf += '\t'
            buf += '\n'
        return buf
        
    def addPet(self,p):
        self.petList.append(p)
   

