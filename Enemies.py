from Functions import *
class Enemy(pygame.sprite.Sprite):
    knockback=[]
    knockbackCounter=0
    effects=[0,0,0,0,0,0,0,0,0,0,0,0]
    rightCounter=0
    leftCounter=0
    upCounter=0
    downCounter=0
    meleeAttackSpeed=0
    rangedAttackSpeed=0
    rangedAttackCooldown=0
    meleeAttackCooldown=0
    xChange=0
    yChange=0
    def __init__(self,sprite,defense,block,maxHp,speed,rangedDamage,rangedSharpness,rangedKnockback,rangedAttackSpeed,rangedVelocity,meleeDamage,meleeRange,meleeSharpness,meleeKnockback,meleeAttackSpeed,x,y,player,xp,level):
        super().__init__()
        self.image=pygame.image.load(path.join("Sprites",sprite)).convert()
        self.image.set_colorkey(BASE)
        self.rect=self.image.get_rect()
        self.rect.x=x
        self.rect.y=y
        self.xp=xp+level
        self.meleeAttackSpeed=meleeAttackSpeed
        self.meleeKnockback=8*meleeKnockback
        self.meleeSharpness=meleeSharpness+int(level/5)
        self.meleeDamage=meleeDamage+level
        self.meleeRange=meleeRange
        self.rangedKnockback=8*rangedKnockback
        self.rangedAttackSpeed=rangedAttackSpeed
        self.rangedDamage=rangedDamage
        self.rangedKnockback=rangedKnockback
        self.rangedVelocity=rangedVelocity
        self.defense=defense+int(level/4)
        self.block=block
        self.maxHp=maxHp+level
        self.hp=maxHp+level
        self.speed=speed
    def ai(self,player,weaponLists,screen):
        if self.hp<=0:
            self.kill()
            player.xp+=self.xp
            return
        if not self.meleeAttackCooldown:
            self.meleeAttackCooldown=self.meleeAttackSpeed
            if collision(self,player):
                damage=damageCalc(player.defense,self.meleeSharpness,player.armorRating,self.meleeDamage,player.block)
                damageTitle=font3.render(str(damage),1,RED)
                screen.blit(damageTitle,(player.rect.x+randrange(-5,25),player.rect.y+randrange(-5,15)))
                choice([playerHitSound,playerHitSound2]).play()
                if player.facing=="right":
                    player.knockback=["-","x"]
                    player.facing="left"
                elif player.facing=="left":
                    player.knockback=["+","x"]
                    player.facing="right"
                elif player.facing=="up":
                    player.knockback=["+","y"]
                    player.facing="down"
                else:
                    player.knockback=["-","y"]
                    player.facing="up"
                player.reset(weaponLists,True)
                player.knockbackCounter=self.meleeKnockback
                player.newHp=self.hp-damage
        else:
            self.meleeAttackCooldown-=1
class FollowingEnemy(Enemy):
    trackingCooldown=0
    x=False
    y=False
    def __init__(self,sprite,defense,block,maxHp,speed,rangedDamage,rangedSharpness,rangedKnockback,rangedAttackSpeed,rangedVelocity,meleeDamage,meleeRange,meleeSharpness,meleeKnockback,meleeAttackSpeed,x,y,player,xp,knockbackImmunity,level):
        super().__init__(sprite,defense,block,maxHp,speed,rangedDamage,rangedSharpness,rangedKnockback,rangedAttackSpeed,rangedVelocity,meleeDamage,meleeRange,meleeSharpness,meleeKnockback,meleeAttackSpeed,x,y,player,xp,level)
        self.knockbackImmunity=knockbackImmunity
    def changeSprites(up=False,down=False,left=False,right=False):
        pass
    def ai(self,wallList,player,weaponLists,screen):
        super().ai(player,weaponLists,screen)
        blockHit=pygame.sprite.spritecollide(self,wallList,False)
        if not blockHit:
            if self.knockback!=[] and not self.knockbackImmunity:
                exec("self.rect."+self.knockback[1]+self.knockback[0]+"=8")
                self.knockbackCounter-=8
                if self.knockbackCounter<=0:
                    self.knockback=[]
        else:
            if self.x:
                self.x=False
            elif self.y:
                self.y=False
        for block in blockHit:
            if self.rect.top<block.rect.bottom and self.rect.bottom>block.rect.bottom:
                self.rect.top=block.rect.bottom
            elif self.rect.bottom>block.rect.top and self.rect.top<block.rect.top:
                self.rect.bottom=block.rect.top
            if self.rect.left<block.rect.right and self.rect.right>block.rect.right:
                self.rect.left=block.rect.right
            elif self.rect.right>block.rect.left and self.rect.left<block.rect.left:
                self.rect.right=block.rect.left
        if onScreen(self)and not self.knockback:
            if not(self.rect.y+int(self.speed/2)>=player.rect.y and self.rect.y-int(self.speed/2)<=player.rect.y)and not self.x:
                if self.rect.y>=player.rect.y:
                    self.rect.y-=self.speed
                    self.changeSprites(True)
                elif self.rect.y<=player.rect.y:
                    self.rect.y+=self.speed
                    self.changeSprites(down=True)
                self.y=True
            else:
                self.y=False
            if not(self.rect.x+int(self.speed/2)>=player.rect.x and self.rect.x-int(self.speed/2)<=player.rect.x)and not self.y:
                if self.rect.x>=player.rect.x:
                    self.rect.x-=self.speed
                    self.changeSprites(left=True)
                elif self.rect.x<=player.rect.x:
                    self.rect.x+=self.speed
                    self.changeSprites(right=True)
                self.x=True
            else:
                self.x=False
class Knight(FollowingEnemy):
    rightCounter=0
    leftCounter=0
    upCounter=0
    downCounter=0
    def __init__(self,x,y,player,level):
        image="Knight_Down.png"
        super().__init__(image,10,3,25,1, False,0,0,0,0,5,2,3,3,30,x,y,player,20,False,level)
    def changeSprites(self,up=False,left=False,right=False,down=False):
        if right:
            if self.rightCounter%16>=7:
                self.image=ppygame.image.load(path.join("Sprites" ,"Knight_Right1.png")).convert()
            else:
                self.image=pygame.image.load(path.join("Sprites" ,"Knight_Right2.png")).convert()
            self.rightCounter+=1
        elif left:
            if self.leftCounter%16>=7:
                self.image=pygame.image.load(path.join("Sprites" ,"Knight_Left1.png")).convert()
            else:
                self.image=pygame.image.load(path.join("Sprites" ,"Knight_Left2.png")).convert()
            self.leftCounter+=1
        elif up:
            if self.upCounter%16>=7:
                self.image=pygame.image.load(path.join("Sprites" ,"Knight_Up1.png")).convert()
            else:
                self.image=pygame.image.load(path.join("Sprites" ,"Knight_Up2.png")).convert()
            self.upCounter+=1    
        elif down:
            if self.downCounter%16<=7:
                self.image=pygame.image.load(path.join("Sprites" ,"Knight_Down1.png")).convert()
            else:
                self.image=pygame.image.load(path.join("Sprites" ,"Knight_Down2.png")).convert()
            self.downCounter+=1
        self.image.set_colorkey(BASE)
class Star(FollowingEnemy):
    spriteCounter=20
    def __init__(self,x,y,player,level):
        super().__init__("Star1.png",5,1,25,2, False,0,0,0,0,3,1,5,5,20,x,y,player,25,False,level)
        self.sprite1=pygame.image.load(path.join("Sprites","Star1.png")).convert()
        self.sprite2=pygame.image.load(path.join("Sprites","Star2.png")).convert()
        self.sprite1.set_colorkey(BASE)
        self.sprite2.set_colorkey(BASE)
    def ai(self,WallList,player,weaponLists,screen):
        super().ai(WallList,player,weaponLists,screen)
        if self.spriteCounter==0:
            if random()>0.5:
                self.image=self.sprite2
            else:
                self.image=self.sprite2
            self.spriteCounter=20
        else:
            self.spriteCounter-=1
