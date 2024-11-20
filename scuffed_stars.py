camX=0
camY=0
import kandinsky as k
class rectangle:
    def __init__(self,x,y,width,height,color):
        self.x=x
        self.y=y
        self.height=height
        self.width=width
        self.color=color
    def putdata(self,k,l,v):
        colorS=""
        colorB=[str(bin(e))[2:].zfill(8) for e in self.color]
        for i in range(16):
                colorS=colorB[(1+i)%3][i//3]+colorS
        colorS=colorS[:k]+str(bin(v))[2:].zfill(l)[-l:][::-1]+colorS[k+l:]
        colorNB=['' for e in range(3)]
        for i in range(16):
            colorNB[(1-i)%3]+=colorS[i]
        colorN=[int(e.zfill(8)[::-1],2) for e in colorNB]
        self.color=tuple(colorN)
    def render(self):
        k.fill_rect(self.x-camX,self.y-camY,self.height,self.width,(0,0,0))
class circle:
    def __init__(self,x,y,radius,color):
        self.x=x
        self.y=y
        self.radius=radius
        self.color=color
    def putdata(self,k,l,v):
        colorS=""
        colorB=[str(bin(e))[2:].zfill(8) for e in self.color]
        for i in range(16):
                colorS=colorB[(1+i)%3][i//3]+colorS
        colorS=colorS[:k]+str(bin(v))[2:].zfill(l)[-l:][::-1]+colorS[k+l:]
        colorNB=['' for e in range(3)]
        for i in range(16):
            colorNB[(1-i)%3]+=colorS[i]
        colorN=[int(e.zfill(8)[::-1],2) for e in colorNB]
        self.color=tuple(colorN)
    def render(self):
        k.fill_circle(self.x-camX,self.y-camY,self.height,self.width,(0,0,0))
class wall(rectangle):
    def __init__(self,x,y,width,height,color,toughness):
        super().__init__(x,y,width,height,color)
        super().putdata(0,3,0)
        self.toughness=toughness
        super().putdata(3,2,toughness)
class water(rectangle):
    def __init__(self,x,y,width,height,color,hover,breakable):
        super().__init__(x,y,width,height,color)
        super().putdata(0,3,1)
        self.hover=hover
        self.breakable=breakable
        super().putdata(3,1,hover)
        super().putdata(4,1,breakable)
class bush(rectangle):
    def __init__(self,x,y,width,height,color):
        super().__init__(x,y,width,height,color)
        super().putdata(0,3,2)
class projectile(circle):
    def __init__(self,x,y,radius,pierce,wallbreak,damage,team):
        super().__init__(x,y,radius,color)
        super().putdata(0,3,0)
        self.pierce=pierce
        self.wallbreak=wallbreak
        self.damage=damage
        self.team=team
        super().putdata(3,1,pierce)
        super().putdata(4,1,wallbreak)
        super().putdata(5,6,damage)
        super().putdata(11,3,team)
        self.damage=0
        self.direction=0
        self.velocity=0
        self.range=0
class player(circle):
    def __init__(self,x,y,team):
        super().__init__(x,y,10,color)
        super().putdata(0,3,0)
        super().putdata(3,3,team)
        self.health=100
class shelly(player):
    def __init__(self,x,y,team):
        super().__init__(self,x,y,width,radius,team)
        self.health=37
    def attack(self,di):
        return [shellyAttack(x,y,di+i,team) for i in range(-15,15+1,7.5)]
class shellyAttack(projectile):
    def __init__(self,x,y,di,team):
        super().__init__(self,x,y,10,0,0,3,team)
        self.velocity=3100
def getdata(c,k,l):
    colorS=""
    colorB=[str(bin(e))[2:].zfill(8) for e in c]
    for i in range(16):
        colorS=colorB[(1+i)%3][i//3]+colorS
    colorV=colorS[k:k+l]
    return int(colorV[::-1],2)