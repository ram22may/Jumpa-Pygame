import pygame
import random

pygame.init()
pygame.mixer.init()

#SOUNDEFFECTS
#MAIN BACKGROUND MUSIC
Start = False


pygame.mixer.music.load("BGMusic.mp3")
pygame.mixer.music.play(-1) # loops forever
pygame.mixer.music.set_volume(0.0)


swordhitSound = pygame.mixer.Sound("SwordHitSound.mp3") 
swordequipSound = pygame.mixer.Sound("SwordEquipSound.mp3")
potionequipSound = pygame.mixer.Sound("PotionEquipSound.wav")
pickaxeequipSound = pygame.mixer.Sound("PickaxeEquipSound.mp3")
pickaxehitSound = pygame.mixer.Sound("PickaxeHitSound.mp3")
BrokenSwordSound = pygame.mixer.Sound("BrokenSword.mp3")
BrokenPickaxeSound = pygame.mixer.Sound("BrokenPickaxe.mp3")
PotionHealSound = pygame.mixer.Sound("PotionHealSound.wav")
GoldMinedSound = pygame.mixer.Sound("GoldMinedSound.mp3")
PotionBuySound = pygame.mixer.Sound("PotionBuySound.mp3")

OgreSpawnSound = pygame.mixer.Sound("OgreSpawnSound.mp3")
OgreGroanSound = pygame.mixer.Sound("OgreGroanSound.wav")

WalkingSound = pygame.mixer.Sound("WalkingSound.mp3")
JumpSound = pygame.mixer.Sound("JumpSound.mp3")
FireObstacleSound = pygame.mixer.Sound("FireObstacleWooshSound.mp3")
OgreProjectileSound = pygame.mixer.Sound("OgreProjectileSound.mp3")

WinSound = pygame.mixer.Sound("WinSound.mp3")
LoseSound = pygame.mixer.Sound("LoseSound.mp3")




font = pygame.font.SysFont(None, 40)
itemfont = pygame.font.SysFont(None, 20)

NOTPAUSED = True

Bossgravity = 200

#EQUIPPED OPTIONS 
HpPotion_equipped = True
Sword_equipped = False
Pickaxe_equipped = False

#500 milliseconds (0.5 second) if 1000 then (1 second)
#SWORD COOLDOWN
last_hit_timeSword = 0
hit_cooldownSword = 500  

#PICKAXE COOLDOWN
last_hit_timePickaxe = 0
hit_cooldownPickaxe = 500

#OBSTACLE HIT COOLDOWN
last_hit_timeObstacle = 0
hit_cooldownObstacle = 500

#OGREPROJECTILE1 COOLDOWN
last_hit_timeOgreProjectile1 = 0
hit_cooldownOgreProjectile1 = 500

#OGREPROJECTILE2 COOLDOWN
last_hit_timeOgreProjectile2 = 0
hit_cooldownOgreProjectile2 = 500

#OGREPROJECTILE3 COOLDOWN
last_hit_timeOgreProjectile3 = 0
hit_cooldownOgreProjectile3 = 500

WIDTH = 800
HEIGHT = 400

TotalGold = 0



goldore_x = random.randint(100, 700)
goldore_y = 300
goldore_w = 50
goldore_h = 50
goldore_hp = 25

player_x = 100
player_y = 300
player_w = 50
player_h = 50
player_hp = 100

ogre_x = 250
ogre_y = -100 #166
ogre_w = 300
ogre_h = 200
ogreProjectileDamage = random.randint(5, 15)
ogreHealth = 250
OgreSpawned = False
OgreDead = False

ogre_projectile1_x = random.randint(100, 300)
ogre_projectile1_y = -50
ogre_projectile1_w = 50
ogre_projectile1_h = 50

ogre_projectile2_x = random.randint(200, 400)
ogre_projectile2_y = -50
ogre_projectile2_w = 50
ogre_projectile2_h = 50

ogre_projectile3_x = random.randint(300, 500)
ogre_projectile3_y = -50
ogre_projectile3_w = 50
ogre_projectile3_h = 50

Hp_potion_x = player_x + player_w
Hp_potion_y = player_y
Hp_potion_w = 50
Hp_potion_h = 50
Hp_potion_healable = False
Hp_potion_heal = 25
Hp_potion_amount = 0

pickaxe_x = player_x + player_w
pickaxe_y = player_y
pickaxe_w = 25
pickaxe_h = 50
PickaxeAtk = False
PickaxeDamage = random.randint(5, 10)
PickaxeHealthDeduct = random.randint(5, 10)
PickaxeHealth = 100
PickaxeBroken = False

sword_x = player_x + player_w
sword_y = player_y 
sword_w = 25
sword_h = 50
SwordAtk = False
SwordDamage = random.randint(8, 10)
SwordHealthDeduct = random.randint(1, 3)
SwordHealth = 100
SwordBroken = False

obstacle_x = 600
obstacle_y = 300
obstacle_w = 50
obstacle_h = 50
ob_damage = 25

platform_x = 0
platform_y = 350
platform_w = 800
platform_h = 50

sky_x = 0
sky_y = 450
sky_w = 800
sky_h = 750

cloud_x = 500
cloud_y = 50
cloud_w = 150
cloud_h = 50

#VALUES

ogreSpeed = 300
ogre_direction = 1

score = 0
base_obspeed = 250
speed_factor = 10

cloudspeed = 200
velocity_y = 0
jump_power = -10

gravity = 0.425




pygame.display.set_caption("Jumpa")
screen = pygame.display.set_mode((WIDTH, HEIGHT))



running = True
onGround = True
GameOver = False
Win = False
clock = pygame.time.Clock()


hpPotion_img = pygame.image.load("HPPOTION.png").convert()
Small_hpPotion_img = pygame.transform.scale(hpPotion_img, (50, 50))
Small_hpPotion_img.set_colorkey((255, 255, 255))
hpPotion_img.set_colorkey((255, 255, 255))

goldore_img = pygame.image.load("GOLDORE.png").convert()
goldore_img.set_colorkey((255, 255, 255))

player_img = pygame.image.load("PLAYER.png").convert()
player_img.set_colorkey((255, 255, 255))

ob_img = pygame.image.load("FIREOBSTACLE.png").convert()
ob_img.set_colorkey((255, 255, 255))


GrassPLATFORM_img = pygame.image.load("GRASSPLATFORM.jpg")
sky_img = pygame.image.load("SKY.jpg")

cloud_img = pygame.image.load("CLOUD.png").convert()
cloud_img.set_colorkey((255, 255, 255))

pickaxe_img = pygame.image.load("PICKAXE.png").convert()
pickaxe_img.set_colorkey((255, 255, 255))

sword_img = pygame.image.load("SWORD.png").convert()
sword_img.set_colorkey((255, 255, 255))

ogre_img = pygame.image.load("OGRE_ENEMY.png").convert()
ogre_img.set_colorkey((255, 255, 255))

ogre_projectile1_img = pygame.image.load("OGREPROJECTILE.png").convert()
ogre_projectile1_img.set_colorkey((255, 255, 255))

ogre_projectile2_img = pygame.image.load("OGREPROJECTILE.png").convert()
ogre_projectile2_img.set_colorkey((255, 255, 255))

ogre_projectile3_img = pygame.image.load("OGREPROJECTILE.png").convert()
ogre_projectile3_img.set_colorkey((255, 255, 255))




player_img = pygame.transform.scale(player_img, (player_w, player_h))
ob_img = pygame.transform.scale(ob_img, (obstacle_w, obstacle_h))
GrassPLATFORM_img = pygame.transform.scale(GrassPLATFORM_img, (platform_w, platform_h))
sky_img = pygame.transform.scale(sky_img, (sky_w, sky_h))
cloud_img = pygame.transform.scale(cloud_img, (cloud_w, cloud_h))
sword_img = pygame.transform.scale(sword_img, (sword_w, sword_h))
#pickaxe_img = pygame.transform.scale()

ogre_img = pygame.transform.scale(ogre_img, (ogre_w, ogre_h))

while running:
   
    screen.fill((255, 255, 255))
    DT = clock.tick(60) / 1000

    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_q:
                Start = True

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                running = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE and onGround:
                JumpSound.play()
                velocity_y = jump_power
                onGround = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_1 and GameOver == False:
                swordequipSound.play()
                HpPotion_equipped = False
                Hp_potion_healable = False

                Sword_equipped = True
                Pickaxe_equipped = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_2 and GameOver == False:
                pickaxeequipSound.play()
                HpPotion_equipped = False
                Hp_potion_healable = False

                Sword_equipped = False
                Pickaxe_equipped = True

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_3 and GameOver == False:
                potionequipSound.play()
                #screen.blit(hpPotion_img, (player_x + player_w, player_y))

                HpPotion_equipped = True
                Hp_potion_healable = True

                Sword_equipped = False
                Pickaxe_equipped = False
        
            
            

        
                
                
        #IF YOURE HOLDING THE LEFT CLICK BUTTON THEN IT SCREEN BLITS SWORD
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1 and Sword_equipped and SwordBroken == False and GameOver == False:  # Left click
                SwordAtk = True
                swordhitSound.play()



        #IF YOURE DONE HOLDING THE LEFT CLICK BUTTON THEN IT DOESNT SCREEN BLIT SWORD ANYMORE IN LINE 250+
        if event.type == pygame.MOUSEBUTTONUP:
            if event.button == 1:
                SwordAtk = False



        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1 and Pickaxe_equipped and PickaxeBroken == False and GameOver == False:
                PickaxeAtk = True
                pickaxehitSound.play()

        if event.type == pygame.MOUSEBUTTONUP:
            if event.button == 1:
                PickaxeAtk = False

        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 3 and HpPotion_equipped and TotalGold >= 10:
                
                PotionBuySound.play()
                TotalGold -= 10
                Hp_potion_amount += 1

   
            

            

        

        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1 and Hp_potion_healable == True and Hp_potion_amount >= 1:
                Hp_potion_amount -= 1

                PotionHealSound.play()

                player_hp += Hp_potion_heal

                if player_hp >= 100:
                    player_hp = 100


  



        






        keys = pygame.key.get_pressed()

    if keys[pygame.K_a] and GameOver == False and Start:
        player_x -= 250 * DT

    if keys[pygame.K_d] and GameOver == False and Start:
        player_x += 250 * DT


    #CHECK IF SWORD DURABILITY IS <=0 then SwordAtk = False
    if SwordHealth <= 0 and SwordBroken == False:

        SwordAtk = False
        BrokenSwordSound.play()
        SwordBroken = True

    if SwordHealth <= 0:
        SwordAtk = False


    if PickaxeHealth <= 0 and PickaxeBroken == False:

        PickaxeAtk = False
        BrokenPickaxeSound.play()
        PickaxeBroken = True
        

    if PickaxeHealth <= 0:
        PickaxeAtk = False



    if SwordAtk:
        screen.blit(sword_img, (player_x + player_w, player_y - 10))

    if PickaxeAtk:
        screen.blit(pickaxe_img, (player_x + player_w, player_y))

        
                
    if not GameOver and Start:

        pygame.mixer.music.set_volume(1.0)

        #TOTAL GOLD TEXT


        if goldore_hp > 0:
            screen.blit(goldore_img, (goldore_x, goldore_y - 25))
            goldore_hpText = font.render("HP: " + str(goldore_hp) + "/ 25", True, (0, 0, 0))
            screen.blit(goldore_hpText, (goldore_x, goldore_y - 30))

        if goldore_hp <= 0:
            GoldMinedSound.play()

            goldore_hp = 25
            TotalGold += 10

            goldore_x = random.randint(100, 700)



        if HpPotion_equipped:
            HpPotion_equippedText = itemfont.render("Currently equipped: Healing potion " + str(Hp_potion_amount), True, (0, 0, 0))
            screen.blit(HpPotion_equippedText, (0, 25))

        if Sword_equipped:
            Sword_equippedText = itemfont.render("Currently equipped: Sword", True, (0, 0, 0))
            screen.blit(Sword_equippedText, (0, 25))

            swordHealthText = font.render("Sword durability: " + str(SwordHealth), True, (255, 165, 0))
            screen.blit(swordHealthText, (0, 50))

        if Pickaxe_equipped:
            Pickaxe_equippedText = itemfont.render("Currently equipped: Pickaxe", True, (0, 0, 0))
            screen.blit(Pickaxe_equippedText, (0, 25))

            PickaxeHealthText = font.render("Pickaxe durability: " + str(PickaxeHealth), True, (255, 165, 0))
            screen.blit(PickaxeHealthText, (0, 50))



        #IF SCORE >= 51 THEN IT SETS A MAXIMUM OBSPEED
        if score >= 51:
            obspeed = obspeed #base_obspeed #TO SET A CONSTANT SPEED IF SCORE >= SCORETHRESHOLD
            print(obspeed) #FOR LOOKING IN THE MAIN OBSPEED

        #IF SCORE IS < 51 THEN IT MULTIPLIES THE OBSPEED
        elif score < 51:
            obspeed = base_obspeed + (score * speed_factor)
            print(obspeed) #FOR LOOKING IN THE MAIN OBSPEED

        velocity_y += gravity
        player_y += velocity_y
        
        if player_y >= 300:
            player_y = 300
            velocity_y = 0
            onGround = True

        
        obstacle_x -= obspeed * DT
        cloud_x -= cloudspeed * DT

        #WALL BOUNDARY FOR LEFT X AXIS PLAYER POSITION
        if player_x <= 0:
            player_x = 0

        #WALL BOUNDARY FOR RIGHT X AXIS PLAYER POSITION
        if player_x >= 750:
            player_x = 750

        #ADD SCORE IF OBSTACLE REACHES -40 PIXELS TO THE LEFT
        if obstacle_x < -40:
            obstacle_x = random.randint(800, 1000)
            #FireObstacleSound.play()
            score += 1

        #CLOUD RECTANGLE FOR AESTHETIC PURPOSE ONLY
        if cloud_x < -150:
            cloud_x = random.randint(800, 1000)
            cloud_y = random.randint(50, 75)

                
        # OBJECT RECTANGLES
               
        goldoreRectangle = pygame.Rect(goldore_x, goldore_y, goldore_w, goldore_h)

        playerRectangle = pygame.Rect(player_x, player_y, player_w, player_h)
    
        ogreRectangle = pygame.Rect(ogre_x, ogre_y, ogre_w, ogre_h)

        ogreProj1Rectangle = pygame.Rect(ogre_projectile1_x, ogre_projectile1_y, ogre_projectile1_w, ogre_projectile1_h)
        ogreProj2Rectangle = pygame.Rect(ogre_projectile2_x, ogre_projectile2_y, ogre_projectile2_w, ogre_projectile2_h)
        ogreProj3Rectangle = pygame.Rect(ogre_projectile3_x, ogre_projectile3_y, ogre_projectile3_w, ogre_projectile3_h)
        
        pickaxeRectangle = pygame.Rect(player_x + player_w, player_y, pickaxe_w, pickaxe_h)

        swordRectangle = pygame.Rect(player_x + player_w, player_y, sword_w, sword_h)

        obRectangle = pygame.Rect(obstacle_x, obstacle_y, obstacle_w, obstacle_h)
        
        platformRectangle = pygame.Rect(0, 350, 800, 50)

        #OGRE PROJECTILE 1 DAMAGE COOLDOWN

        current_time_ogreprojectile1 = pygame.time.get_ticks()

        if playerRectangle.colliderect(ogreProj1Rectangle):
            if current_time_ogreprojectile1 - last_hit_timeOgreProjectile1 > hit_cooldownOgreProjectile1:
                player_hp -= ogreProjectileDamage

                last_hit_timeOgreProjectile1 = current_time_ogreprojectile1

        #OGRE PROJECTILE 2 DAMAGE COOLDOWN

        current_time_ogreprojectile2 = pygame.time.get_ticks()

        if playerRectangle.colliderect(ogreProj2Rectangle):
            if current_time_ogreprojectile2 - last_hit_timeOgreProjectile2 > hit_cooldownOgreProjectile2:
                player_hp -= ogreProjectileDamage

                last_hit_timeOgreProjectile2 = current_time_ogreprojectile2

        #OGRE PROJECTILE 3 DAMAGE COOLDOWN

        current_time_ogreprojectile3 = pygame.time.get_ticks()

        if playerRectangle.colliderect(ogreProj3Rectangle):
            if current_time_ogreprojectile3 - last_hit_timeOgreProjectile3 > hit_cooldownOgreProjectile3:
                player_hp -= ogreProjectileDamage

                last_hit_timeOgreProjectile3 = current_time_ogreprojectile3
        
        #OBSTACLE DAMAGE COOLDOWN
        current_timeObstacle = pygame.time.get_ticks()

        if playerRectangle.colliderect(obRectangle):
            if current_timeObstacle - last_hit_timeObstacle > hit_cooldownObstacle:
                player_hp -= ob_damage

                
                playerHealthText = itemfont.render("Health: " + str(player_hp) + "/ 100", True, (200, 0, 0))

                last_hit_timeObstacle = current_timeObstacle


        #SWORD DAMAGE COOLDOWN
        current_timeSword = pygame.time.get_ticks()

        #IF SWORD HITBOX COLLIDES WITH OGRE AND SwordAtk IS TRUE OR BEING HELD THEN IT DEDUCTS VALUES LINE 204 FOR SwordAtk Screen Blit
        if swordRectangle.colliderect(ogreRectangle) and SwordAtk:
            if current_timeSword - last_hit_timeSword > hit_cooldownSword:
                ogreHealth -= SwordDamage
                SwordHealth -= SwordHealthDeduct


                last_hit_timeSword = current_timeSword

        #PICKAXE DAMAGE COOLDOWN FOR GOLD ORE
        current_timePickaxe = pygame.time.get_ticks()

        if pickaxeRectangle.colliderect(goldoreRectangle) and PickaxeAtk:
            if current_timePickaxe - last_hit_timePickaxe > hit_cooldownPickaxe:
                goldore_hp -= PickaxeDamage
                PickaxeHealth -= PickaxeHealthDeduct

                last_hit_timePickaxe = current_timePickaxe

            
        #IF SCORE REACHES 25 OR MORE THEN IT SPAWNS THE OGRE BOSS
        if score >= 25:
            if OgreSpawned == False:
                OgreSpawnSound.play()
                OgreGroanSound.play()
                OgreSpawned = True

            if ogreHealth >= 1 and OgreDead == False:   

                

                ogre_y += Bossgravity * DT

                ogre_projectile1_y += Bossgravity * DT
                ogre_projectile2_y += Bossgravity * DT
                ogre_projectile3_y += Bossgravity * DT

                if ogre_projectile1_y >= 320:

                    OgreProjectileSound.play()

                    ogre_projectile1_y = -50
                    ogre_projectile1_x = random.randint(100, 700)
                
                if ogre_projectile2_y >= 320:
                    ogre_projectile2_y = -50
                    ogre_projectile2_x = random.randint(100, 700)

                if ogre_projectile3_y >= 320:
                    ogre_projectile3_y = -50
                    ogre_projectile3_x = random.randint(100, 700)

                


            


                #WALL BOUNDARY FOR OGRE BOSS RIGHT X AXIS
                if ogre_x >= 700:
                    ogre_direction = -1

                #WALL BOUNDARY FOR OGRE BOSS LEFT X AXIS
                if ogre_x <= -200:
                    ogre_direction = 1



                #SHOW OGRE BOSS
                screen.blit(ogre_img, (ogre_x, ogre_y))

                OgreHealthText = font.render("Boss health: " + str(ogreHealth), True, (255, 0, 0))
                screen.blit(OgreHealthText, (300, 50))

                screen.blit(ogre_projectile1_img, (ogre_projectile1_x, ogre_projectile1_y))
                screen.blit(ogre_projectile2_img, (ogre_projectile2_x, ogre_projectile2_y))
                screen.blit(ogre_projectile3_img, (ogre_projectile3_x, ogre_projectile3_y))

                
            


        #IF OGRE BOSS EXCEEDS 166 Y AXIS THEN IT SETS IT TO GROUND 166
        if ogre_y >= 166:
            ogre_y = 166

            ogre_x += ogreSpeed * ogre_direction * DT 

        #IF OGRE HEALTH <= 0 THEN THE OGRE IMAGE DISAPPEARS
        if ogreHealth <= 0:
            OgreDead = True
            ogreDeathText = font.render("Ogre: Slayed", True, (0, 255, 0))
            screen.blit(ogreDeathText, (0, 75))

            #TO STOP THE OGRE PROJECTILES
            ogre_projectile1_y = -50
            ogre_projectile2_y = -50
            ogre_projectile3_y = -50
            ogreProjectileDamage = 0


            


        #IF SCORE >= 50 AND OGREHEALTH <= 0 THEN YOU WIN
        if score >= 50 and ogreHealth <= 0:
            WinSound.play()
            Win = True
            GameOver = True

        #IF PLAYER HEALTH <= 0 YOU LOST
        if player_hp <= 0:
            GameOver = True
            LoseSound.play()
            pygame.mixer.music.stop()
            







    #SCORE TEXT
    scoreText = font.render("Score: " + str(score), True, (0, 0, 0))
    screen.blit(scoreText, (350, 0))

    #SWORD HEALTH TEXT
    #swordHealthText = font.render("Sword durability: " + str(SwordHealth), True, (255, 165, 0))
    #screen.blit(swordHealthText, (0, 25))

    #PLAYER HEALTH TEXT
    playerHealthText = font.render("Health: " + str(player_hp) + "/ 100", True, (0, 200, 0))
    screen.blit(playerHealthText, (0, 0))
    


    #IF WIN IS TRUE THEN YOU WON TEXT
    if Win:
        winText = font.render("You won!", True, (0, 255, 0))
        screen.blit(winText, (275, 150)) #X = 400 if PC
    #IF GAVEOVER IS TRUE THEN YOU LOST TEXT
    elif GameOver:
        GameOverText = font.render("You died! Game over!", True, (255, 0, 0))
        screen.blit(GameOverText, (260, 150)) #X = 400 if PC

                
    screen.blit(player_img, (player_x, player_y))
    
    screen.blit(ob_img, (obstacle_x, obstacle_y))

    screen.blit(GrassPLATFORM_img, (platform_x, platform_y))

    screen.blit(sky_img, (sky_x, sky_y))
    
    screen.blit(cloud_img, (cloud_x, cloud_y))
    #pygame.draw.rect(screen, (230, 230, 230), (cloud_x, cloud_y, cloud_w, cloud_h))

    TotalGoldText = font.render("Gold: " + str(TotalGold), True, (0, 0, 0))
    screen.blit(TotalGoldText, (350, 25)) 

      

        

    InstructionsText = itemfont.render(
        "A/D Move | Space Jump",
        True,
        (0, 0, 0)
    )
    screen.blit(InstructionsText, InstructionsText.get_rect(topright=(780, 25)))

    InstructionsText2 = itemfont.render(
        "1 Sword | 2 Pickaxe",
        True,
        (0, 0, 0)
    )
    screen.blit(InstructionsText2, InstructionsText2.get_rect(topright=(780, 45)))

    InstructionsText3 = itemfont.render(
        "3 Potion | LClick Use | RClick Buy",
        True,
        (0, 0, 0)
    )
    screen.blit(InstructionsText3, InstructionsText3.get_rect(topright=(780, 65)))

    if Hp_potion_healable:
        screen.blit(Small_hpPotion_img, (player_x + player_w - 10, player_y - 5))

    ExitText = itemfont.render("Press ESC to exit the game.", True, (255, 0, 0))
    screen.blit(ExitText, (620, 5))        

    if Start == False:
        StartText = font.render("Press Q to start the game.", True, (0, 165, 0))
        screen.blit(StartText, (250, 150))
    
    pygame.display.update()
pygame.quit()