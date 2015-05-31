from Game import *
def main():
    meleeList=pygame.sprite.Group()
    wallList=pygame.sprite.Group()
    itemList=pygame.sprite.Group()
    enemyList=pygame.sprite.Group()
    doorList=pygame.sprite.Group()
    projectileList=pygame.sprite.Group()
    backgroundList=pygame.sprite.Group()
    foregroundList=pygame.sprite.Group()
    animationList=pygame.sprite.Group()
    weaponLists=[meleeList,projectileList]
    player=Player()
    backgrounds=[Background(0,0,"Dungeon_Floor.png"),Background(320,0,"Dungeon_Floor.png")]
    for grass1 in range(-8,8):
        for grass2 in range(-4,4):
            backgrounds.append(Background(-5000+grass1*704,-5000+grass2*496,"Grass_Background.png"))
    for background in backgrounds:
        backgroundList.add(background)
    enemy=Star(200,200,player,10)
    enemyList.add(enemy)
    paused=False
    end=False
    fps=30
    gameReset(wallList,itemList,enemyList,player,doorList)
    player.update(wallList,itemList,enemyList,weaponLists,backgroundList,doorList)
    while not end:
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                end=True
            elif event.type==pygame.KEYDOWN:
                if not paused:
                    if player.canMove==True:
                        if event.key in(pygame.K_LEFT,pygame.K_a):
                            player.goLeft()
                        elif event.key in(pygame.K_RIGHT,pygame.K_d):
                            player.goRight()
                        elif event.key in(pygame.K_UP,pygame.K_w):
                            player.goUp()
                        elif event.key in(pygame.K_DOWN,pygame.K_s):
                            player.goDown()
                if event.key==pygame.K_ESCAPE:
                    menuSelect.play()
                    if not paused:
                        paused=True
                    else:
                        paused=False
                elif event.key==pygame.K_RETURN:
                    fps=90
            elif event.type==pygame.MOUSEBUTTONDOWN:
                if event.button==1 and not player.meleeAttackCooldown and player.meleeClass:
                    player.meleeWeapon.attack(meleeList,player)
                elif event.button==3 and not player.rangedAttackCooldown and player.rangedClass:
                    player.rangedWeapon.attack(projectileList,player)
            elif event.type==pygame.KEYUP and not paused:
                if event.key in(pygame.K_LEFT,pygame.K_a):
                    player.moving=False
                    player.left=False
                elif event.key in(pygame.K_RIGHT,pygame.K_d):
                    player.moving=False
                    player.right=False
                elif event.key in(pygame.K_UP,pygame.K_w):
                    player.moving=False
                    player.up=False
                elif event.key in(pygame.K_DOWN,pygame.K_s):
                    player.moving=False
                    player.down=False
                elif event.key==pygame.K_RETURN:
                    fps=30
        if RAINBOW==RED and randrange(0,5)==4:
            RAINBOW=(255,128,0)
        elif RAINBOW==(255,128,0) and randrange(0,5)==4:
            RAINBOW=YELLOW
        elif RAINBOW==YELLOW and randrange(0,5)==4:
            RAINBOW=GREEN
        elif RAINBOW==GREEN and randrange(0,5)==4:
            RAINBOW=BLUE
        elif RAINBOW==BLUE and randrange(0,5)==4:
            RAINBOW=BASE
        elif RAINBOW==BASE and randrange(0,3)==2:
            RAINBOW=RED
        mousePos=pygame.mouse.get_pos()
        screen.fill(BLACK)
        if paused:
            playerImage=pygame.transform.scale(pygame.image.load(path.join("Sprites","Player_Down.png")).convert(),(64,64))
            playerImage.set_colorkey(BASE)
            screen.blit(playerImage,(5,5))
            pygame.draw.rect(screen,RED,(76,2,70,70))
            pygame.draw.rect(screen,BLUE,(150,2,70,70))
            screen.blit(player.meleeWeapon.sprite,(79,5))
            screen.blit(player.rangedWeapon.sprite,(153,5))
            if any(player.effects):
                unused=0
                for effect in range(len(player.effects)):
                    if player.effects[effect]:
                        x=237+effect*42-unused  
                        screen.blit(statuses[effect][0],(x,5))
                        if mouseOver(x,x+32,5,37):
                            statusTitle=font1.render(statuses[effect][1],1,YELLOW)
                            screen.blit(statusTitle,(mousePos[0]+10,mousePos[1]+20))
                            timer=font1.render("Duration: "+str(player.effects[effect]),1,YELLOW)
                            screen.blit(timer,(5,79))
                    else:
                        unused+=42
            if mouseOver(79,143,5,69) and player.meleeClass:
                meleeTagTitle=font2.render(player.meleeName+": "+player.meleeWeapon.tag,1,YELLOW)
                screen.blit(meleeTagTitle,(mousePos[0]+10,mousePos[1]))
                damageTitle=font1.render("Damage:",1,YELLOW)
                screen.blit(damageTitle,(5,79))
                pygame.draw.rect(screen,getColour(player.meleeWeapon.damage/(30+player.attackBase+player.level)),(110,79,player.meleeWeapon.damage/(30+player.attackBase+player.level)*200,30))
                speedTitle=font1.render("Speed:",1,YELLOW)
                screen.blit(speedTitle,(5,119))
                pygame.draw.rect(screen,getColour((7-player.meleeWeapon.speed)/6),(110,119,(7-player.meleeWeapon.speed)/3*100,30))
                sharpnessTitle=font1.render("Sharpness:",1,YELLOW)
                screen.blit(sharpnessTitle,(5,159))
                pygame.draw.rect(screen,getColour(player.meleeWeapon.sharpness/(13+int(player.level/5))),(110,159,player.meleeWeapon.sharpness/(13+int(player.level/5))*200,30))
                knockbackTitle=font1.render("Knockback:",1,YELLOW)
                screen.blit(knockbackTitle,(5,199))
                pygame.draw.rect(screen,getColour(player.meleeWeapon.knockback/(128+player.level)),(110,199,player.meleeWeapon.knockback/(128+player.level)*200,30))
                rangeTitle=font1.render("Range:",1,YELLOW)
                screen.blit(rangeTitle,(5,239))
                pygame.draw.rect(screen,getColour(player.meleeWeapon.attackRange/6),(110,239,player.meleeWeapon.attackRange/3*100,30))
            elif mouseOver(153,217,5,69) and player.rangedClass:
                rangedTagTitle=font2.render(player.rangedName+": "+player.rangedWeapon.tag,1,YELLOW)
                screen.blit(rangedTagTitle,(mousePos[0]+10,mousePos[1]))
                damageTitle=font1.render("Damage:",1,YELLOW)
                screen.blit(damageTitle,(5,79))
                pygame.draw.rect(screen,getColour(player.rangedWeapon.damage/(31+player.level)),(110,79,player.rangedWeapon.damage/(31+player.level)*200,30))
                speedTitle=font1.render("Speed:",1,YELLOW)
                screen.blit(speedTitle,(5,119))
                pygame.draw.rect(screen,getColour((8-player.rangedWeapon.speed)/7),(110,119,(8-player.rangedWeapon.speed)/7*200,30))
                sharpnessTitle=font1.render("Sharpness:",1,YELLOW)
                screen.blit(sharpnessTitle,(5,159))
                pygame.draw.rect(screen,getColour(player.rangedWeapon.sharpness/(11+int(player.level/5))),(110,159,player.rangedWeapon.sharpness/(11+int(player.level/5))*200,30))
                knockbackTitle=font1.render("Knockback:",1,YELLOW)
                screen.blit(knockbackTitle,(5,199))
                pygame.draw.rect(screen,getColour(player.rangedWeapon.knockback/128),(110,199,player.rangedWeapon.knockback/15*25,30))
                velocityTitle=font1.render("Velocity:",1,YELLOW)
                screen.blit(velocityTitle,(5,239))
                pygame.draw.rect(screen,getColour(player.rangedWeapon.velocity/26),(110,239,player.rangedWeapon.velocity/13*100,30))
        else:
            player.image.set_colorkey(BASE)
            wallList.update()
            itemList.update()
            enemyList.update()
            for enemy in enemyList:
                if onScreen(enemy):
                    enemy.ai(wallList,player,enemyList,weaponLists,screen)
            doorList.update(player)
            weaponLists[0].update(weaponLists,enemyList,player,wallList)
            weaponLists[1].update(weaponLists,enemyList,player,wallList)
            animationList.update()
            backgroundList.draw(screen)
            wallList.draw(screen)
            screen.blit(player.image,(player.rect.x,player.rect.y))
            enemyList.draw(screen)
            projectileList.draw(screen)
            itemList.draw(screen)
            doorList.draw(screen)
            for enemy in enemyList:
                pygame.draw.rect(screen,getColour(enemy.hp/enemy.maxHp),(enemy.rect.left,enemy.rect.bottom,enemy.hp/enemy.maxHp*enemy.rect.width,2))
            animationList.draw(screen)
            foregroundList.draw(screen)
            pygame.draw.rect(screen,GREY,(0,494,704,102))
            pygame.draw.rect(screen,BLACK,(501,495,203,31))
            pygame.draw.rect(screen,BLACK,(501,530,203,31))
            pygame.draw.rect(screen,BLACK,(501,565,203,31))
            pygame.draw.rect(screen,BLUE,(340,510,70,70))
            screen.blit(player.rangedWeapon.sprite,(343,513))
            pygame.draw.rect(screen,getColour(player.hp/player.maxHp),(504,498,player.hp/player.maxHp*197,25))
            if player.meleeClass:
                pygame.draw.rect(screen,RED,(504,533,(player.meleeWeapon.speed-player.meleeAttackCooldown)/player.meleeWeapon.speed*197,25))
            if player.rangedClass:
                pygame.draw.rect(screen,BLUE,(504,568,(player.rangedWeapon.speed-player.rangedAttackCooldown)/player.rangedWeapon.speed*197,25))
            screen.blit(hpTitle,(465,495))
            screen.blit(meleeTitle,(440,530))
            screen.blit(rangedTitle,(430,565))
            player.update(wallList,itemList,enemyList,weaponLists,backgroundList,doorList)
            if player.effects[4]:
                player.effects[4]-=1
                pygame.draw.rect(screen,BLACK,(0,0,704,496))
        if player.effects[9]:
            player.effects[9]-=1
            pygame.draw.rect(screen,BLACK,(0,495,704,101))
        if not paused and player.effects[11]:
            player.effects[11]-=1
            screen.blit(pygame.transform.flip(screen,True,True),(0,0))
        if player.hp<=0:
            screen.fill(BLACK)
            screen.blit(gameOverTitle,(200,250))
            gameOverSound.play()
            pygame.display.flip()
            player.death(wallList,itemList,enemyList,weaponLists,backgroundList,doorList)
            sleep(5)
        else:
            pygame.display.flip()
            clock.tick(fps)
            print(clock.get_fps())
    pygame.quit()
if __name__=="__main__":
    main()
